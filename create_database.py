from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
import os
import chromadb
import shutil

CHROMA_PATH = "chroma"
DATA_PATH = "data"


def main():
    print("🚀 Starting database creation...")
    generate_data_store()


def generate_data_store():
    documents = load_documents()

    if len(documents) == 0:
        print("❌ No documents found in data/")
        return

    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    print("📂 Loading documents...")
    docs = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".md"):
            file_path = os.path.join(DATA_PATH, file)
            loader = TextLoader(file_path, encoding="utf-8")
            loaded = loader.load()

            # category = filename without extension (e.g. "hr.md" -> "hr")
            category = os.path.splitext(file)[0].lower()

            for d in loaded:
                d.metadata["category"] = category

            docs.extend(loaded)

    print(f"Loaded {len(docs)} documents")
    return docs


def split_text(documents: list[Document]):
    print("✂️ Splitting text into chunks (by Q&A block)...")
    chunks = []

    for doc in documents:
        # Split on each '## ' heading — keep the heading attached to its answer
        parts = doc.page_content.split("\n## ")

        for i, part in enumerate(parts):
            part = part.strip()
            if not part:
                continue

            # Re-add the '## ' prefix except for the very first part
            # (which may contain the doc title/intro before the first heading)
            content = part if i == 0 else "## " + part

            if len(content) < 10:  # skip near-empty fragments (e.g. title-only)
                continue

            chunks.append(Document(
                page_content=content,
                metadata=doc.metadata
            ))

    print(f"Created {len(chunks)} chunks")
    return chunks


def save_to_chroma(chunks: list[Document]):
    print("🧠 Creating embeddings + vector DB...")

    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    embedding_model = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    client = chromadb.PersistentClient(path=CHROMA_PATH)

    db = Chroma(
        client=client,
        embedding_function=embedding_model
    )

    db.add_documents(chunks)

    print("✅ Database created successfully!")


if __name__ == "__main__":
    main()