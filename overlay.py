import tkinter as tk

class Overlay:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "black")
        self.root.overrideredirect(True)

        self.canvas = tk.Canvas(self.root, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    def draw_text(self, x, y, text):
        self.canvas.create_text(
            x, y,
            text=text,
            fill="white",
            anchor="nw",
            font=("Arial", 12)
        )

    def clear(self):
        self.canvas.delete("all")

    def run(self):
        self.root.mainloop()