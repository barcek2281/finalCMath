import sys
import matplotlib.pyplot as plt
import numpy as np
import warnings
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt6 import uic


class Task2(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        warnings.simplefilter("ignore")

        # Create a Figure and Canvas
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Layout to add Matplotlib canvas
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Plot function
        self.plot_graph()

    def plot_graph(self, x_range=(0, 3)):
        """Generate a plot for the function f(x) within the user-defined range"""
        self.ax.clear()
        x = np.linspace(x_range[0], x_range[1], 100)
        y = self.f(x)
        self.ax.plot(x, y, label="f(x) = x^4 - 5x^2 + 4")
        self.ax.axhline(0, color='black', linewidth=0.5)  # X-axis
        self.ax.grid(True)
        self.ax.legend()
        self.canvas.draw()

    def f(self, x):
        return x ** 4 - 5 * x ** 2 + 4

    def false_position(self, a, b, tol=1e-6, max_iter=100):
        """False Position Method"""
        if self.f(a) * self.f(b) >= 0:
            return None, None

        iteration = 0
        c_old = a
        while iteration < max_iter:
            c = (a * self.f(b) - b * self.f(a)) / (self.f(b) - self.f(a))
            if abs(self.f(c)) < tol:
                return c, iteration

            if self.f(a) * self.f(c) < 0:
                b = c
            else:
                a = c

            relative_error = abs((c - c_old) / c) if c != 0 else float('inf')
            if relative_error < tol:
                return c, iteration

            c_old = c
            iteration += 1

        return c, iteration

    def bisection(self, a, b, tol=1e-6, max_iter=100):
        """Bisection Method"""
        if self.f(a) * self.f(b) >= 0:
            return None, None

        iteration = 0
        c_old = a
        while iteration < max_iter:
            c = (a + b) / 2
            if abs(self.f(c)) < tol:
                return c, iteration

            if self.f(a) * self.f(c) < 0:
                b = c
            else:
                a = c

            relative_error = abs((c - c_old) / c) if c != 0 else float('inf')
            if relative_error < tol:
                return c, iteration

            c_old = c
            iteration += 1

        return c, iteration