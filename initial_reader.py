import pdfplumber
import pytesseract

def is_scanned_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        if first_page.extract_text() is None:
            return True
        return False
    
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            image = page.to_image()
            page_text = pytesseract.image_to_string(image.original)
            text += page_text
    return text

pdf_path = "./testfiles/Trek Allen - Work Order 2025-08-05.pdf"

if is_scanned_pdf(pdf_path):
    print("This is a scanned PDF. OCR is required.")
else:
    print("This is a text-based PDF. Can be processed directly.")
    
#extracted_text = extract_text_from_pdf(pdf_path)
#print(extracted_text)