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

        # Настраиваем график
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Добавляем график в существующий layout
        self.graph_layout = self.parent.tab2_verticalLayout_task8
        self.graph_layout.addWidget(self.canvas)

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

            # Списки для хранения значений
            x_values = [x0]
            y_values = [y0]

            # Метод Рунге-Кутты 2-го порядка
            while x < x_target:
                k1 = h * self.dydx(x, y)
                k2 = h * self.dydx(x + h / 2, y + k1 / 2)
                y += k2
                x += h

                x_values.append(x)
                y_values.append(y)

            # Выводим результат в lineEdit
            self.parent.lineEdit_16_answer_task8.setText(f"{y:.4f}")

            # Обновляем график
            self.plot_runge_kutta(x_values, y_values)

        except Exception as e:
            self.parent.lineEdit_16_answer_task8.setText(f"Error: {e}")

    def plot_runge_kutta(self, x_values, y_values):
        """Строит график зависимости y(x) после решения уравнения."""
        self.ax.clear()  # Очищаем старый график

        # График решения
        self.ax.plot(x_values, y_values, marker='o', linestyle='-', color='blue', label="Runge-Kutta")

        # Настройки графика
        self.ax.set_title("Solution of dy/dx = e^x - y using Runge-Kutta")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("y")
        self.ax.legend()
        self.ax.grid()

        self.canvas.draw()  # Обновляем график
