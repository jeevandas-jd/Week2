import fitz
import os


def extractPDF(filePath):

    try:
        doc= fitz.open(filePath)

        textFile=os.path.splitext(filePath)[0]+'.txt'
        with open(textFile, 'w', encoding='utf-8') as f:
            for page in doc:
                text=page.get_text()
                f.write(text)
        doc.close()
        print(f"Text extracted to {textFile}")
    except Exception as e:
        print(f"Error extracting text from {filePath}: {e}")
        return None
    return textFile