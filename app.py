import streamlit as st
import hashlib
from query_data import (
    answer_question_cached, build_vectorstore_from_file, answer_question_from_upload,
    check_and_record_upload
)

st.set_page_config(page_title="RAG Document Q&A", page_icon="📄", layout="centered")

st.title("📄 RAG Document Q&A System")
st.caption("Ask questions across Technical, HR, and CV documents — powered by Groq")

MODEL_LABELS = {
    "openai/gpt-oss-120b": "GPT-OSS 120B (best quality)",
    "openai/gpt-oss-20b": "GPT-OSS 20B (faster)",
}


def get_client_ip():
    try:
        headers = st.context.headers
        forwarded = headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return headers.get("Host", "unknown")
    except Exception:
        return "unknown"


mode = st.radio(
    "Source",
    ["Ask about Anuvab (preloaded)", "Upload your own document"],
    horizontal=True
)

with st.sidebar:
    st.header("⚙️ Settings")
    if mode == "Ask about Anuvab (preloaded)":
        category = st.selectbox(
            "Document category",
            options=["all", "technical", "hr", "cv"],
            format_func=lambda x: x.upper() if x != "all" else "All Categories"
        )
    model = st.selectbox(
        "LLM model",
        options=list(MODEL_LABELS.keys()),
        format_func=lambda m: MODEL_LABELS[m],
    )
    st.markdown("---")
    st.markdown("Built with LangChain + Chroma + Groq")

MAX_FILE_SIZE_MB = 5

if mode == "Upload your own document":
    st.caption("You can upload up to 2 documents per day. Uploading a new file replaces the current one — only one document is active at a time.")

    uploaded_file = st.file_uploader("Upload a document (max 5MB)", type=["pdf", "docx", "txt", "csv", "md"])
    if uploaded_file:
        if uploaded_file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
            st.error(f"File too large. Max size is {MAX_FILE_SIZE_MB}MB.")
            st.stop()

        file_hash = hashlib.md5(uploaded_file.getvalue()).hexdigest()

        if st.session_state.get("last_file_hash") != file_hash:
            ip = get_client_ip()
            allowed, remaining = check_and_record_upload(ip)

            if not allowed:
                st.error("Daily upload limit reached for your network. Try again tomorrow.")
                st.stop()

            with st.spinner("Processing document..."):
                st.session_state.vectorstore = build_vectorstore_from_file(uploaded_file)
                st.session_state.last_file_hash = file_hash
                st.session_state.messages = []
            st.success(f"Loaded: {uploaded_file.name} ({remaining} uploads left today)")
    else:
        st.session_state.pop("vectorstore", None)
        st.session_state.pop("last_file_hash", None)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and msg.get("sources"):
            with st.expander(f"🔎 Sources (relevance: {msg['score']:.2f})"):
                for s in msg["sources"]:
                    label = s.get("category", "").upper() or "UPLOAD"
                    st.markdown(f"**[{label}]** (score: {s['score']:.2f})")
                    st.text(s["content"] + "...")
                    st.markdown("---")

query = st.chat_input("Ask a question about the documents...")

if query:
    if mode == "Upload your own document" and "vectorstore" not in st.session_state:
        st.warning("Upload a document first.")
    else:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                if mode == "Upload your own document":
                    result = answer_question_from_upload(
                        st.session_state.vectorstore, query, model=model
                    )
                else:
                    result = answer_question_cached(query, category, model)

            st.markdown(result["answer"])

            if result["sources"]:
                with st.expander(f"🔎 Sources (relevance: {result['score']:.2f})"):
                    for s in result["sources"]:
                        label = s.get("category", "").upper() or "UPLOAD"
                        st.markdown(f"**[{label}]** (score: {s['score']:.2f})")
                        st.text(s["content"] + "...")
                        st.markdown("---")

        st.session_state.messages.append({
            "role": "assistant",
            "content": result["answer"],
            "score": result.get("score") or 0,
            "sources": result["sources"]
        })