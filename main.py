from capture import capture_screen
from ocr import extract_text
from translate import translate
import time


def is_valid(text):
    text = text.strip()
    return len(text) > 5 and not text.isdigit()

seen = set()

while True:
    img = capture_screen()
    text = extract_text(img)
    
    if text.strip() and is_valid(text):
        print("Original:", text)
    
    if text.strip() and text not in seen:
        seen.add(text)
        translated = translate(text)

        print("Original:", text)
        print("Translated:", translated)
        print("-----")

    time.sleep(1)