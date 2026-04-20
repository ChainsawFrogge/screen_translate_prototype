from capture import capture_screen
from ocr import extract_text
from translate import translate
import time

seen = set()

while True:
    img = capture_screen()
    text = extract_text(img)

    if text.strip() and text not in seen:
        seen.add(text)
        translated = translate(text)

        print("Original:", text)
        print("Translated:", translated)
        print("-----")

    time.sleep(1)