import sys
import matplotlib.pyplot as plt
import numpy as np
import warnings
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from scipy.optimize import fsolve

class Task1(QWidget):
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

        # Plot something
        self.plot_graph()

    def plot_graph(self, x_range=(-2, 2)):
        """Generate a simple sine wave plot"""
        self.ax.clear()
        x = np.linspace(*x_range, 100)
        y = self.f(x)
        self.ax.plot(x, y, label="")
        self.ax.grid(True)
        self.canvas.draw()  # Refresh the canvas

    def calc_root(self, x_range=(-2, 2), approx_root=-0):
        initial_guesses = np.linspace(x_range[0], x_range[1], 100)
        roots = set()

        for guess in initial_guesses:
            root = fsolve(self.f, guess)[0]
            if x_range[0] <= root <= x_range[1]:  # Ensure the root is within range
                roots.add(round(root, 6))  # Round to avoid close duplicates

        roots = sorted(list(roots))  # Sort the roots

        # Find the closest root to the given approximate root
        if roots:
            closest_root = min(roots, key=lambda r: abs(r - approx_root))
            absolute_error = abs(closest_root - approx_root)
            return roots, closest_root, absolute_error

        return [], None, None  # No valid root found

    def f(self, x):
        return x ** 3 - 3 * x + 2