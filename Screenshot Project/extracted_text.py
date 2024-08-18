import cv2
import pytesseract
import sys

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    print("Extracted Text:")
    print(text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_text.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    extract_text_from_image(image_path)
