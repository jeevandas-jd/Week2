import os
import fitz


class PDFtoText(object):
    def __init__(self,pdf_path=None,txt_path=None):
        self.pdf_path = pdf_path
        self.txt_path = txt_path
        self.text= [] # list to store text from each page
        if pdf_path is None or os.path.exists(pdf_path) is False: # check if the file exists
            self.pdf_path = input("Enter the path to the PDF file: ")
    
    def extract_text(self): # extract text from the PDF file
        try:

            doc=fitz.open(self.pdf_path)
            
            #print(f"type of doc: {type(doc)}")
            #print(f"number of pages: {doc.page_count}")
            
            for page in doc:
                text=page.get_text()
                self.text.append(text) # append text to the list
            print("Text extraction complete.")
        except Exception as e:
            print(f"An error occurred while extracting text: {e}")
    def save_text(self): # save the extracted text to a file
        if self.txt_path is None:
            self.txt_path = os.path.splitext(self.pdf_path)[0] + ".txt"# create a txt file with the same name as the pdf file
        try:
            with open(self.txt_path, "w", encoding="utf-8") as f:# open the file in write mode
                for page in self.text:
                    f.write(page)
            print(f"Text saved to {self.txt_path}")
        except Exception as e:
            print(f"An error occurred while saving text: {e}")
    def get_text(self):
        for page in self.text:
            print(page)
    def clear(self):# clear the text list and file paths
        self.text = []
        self.pdf_path = None
        self.txt_path = None
        print("PDFtoText object cleared.")
    def Load_PDF(self,pdf_path=None):# load a new PDF file
        if pdf_path is None:
            pdf_path = input("Enter the path to the PDF file: ")
        if os.path.exists(pdf_path) is False:
            print(f"File {pdf_path} does not exist.")
            return
        self.pdf_path = pdf_path
        self.clear()
        self.extract_text()
        self.save_text()
        print("PDF loaded and text extracted.")
