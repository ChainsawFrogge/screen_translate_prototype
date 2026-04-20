import time
import mss
import numpy as np

from ocr import extract_text_boxes
from translate import translate
from overlay import Overlay

sct = mss.mss()

monitor = sct.monitors[1]

overlay = Overlay()

def capture():
    img = np.array(sct.grab(monitor))
    return img

# cache for stable rendering
seen = {}

while True:
    img = capture()
    boxes = extract_text_boxes(img)

    overlay.clear()

    for b in boxes:
        text = b["text"]
        x, y = b["x"], b["y"]

        translated = translate(text)

        # keep text persistent
        key = (x, y, text)
        seen[key] = translated

        overlay.draw_text(x, y, translated)

    overlay.root.update()

    time.sleep(0.5)