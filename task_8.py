import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Task8(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.compute_button = QPushButton("Compute Runge-Kutta 2nd Order")
        self.output_text = QTextEdit()

        self.layout.addWidget(self.compute_button)
        self.layout.addWidget(self.output_text)
        self.setLayout(self.layout)

        self.compute_button.clicked.connect(self.runge_kutta)

    def dydx(self, x, y):
        return np.exp(x) - y

    def runge_kutta(self):
        try:
            x0, y0, h, x_target = 0, 0, 0.1, 0.2
            y = y0
            x = x0
            while x < x_target:
                k1 = h * self.dydx(x, y)
                k2 = h * self.dydx(x + h / 2, y + k1 / 2)
                y += k2
                x += h
            self.output_text.setText(f'Runge-Kutta 2nd Order Result: y({x_target}) = {y:.4f}')
        except Exception as e:
            self.output_text.setText(f'Error: {e}')
