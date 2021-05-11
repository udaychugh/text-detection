import pytesseract as tess
tess.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

from PIL import Image
img_src=input("Enter Soruce of Image=")
img=Image.open(img_src)
text=tess.image_to_string(img)
print(text)
