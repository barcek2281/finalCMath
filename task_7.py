import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Task7(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.h_label = QLabel("h =")
        self.lineEdit_for_h = QLineEdit()
        self.compute_button = QPushButton("Submit")
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.layout.addWidget(self.h_label)
        self.layout.addWidget(self.lineEdit_for_h)
        self.layout.addWidget(self.compute_button)
        self.layout.addWidget(self.output_text)
        self.setLayout(self.layout)

        self.compute_button.clicked.connect(self.romberg_integration)

    def function(self, x):
        return x ** 2

    def romberg_integration(self):
        try:
            h_value = self.lineEdit_for_h.text().strip()
            if not h_value:
                self.output_text.setText("Error: Please enter a value for h.")
                return

            h = float(h_value)
            result = spi.romberg(self.function, 0, 1, divmax=5)
            self.output_text.setText(f'Romberg Integration Result: {result:.4f}')
        except ValueError:
            self.output_text.setText("Error: Invalid input. Please enter a numeric value for h.")
        except Exception as e:
            self.output_text.setText(f'Error: {e}')