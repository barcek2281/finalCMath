import numpy as np
from PyQt6.QtWidgets import QWidget


class Task5(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        # Собираем ссылки на поля x и y
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

    def fit_curve(self):
        """Считываем x и y из lineEdit'ов, строим квадратичную аппроксимацию, выводим результат."""
        try:
            # Считываем 5 точек, проверяем, что все введены
            x = []
            y = []
            for x_edit, y_edit in zip(self.x_edits, self.y_edits):
                x_text = x_edit.text().strip()
                y_text = y_edit.text().strip()

                if not x_text or not y_text:
                    self.answer_edit.setText("Error: Все поля должны быть заполнены")
                    return

                x.append(float(x_text))
                y.append(float(y_text))

            x = np.array(x, dtype=float)
            y = np.array(y, dtype=float)

            # Квадратичная аппроксимация (полином 2-й степени)
            coeffs = np.polyfit(x, y, 2)
            poly = np.poly1d(coeffs)

            # Форматируем уравнение
            equation = f"{coeffs[0]:.4f} x² + {coeffs[1]:.4f} x + {coeffs[2]:.4f}"
            self.answer_edit.setText(equation)

        except Exception as e:
            self.answer_edit.setText(f'Error: {e}')
