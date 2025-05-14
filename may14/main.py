
import extractPDF

from storeDB import addToDB
from chunkTXT import chunkTXT
"""pdfPath = 'Week2/may14/sample.pdf'

textFile=extractPDF.extractPDF(pdfPath)
if textFile:
    print(f"Text extracted to {textFile}")
else:
    print("Failed to extract text.")"""

txt_path="/home/jeevandas/KlaWa/Week2/may14/sample.txt"
document=chunkTXT(txt_path)

addToDB(document,"resume2")