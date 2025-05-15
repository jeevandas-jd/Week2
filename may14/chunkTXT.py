

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
import os
load_dotenv()

def chunkTXT(path):

    text=""
    try:
        with open(path,"r") as f:
            for lines in f:
                text=text +f"{lines}"
            text_spliter=SemanticChunker(GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
                             breakpoint_threshold_type="percentile")
            documents=text_spliter.create_documents([text])
            #print(f"documnet after chunking\n{"*"*20}\n{documents}")
            with open(os.path.splitext(path)[0]+"Chunk.txt","a") as f:
                for lines in documents:
                    f.write(lines.page_content)
            return documents
    
    except Exception as e:
        print(f"error {e} occured")
    
        return None

    

"""googl_api=os.getenv("API_KEY")


text_spliter=SemanticChunker(GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
                             breakpoint_threshold_type="percentile")

text=""
try:
    with open("/home/jeevandas/KlaWa/Week2/may14/sample.txt","r") as f:
        for lines in f:
            text=text +f"\n {lines}"
except Exception as e:
    print(f"error {e} occured")
documents=text_spliter.create_documents([text])

print(documents)"""