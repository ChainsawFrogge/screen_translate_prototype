from PyQt6 import QtWidgets, QtCore, QtGui
import sys

class Overlay(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Make window borderless + always on top
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )

        # Make background transparent
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        # Full screen
        self.showFullScreen()

        self.labels = []

    def clear(self):
        for label in self.labels:
            label.deleteLater()
        self.labels = []

    def draw_text(self, x, y, text):
        label = QtWidgets.QLabel(self)
        label.setText(text)
        label.setStyleSheet("""
            color: white;
            font-size: 18px;
            font-weight: bold;
            background: transparent;
        """)
        label.adjustSize()
        label.move(x, y)
        label.show()

        self.labels.append(label)