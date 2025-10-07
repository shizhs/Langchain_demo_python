import os

from supabase import Client, create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

client: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def insert_embedding(table: str, doc_id: str, embedding: list, document: str):
    """
    Insert an embedding vector and its metadata into a Supabase table.
    Args:
        table (str): Supabase table name
        doc_id (str): Unique document ID
        embedding (list): Embedding vector (list of floats)
        document (str): Original document text
    """
    data = {"id": doc_id, "embedding": embedding, "document": document}
    response = client.table(table).insert(data).execute()
    return response
