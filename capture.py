import mss
import numpy as np

sct = mss.mss()

def capture_screen():
    monitor = sct.monitors[1]
    screenshot = sct.grab(monitor)
    return np.array(screenshot)