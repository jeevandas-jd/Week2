import os
import json
import extractPDF
from storeDB import addToDB
from chunkTXT import chunkTXT
from chatboat import get_chroma_collection, get_query_embedding, search_collection, generate_answer

class ChatWithPDF:
    def __init__(self):
        self.availablePDFs = []
        self.logJSON = "/home/jeevandas/KlaWa/Week2/may14/pdf-log.json"
        self.selectedPDF = None
        self.currentPDF = None

        # Load existing log (if any)
        if os.path.exists(self.logJSON):
            with open(self.logJSON, "r") as f:
                self.availablePDFs = json.load(f)

    def upload_pdf(self, path):
        if os.path.exists(path):
            txt_path = extractPDF.extractPDF(path)
            documents = chunkTXT(txt_path)
            collection_name = os.path.splitext(os.path.basename(path))[0]
            addToDB(documents=documents, collectionName=collection_name)
            self.currentPDF = collection_name

            # Update log
            if collection_name not in self.availablePDFs:
                self.availablePDFs.append(collection_name)
                with open(self.logJSON, "w") as f:
                    json.dump(self.availablePDFs, f)

            print(f"[INFO] Successfully processed and stored: {path}")
        else:
            raise FileNotFoundError(f"[ERROR] File not found: {path}")
    def switchPDF(self,path):
        pass


    def ask_question(self, query):
        if not self.currentPDF:
            raise ValueError("[ERROR] No PDF selected. Please upload a PDF first.")
        
        collection = get_chroma_collection(collection_name=self.currentPDF)
        embedding = get_query_embedding(query)
        documents = search_collection(collection, embedding)
        answer = generate_answer(documents, query)
        return answer






