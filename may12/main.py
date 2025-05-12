
import PDFtoTXT

pdf_path="Week2/may12/sample.pdf"


pdf_to_text = PDFtoTXT.PDFtoText(pdf_path=pdf_path)
pdf_to_text.extract_text()
pdf_to_text.save_text()