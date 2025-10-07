import os

import numpy as np
from supabase import Client, create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def query_by_vector_similarity(table: str, query_vector: list, limit: int = 1):
    """
    Query Supabase table for the most similar embedding using pgvector extension.
    Args:
        table (str): Supabase table name
        query_vector (list): Query embedding vector
        limit (int): Number of results to return
    Returns:
        List of rows sorted by similarity (closest first)
    """
    # Convert Python list to PostgreSQL vector literal
    response = supabase.rpc(
        "vector_search", {"query_vector": query_vector, "limit_count": 1}
    ).execute()
    return response.data
