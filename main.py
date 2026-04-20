import sys
import time
import threading
import mss
import numpy as np

from PyQt6 import QtWidgets

from overlay import Overlay
from ocr import extract_text_boxes
from translate import translate

# screen capture
sct = mss.mss()
monitor = sct.monitors[1]

def capture():
    img = np.array(sct.grab(monitor))
    return img

class App:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.overlay = Overlay()

    def run_loop(self):
        seen = set()

        while True:
            img = capture()
            boxes = extract_text_boxes(img)

            self.overlay.clear()

            for b in boxes:
                text = b["text"]
                translated = translate(text)

                key = (text, b["x"], b["y"])
                if key not in seen:
                    seen.add(key)

                self.overlay.draw_text(
                    b["x"],
                    b["y"],
                    translated
                )

            time.sleep(0.5)

    def run(self):
        thread = threading.Thread(target=self.run_loop, daemon=True)
        thread.start()

        sys.exit(self.app.exec())

if __name__ == "__main__":
    App().run()