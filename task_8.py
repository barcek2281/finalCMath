import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import uic
class RungeKuttaSecondOrder(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.button = QPushButton("Compute", self)
        self.button.clicked.connect(self.compute_rk2)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
    
    def f(self, x, y):
        return np.exp(x) - y

    def compute_rk2(self):
        self.ax.clear()
        x = np.linspace(0, 2, 100)
        y_exact = np.exp(x) - x
        y_rk = [self.runge_kutta_2nd_order(0, 1, 0.1, xi) for xi in x]
        self.ax.plot(x, y_exact, label='Exact Solution', linestyle='dashed')
        self.ax.plot(x, y_rk, label='Runge-Kutta 2nd Order')
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()
    
    def runge_kutta_2nd_order(self, x0, y0, h, x_target):
        x, y = x0, y0
        while x < x_target:
            k1 = h * self.f(x, y)
            k2 = h * self.f(x + h, y + k1)
            y += (k1 + k2) / 2
            x += h
        return y
