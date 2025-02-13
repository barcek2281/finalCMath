import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
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

        # Используем уже существующий layout
        self.graph_layout = self.parent.tab2_verticalLayout_task7
        self.graph_layout.addWidget(self.canvas)

    def function(self, x):
        return x ** 2

    def romberg_integration(self):
        try:
            h1_value = self.parent.lineEdit_for_h.text().strip()
            h2_value = self.parent.lineEdit_for_h_2.text().strip()
            h3_value = self.parent.lineEdit_for_h_4.text().strip()

            if not h1_value or not h2_value or not h3_value:
                self.parent.lineEdit_16_answer_7.setText("Error: Enter values for h1, h2, h3.")
                return

            h_values = [float(h1_value), float(h2_value), float(h3_value)]
            results = [spi.quad(self.function, 0, h)[0] for h in h_values]

            # Отображаем в поле ответа последний результат
            self.parent.lineEdit_16_answer_7.setText(f'{results[-1]:.4f}')

            # Заполняем таблицу
            self.update_romberg_table(h_values, results)

            # Отрисовка графика
            self.plot_function(h_values[-1])

        except ValueError:
            self.parent.lineEdit_16_answer_7.setText("Error: Invalid input.")
        except Exception as e:
            self.parent.lineEdit_16_answer_7.setText(f'Error: {e}')

    def update_romberg_table(self, h_values, results):
        """Заполняет таблицу значениями h и результатами интегрирования."""
        self.parent.tableWidget.setRowCount(len(h_values))
        self.parent.tableWidget.setColumnCount(2)
        self.parent.tableWidget.setHorizontalHeaderLabels(["h", "Result"])

        for i, (h, result) in enumerate(zip(h_values, results)):
            self.parent.tableWidget.setItem(i, 0, QTableWidgetItem(f"{h:.4f}"))
            self.parent.tableWidget.setItem(i, 1, QTableWidgetItem(f"{result:.4f}"))

    def plot_function(self, h):
        self.ax.clear()  # Очищаем старый график

        # Данные для графика
        x = np.linspace(0, h, 100)
        y = self.function(x)

        # График функции
        self.ax.plot(x, y, label="f(x) = x²", color='blue')

        # Заливка интегрируемой области
        x_fill = np.linspace(0, h, 100)
        y_fill = self.function(x_fill)
        self.ax.fill_between(x_fill, y_fill, color='blue', alpha=0.3, label="Integral Area")

        # Настройки графика
        self.ax.set_title(f"Integral of f(x) = x² from 0 to {h}")
        self.ax.set_xlabel("x")
        self.ax.set_ylabel("f(x)")
        self.ax.legend()
        self.ax.grid()

        self.canvas.draw()  # Обновляем график