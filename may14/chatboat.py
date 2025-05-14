from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
import chromadb
import uuid

def search_chroma(query: str, collection_name: str = "resume2"):
    # Init embedding model and chroma client
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-pro")
    chroma_client = chromadb.PersistentClient(path="vectorDB/")
    collection = chroma_client.get_or_create_collection(name=collection_name)

    # Embed the query
    query_embedding = embeddings.embed_query(query)

    # Search the DB
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    
    # Return the documents only
    documents = results["documents"][0] if results and results["documents"] else []
    return documents

def chat_with_docs(query: str, context_docs: list):
    # Init Gemini LLM
    chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    # Combine retrieved docs into context
    context = "\n".join(context_docs)

    # Create prompt
    prompt = f"""Use the following context to answer the user's question:

    Context:
    {context}

    Question:
    {query}
    """

    response = chat_model([HumanMessage(content=prompt)])
    return response.content
query = "Who is jeevandas"
docs = search_chroma(query, collection_name="resume2")
response = chat_with_docs(query, docs)
print("Bot:", response)
