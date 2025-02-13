from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np
from PyQt6.QtWidgets import QWidget

class Task5(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.x_edits = [
            self.parent.lineEdit_31,
            self.parent.lineEdit_33,
            self.parent.lineEdit_29,
            self.parent.lineEdit_34,
            self.parent.lineEdit_30
        ]
        self.y_edits = [
            self.parent.lineEdit_18,
            self.parent.lineEdit_28,
            self.parent.lineEdit_32,
            self.parent.lineEdit_35,
            self.parent.lineEdit_36
        ]

        # Поле для вывода результата
        self.answer_edit = self.parent.lineEdit_16_anwer

        # Кнопка для расчёта
        self.solve_button = self.parent.pushButton_4
        self.solve_button.clicked.connect(self.fit_curve)

        # График
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Добавляем в layout
        self.parent.tab2_verticalLayout_task5.addWidget(self.canvas)

    def fit_curve(self):

        try:
            x = []
            y = []
            for x_edit, y_edit in zip(self.x_edits, self.y_edits):
                x_text = x_edit.text().strip()
                y_text = y_edit.text().strip()

                if not x_text or not y_text:
                    self.answer_edit.setText("Error:  All fields must be filled in")
                    return

                x.append(float(x_text))
                y.append(float(y_text))

            x = np.array(x, dtype=float)
            y = np.array(y, dtype=float)

            coeffs = np.polyfit(x, y, 2)
            poly = np.poly1d(coeffs)

            equation = f"{coeffs[0]:.4f} x² + {coeffs[1]:.4f} x + {coeffs[2]:.4f}"
            self.answer_edit.setText(equation)

            self.ax.clear()
            self.ax.scatter(x, y, color='red', label="Initial points")
            x_range = np.linspace(min(x), max(x), 100)
            self.ax.plot(x_range, poly(x_range), label="Approximation", color="blue")
            self.ax.legend()
            self.ax.set_xlabel("X")
            self.ax.set_ylabel("Y")
            self.ax.set_title("Quadratic approximation")

            self.canvas.draw()

        except Exception as e:
            self.answer_edit.setText(f'Error: {e}')
