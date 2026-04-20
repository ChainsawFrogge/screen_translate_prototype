import time, os
import threading
from Cocoa import NSApplication
from Cocoa import NSFont, NSFontManager
from CoreText import CTFontManagerRegisterFontsForURL
from Foundation import NSDictionary
from Foundation import NSURL

from overlay import Overlay, OverlayWindow

from ocr import extract_text_boxes
from translate import translate

import mss
import numpy as np

sct = mss.mss()
monitor = sct.monitors[1]

def capture():
    return np.array(sct.grab(monitor))

def convert_y(y, h):
    screen_h = monitor["height"]
    return screen_h - y - h

def load_font(path):
    url = NSURL.fileURLWithPath_(path)
    success = CTFontManagerRegisterFontsForURL(url, 0, None)
    print("FONT REGISTERED:", success)
    for f in NSFontManager.sharedFontManager().availableFonts():
        if "pokemon" in f.lower():
            print(f)

class App:
    def __init__(self):
        self.app = NSApplication.sharedApplication()

        self.window = OverlayWindow.alloc().init()

        font_path = os.path.join(
            os.path.dirname(__file__),
            "./assets/fonts/kvn-pokemon-gen-5.ttf"
        )

        load_font(font_path)
        self.font = NSFont.fontWithName_size_("REAL_NAME_HERE", 18)
        self.overlay = Overlay(self.window, self.font)

        from Cocoa import NSFontManager

        fonts = NSFontManager.sharedFontManager().availableFonts()

        for f in fonts:
            if "pokemon" in f.lower():
                print("FOUND FONT:", f)

    def worker(self):
        last = {}

        while True:
            img = capture()
            boxes = extract_text_boxes(img)

            new_state = {}

            for b in boxes:
                text = translate(b["text"])
                key = (b["x"], b["y"])

                new_state[key] = text

                if last.get(key) != text:
                    y = convert_y(b["y"], b["h"])
                    self.overlay.draw_text(b["x"], y, text)

            last = new_state

            time.sleep(0.8)

    def run(self):
        t = threading.Thread(target=self.worker, daemon=True)
        t.start()

        self.window.makeKeyAndOrderFront_(None)
        self.app.run()


if __name__ == "__main__":
    App().run()