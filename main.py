from langchain_ollama import ChatOllama, OllamaEmbeddings

from supabase_vector_search import query_by_vector_similarity

# Initialize LangChain Ollama components
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
chat_model = ChatOllama(model="llama3.1:8b", temperature=0)

print("Ask a question (type 'q' to quit):")
while True:
    # an example input
    input_text = input("Question: ").strip()
    if input_text.lower() == "q":
        print("Exiting.")
        break

    # generate an embedding for the input and retrieve the most relevant doc
    query_vector = embeddings.embed_query(input_text)

    # Query Supabase for the most similar document
    result = query_by_vector_similarity("embeddings", query_vector, limit=1)
    if result:
        best_match = result[0]
        print("Most similar document:", best_match["document"])
        print("Distance:", best_match["distance"])
    else:
        print("No match found.")

    data = best_match["document"] if result else "No relevant document found."

    # generate a response combining the prompt and data we retrieved in step 2
    prompt = f"Using this data: {data}. Respond to this prompt: {input_text}"
    response = chat_model.invoke(prompt)

    print("Answer:", response.content)
