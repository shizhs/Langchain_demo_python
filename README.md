# LangChain + Supabase Online Embedding Demo

## Summary
This project demonstrates how to use LangChain with Ollama for generating embeddings and storing them online in Supabase using the pgvector extension. It supports interactive CLI querying and vector similarity search.

## Features
- **Supabase Integration:**
  - Embeddings and metadata are stored in a Supabase PostgreSQL table with pgvector.
  - Utility functions for inserting and querying embeddings.
- **Vector Search:**
  - Fast nearest-neighbor search using pgvector’s `<->` operator.
- **Interactive CLI:**
  - `main.py` allows multi-question input until you type 'q' to quit.
  - Each question is embedded, searched against Supabase, and answered using the most relevant document.

## Setup Instructions

### 1. Enable pgvector in Supabase
Run this in the Supabase SQL editor:
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### 2. Create the Embeddings Table
Adjust the vector dimension to match your embedding size (e.g., 768 or 1024):
```sql
CREATE TABLE embeddings (
  id text PRIMARY KEY,
  embedding vector(1024),
  document text
);
```

### 3. Environment Variables
Set your Supabase credentials in `.env.local` or your shell:
```
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Store Embeddings
Run `embedding.py` to generate and store embeddings in Supabase:
```bash
python embedding.py
```

### Interactive Query
Run `main.py` and ask questions interactively:
```bash
python main.py
```
Type 'q' to quit.

## How It Works
- Embeddings are generated using LangChain/Ollama and stored in Supabase.
- When you ask a question, its embedding is computed and the most similar document is retrieved from Supabase using vector similarity search.
- The answer is generated using the retrieved document and your question.

## Troubleshooting
- Ensure pgvector is enabled and your table uses the correct vector dimension.
- Make sure your Supabase credentials are set.
- If you change the embedding size, update the table schema accordingly.

## Contributing
Pull requests are welcome! See the PR for details on features and setup.