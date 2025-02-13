import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Task8(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # Связываем с главным UI

        # Подключаем кнопку к функции Runge-Kutta
        self.parent.pushButton_13.clicked.connect(self.runge_kutta)

    def dydx(self, x, y):
        """Функция правой части уравнения dy/dx = e^x - y."""
        return np.exp(x) - y

    def runge_kutta(self):
        try:
            # Получаем h из lineEdit
            h = float(self.parent.lineEdit_for_h_3.text())

            # Начальные условия
            x0, y0 = 0, 0
            x_target = 0.2
            y = y0
            x = x0

            # Метод Рунге-Кутты 2-го порядка
            while x < x_target:
                k1 = h * self.dydx(x, y)
                k2 = h * self.dydx(x + h / 2, y + k1 / 2)
                y += k2
                x += h

            # Выводим результат в lineEdit
            self.parent.lineEdit_16_answer_task8.setText(f"{y:.4f}")

        except Exception as e:
            self.parent.lineEdit_16_answer_task8.setText(f"Error: {e}")