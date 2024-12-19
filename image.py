from collections import Counter
import pytesseract
from PIL import Image
import re

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the input image
image_path = 'image.png'

# Load the image using PIL
image = Image.open(image_path)

# Perform OCR using pytesseract to extract text
extracted_text = pytesseract.image_to_string(image)

# Print the extracted content
print("Extracted Contents from the Image:")
print("-" * 50)
print(extracted_text)
print("-" * 50)

# Process the extracted text: Normalize, remove punctuation, and split into words
words = re.findall(r'\b\w+\b', extracted_text.lower())

# Count the occurrences of each word
word_count = Counter(words)

# Display the word count map
print("Word Count Map:")
for word, count in word_count.items():
    print(f"{word}: {count}")
