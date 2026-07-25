FROM python:3.11-slim

WORKDIR /app

# System deps needed by some packages (chromadb, pypdf, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps first (better layer caching — only re-runs on requirements.txt change)
COPY requirements.txt .

# Install CPU-only torch first — avoids pulling ~2GB+ of unused NVIDIA/CUDA packages
# that sentence-transformers would otherwise drag in via the default GPU torch build
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the embedding model at BUILD time, not runtime —
# this is the key fix for slow cold starts on Render
RUN python -c "from langchain_huggingface import HuggingFaceEmbeddings; HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')"

# Copy the rest of the app
COPY . .

# Build the persisted vector DB at image build time, since chroma/ is gitignored
# and won't exist in a fresh container otherwise
RUN python create_database.py

# Render sets $PORT dynamically — Streamlit must bind to it, not a hardcoded port
EXPOSE 8501

CMD streamlit run app.py \
    --server.port=$PORT \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --server.enableCORS=false \
    --server.enableXsrfProtection=false