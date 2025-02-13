import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Task7(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  # Сохраняем родителя

        # Подключаем кнопку
        self.parent.pushButton_6.clicked.connect(self.romberg_integration)

        # Настраиваем график
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Используем уже существующий layout, а не создаём новый
        self.graph_layout = self.parent.tab2_verticalLayout_task7
        self.graph_layout.addWidget(self.canvas)

    def function(self, x):
        return x ** 2

    def romberg_integration(self):
        try:
            h_value = self.parent.lineEdit_for_h.text().strip()
            if not h_value:
                self.parent.lineEdit_16_answer_7.setText("Error: Enter a value for h.")
                return

            h = float(h_value)
            result, _ = spi.quad(self.function, 0, 1)  # Используем quad вместо romberg
            self.parent.lineEdit_16_answer_7.setText(f'{result:.4f}')

            # Рисуем график
            self.plot_function()

        except ValueError:
            self.parent.lineEdit_16_answer_7.setText("Error: Invalid input.")
        except Exception as e:
            self.parent.lineEdit_16_answer_7.setText(f'Error: {e}')

    def plot_function(self):
        self.ax.clear()  # Очищаем старый график

        # Данные для графика
        x = np.linspace(0, 1, 100)
        y = self.function(x)

        # График функции
        self.ax.plot(x, y, label="f(x) = x²", color='blue')

        # Заливка интегрируемой области
        x_fill = np.linspace(0, 1, 100)
        y_fill = self.function(x_fill)
        self.ax.fill_between(x_fill, y_fill, color='blue', alpha=0.3, label="Integral Area")

        # Настройки графика
        self.ax.set_title("Function f(x) = x² with Integral Area")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.legend()
        self.ax.grid()

        self.canvas.draw()  # Обновляем график
