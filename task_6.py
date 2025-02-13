import sys
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi


class Task6(QMainWindow):
    def __init__(self, parent=None):  # Добавляем parent с дефолтным значением None
        super().__init__(parent)
        loadUi("untitled.ui", self)
        self.pushButton_5.clicked.connect(self.interpolate)


    def lagrange_interpolation(self, x, y, x_val):
        result = 0
        for i in range(len(x)):
            term = y[i]
            for j in range(len(x)):
                if i != j:
                    term *= (x_val - x[j]) / (x[i] - x[j])
            result += term
        return result

    def interpolate(self):
        try:
            # Read input values
            x = np.array([
                float(self.lineEdit_39.text()),
                float(self.lineEdit_40.text()),
                float(self.lineEdit_42.text())
            ])
            y = np.array([
                float(self.lineEdit_19.text()),
                float(self.lineEdit_41.text()),
                float(self.lineEdit_37.text())
            ])
            x_val = float(self.lineEdit_43.text())  # F(x) input

            # Compute interpolation
            result = self.lagrange_interpolation(x, y, x_val)
            self.lineEdit_44_answer.setText(f'{result:.4f}')  # Display answer

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Invalid input: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LagrangeInterpolationApp()
    window.show()
    sys.exit(app.exec())
