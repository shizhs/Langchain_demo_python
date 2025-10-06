from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain.schema import ChatMessage
from langchain.tools import Tool
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate

from embedding import collection

# Initialize LangChain Ollama components
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
chat_model = ChatOllama(model="llama3.1", temperature=0)

# an example input
input_text = "What animals are llamas related to?"

# generate an embedding for the input and retrieve the most relevant doc
query_embedding = embeddings.embed_query(input_text)
results = collection.query(
  query_embeddings=[query_embedding],
  n_results=1
)
data = results['documents'][0][0]

# generate a response combining the prompt and data we retrieved in step 2
prompt = f"Using this data: {data}. Respond to this prompt: {input_text}"
response = chat_model.invoke(prompt)

print(response.content)