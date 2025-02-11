import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import uic
class RombergIntegration(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.input_field = QLineEdit(self)
        self.button = QPushButton("Compute", self)
        self.button.clicked.connect(self.compute_integral)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter integration limits (a b):"))
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def f(self, x):
        return x**2
    
    def compute_integral(self):
        self.ax.clear()
        a, b = map(float, self.input_field.text().split())
        x = np.linspace(a, b, 100)
        y = self.f(x)
        self.ax.plot(x, y, label='Function x^2')
        self.ax.fill_between(x, 0, y, alpha=0.3)
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()
