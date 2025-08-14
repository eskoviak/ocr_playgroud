import pdfplumber
import pytesseract
import cv2
from PIL import Image

image_path = "./testfiles/Trek_Allen_test Receipt.jpg"

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

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # Deskewing can be added here with more complex algorithms
    return binary


img = preprocess_image(image_path)
# Open the image using Pillow
#img = Image.open(image_path)

# Perform OCR using pytesseract
text = pytesseract.image_to_string(img)

# Print the extracted text
#print((text))
for c in text[0:64]:
    print(f"Character: {c} | ASCII: {ord(c)}")

#image = preprocess_image(pdf_path)

#if is_scanned_pdf(image_path):
#    print("This is a scanned PDF. OCR is required.")
#else:
#    print("This is a text-based PDF. Can be processed directly.")    
#    extracted_text = extract_text_from_pdf(pdf_path)
#    print(extracted_text)
#    #image_processed = preprocess_image(pdf_path)