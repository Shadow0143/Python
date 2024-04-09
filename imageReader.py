import os
import pytesseract
from PIL import Image

directory = './images'
files = os.listdir(directory)
image_files = [file for file in files if file.endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp','avif'))]
for image_file in image_files:
    image_path = os.path.join(directory, image_file)
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print(f"Text extracted from {image_file}:\n\n{text}\n\n\n")

