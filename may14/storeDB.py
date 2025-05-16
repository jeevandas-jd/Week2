import chromadb
import uuid
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def addToDB(documents, collectionName):


    try:
        chroma_client = chromadb.PersistentClient(path="vectorDB/")
        collection = chroma_client.create_collection(name=collectionName)

        # Extract raw texts
        texts = [doc.page_content for doc in documents]

        # Generate embeddings using LangChain wrapper
        embed_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-exp-03-07")
        embeddings = embed_model.embed_documents(texts)  # returns List[List[float]]
        collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=[str(uuid.uuid4()) for _ in range(len(texts))]
        )
        print("Documents added successfully!")
    except Exception as e:
        print(f"Error adding to ChromaDB: {e}")
