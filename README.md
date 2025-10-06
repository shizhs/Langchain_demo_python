# LangChain Basic Project

This project uses LangChain with Ollama for language model operations and vector embeddings.

## Environment Setup

### Prerequisites
- Python 3.8 or higher
- Ollama installed and running locally on port 11434

### Setup Instructions

1. **Activate the virtual environment:**
   ```bash
   source activate.sh
   ```
   
   Or manually:
   ```bash
   source venv/bin/activate
   ```

2. **Install dependencies (if not already installed):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Deactivate the environment when done:**
   ```bash
   deactivate
   ```

## Dependencies

- `langchain` - Core LangChain framework
- `langchain-ollama` - Ollama integration for LangChain
- `langchain-chroma` - ChromaDB vector store integration
- `pandas` - Data manipulation and analysis

## Project Files

- `main.py` - Main application script
- `embedding.py` - Embedding functionality (referenced in main.py)
- `realistic_restaurant_reviews.csv` - Sample data file
- `requirements.txt` - Python dependencies
- `activate.sh` - Convenience script for environment activation

## Usage

Make sure Ollama is running locally, then:

```bash
source activate.sh
python main.py
```

## Notes

- The project assumes Ollama is running on `http://localhost:11434`
- The embedding model used is `mxbai-embed-large`
- The language model used is `llama3.1`