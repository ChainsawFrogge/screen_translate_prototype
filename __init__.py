import tkinter as tk

class Overlay:
    def __init__(self):
        self.root = tk.Tk()

        # Always on top
        self.root.attributes("-topmost", True)

        # Make window transparent (macOS supported)
        self.root.attributes("-alpha", 0.8)

        # Remove window border
        self.root.overrideredirect(True)

        # Fullscreen transparent canvas
        self.canvas = tk.Canvas(
            self.root,
            bg="black",
            highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True)

        # Resize to screen size
        self.root.geometry("1920x1080")