import streamlit as st
import pytesseract
from PIL import Image
import cv2
import numpy as np

# Add the path to the tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title('Image to Text Extractor')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png",'jpeg'])

if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)[1]

    extracted_text = pytesseract.image_to_string(thresh, lang='eng')

    st.text_area("Extracted Text", extracted_text, height=400)
