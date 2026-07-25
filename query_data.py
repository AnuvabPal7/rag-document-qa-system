import os
import json
import argparse
import tempfile
from datetime import date

import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader, Docx2txtLoader, TextLoader, CSVLoader
)

load_dotenv()

CHROMA_PATH = "chroma"
UPLOAD_LOG_PATH = "upload_log.json"
MAX_UPLOADS_PER_IP_PER_DAY = 2


# ---------- Cached resources (built once per container process) ----------

@st.cache_resource
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


_embedding = get_embedding_model()


@st.cache_resource
def get_db():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    db = Chroma(client=client, embedding_function=_embedding)
    return db


# ---------- Preloaded (persisted) DB ----------

def get_relevant_context(db, query, category=None, k=10):
    filter_dict = {"category": category} if category and category != "all" else None
    results = db.similarity_search_with_relevance_scores(query, k=k, filter=filter_dict)

    if not results:
        return None, None, []

    score = results[0][1]
    if score < -0.35:
        return None, score, []

    context = "\n\n---\n\n".join([doc.page_content[:1000] for doc, _ in results])
    sources = [
        {"content": doc.page_content[:300], "category": doc.metadata.get("category", "unknown"), "score": s}
        for doc, s in results
    ]
    return context, score, sources


def build_prompt(context, query):
    return f"""
You are answering questions on behalf of a candidate, using ONLY the information in the context below.
The context contains the candidate's own first-person answers (e.g. "I am...", "My name is...").

RULES:
- Do NOT use outside knowledge
- Do NOT guess information
- Do NOT comment on what is or isn't in the context, just answer directly
- If the answer is genuinely missing, say only: "Not enough information in the document."
- Be clear, structured, and concise
- Answer as if you ARE the candidate speaking, using the context provided
- Do not mention "context", "document", or your reasoning process in the answer

Context:
{context}

Question:
{query}

Answer:
"""


_INTRO_QUERY_ALIASES = [
    "tell me about yourself",
    "tell me about yourself.",
    "introduce yourself",
    "walk me through your background",
    "give me a brief introduction",
]


def answer_question(query, category=None, model="llama-3.1-8b-instant"):
    normalized = query.strip().lower()

    if category == "cv" and normalized in _INTRO_QUERY_ALIASES:
        db = get_db()
        _, _, sources = get_relevant_context(db, "Tell me about yourself", category="cv", k=15)
        for s in sources:
            if s["content"].startswith("## Tell me about yourself"):
                answer_text = s["content"].split("\n", 1)[1] if "\n" in s["content"] else s["content"]
                return {"answer": answer_text, "score": 1.0, "sources": [s]}

    db = get_db()
    context, score, sources = get_relevant_context(db, query, category=category)

    if context is None:
        return {
            "answer": "No strong relevant information found in documents.",
            "score": score,
            "sources": []
        }

    prompt = build_prompt(context, query)
    answer = get_groq_response(prompt, model=model)
    return {"answer": answer, "score": score, "sources": sources}


@st.cache_data(ttl=3600)
def answer_question_cached(query, category, model):
    """Cached wrapper — skips re-hitting Groq for identical repeated questions within an hour."""
    return answer_question(query, category=category, model=model)


# ---------- Upload mode (in-memory, per-session) ----------

def build_vectorstore_from_file(uploaded_file):
    """Build an in-memory (non-persisted) Chroma vectorstore from a single uploaded file."""
    suffix = os.path.splitext(uploaded_file.name)[1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    try:
        if suffix == ".pdf":
            loader = PyPDFLoader(tmp_path)
        elif suffix == ".docx":
            loader = Docx2txtLoader(tmp_path)
        elif suffix == ".csv":
            loader = CSVLoader(tmp_path)
        else:  # .txt, .md, fallback
            loader = TextLoader(tmp_path, encoding="utf-8")

        documents = loader.load()
    finally:
        os.remove(tmp_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    # No client, no persist_directory -> lives in memory only, dies with the session
    vectorstore = Chroma.from_documents(chunks, embedding=_embedding)
    vectorstore._chunk_count = len(chunks)
    return vectorstore


def get_relevant_context_from_store(vectorstore, query, k=5):
    total_chunks = vectorstore._collection.count()
    effective_k = total_chunks if total_chunks <= 15 else k

    results = vectorstore.similarity_search_with_relevance_scores(query, k=effective_k)

    if not results:
        return None, None, []

    score = results[0][1]
    context = "\n\n---\n\n".join([doc.page_content[:1000] for doc, _ in results])
    sources = [{"content": doc.page_content[:300], "score": s} for doc, s in results]
    return context, score, sources


def build_upload_prompt(context, query):
    return f"""
You are a helpful assistant answering questions about a document that was uploaded by the user.
Use ONLY the information in the context below to answer.

RULES:
- Do NOT use outside knowledge
- Do NOT guess information
- Do NOT speak in first person or pretend to be the subject of the document
- Answer factually and neutrally, referring to the document's subject in third person where relevant
- If the answer is genuinely missing, say only: "Not enough information in the document."
- Be clear, structured, and concise
- Do not mention "context" or your reasoning process in the answer

Context:
{context}

Question:
{query}

Answer:
"""


def answer_question_from_upload(vectorstore, query, model="llama-3.1-8b-instant"):
    context, score, sources = get_relevant_context_from_store(vectorstore, query)

    if context is None:
        return {
            "answer": "No relevant information found in the uploaded document.",
            "score": score,
            "sources": []
        }

    prompt = build_upload_prompt(context, query)
    answer = get_groq_response(prompt, model=model)
    return {"answer": answer, "score": score, "sources": sources}


# ---------- Per-IP daily upload limit ----------

def _load_upload_log():
    if not os.path.exists(UPLOAD_LOG_PATH):
        return {}
    try:
        with open(UPLOAD_LOG_PATH, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}


def _save_upload_log(log):
    try:
        with open(UPLOAD_LOG_PATH, "w") as f:
            json.dump(log, f)
    except IOError:
        pass


def check_and_record_upload(ip_address):
    today = str(date.today())
    log = _load_upload_log()

    key = f"{ip_address}:{today}"
    count = log.get(key, 0)

    if count >= MAX_UPLOADS_PER_IP_PER_DAY:
        return False, 0

    log[key] = count + 1
    log = {k: v for k, v in log.items() if k.endswith(today)}
    _save_upload_log(log)

    return True, MAX_UPLOADS_PER_IP_PER_DAY - (count + 1)


# ---------- Groq call ----------

def get_groq_response(prompt, model="llama-3.1-8b-instant"):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            pass

    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str)
    parser.add_argument("--category", type=str, default=None)
    args = parser.parse_args()

    print("\nRAG System Starting...")
    db = get_db()
    print("Vector database loaded")

    context, score, _ = get_relevant_context(db, args.query_text, category=args.category)

    if context is None:
        print("\nNo strong relevant information found in documents.")
        return

    print(f"Relevance Score: {score:.2f}")

    prompt = build_prompt(context, args.query_text)
    print("\nSending to Groq...")

    answer = get_groq_response(prompt)

    print("\n================ FINAL ANSWER ================\n")
    print(answer)
    print("\n=============================================\n")


if __name__ == "__main__":
    main()