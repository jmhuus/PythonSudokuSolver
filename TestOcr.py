try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('random_numbers.png')))



#================
# # French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# # Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open('test.png')))

# # Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open('test.png')))

# # Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open('test.png')))

# # In order to bypass the internal image conversions, just use relative or absolute image path
# # NOTE: If you don't use supported images, tesseract will return error
# print(pytesseract.image_to_string('test.png'))

# # get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')

# # get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')