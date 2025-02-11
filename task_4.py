import numpy as np
from PyQt6.QtWidgets import QWidget, QPushButton, QTextEdit, QLineEdit


class Task4(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Access UI elements from main window
        self.matrix_inputs = [
            [self.parent().lineEdit_22, self.parent().lineEdit_17, self.parent().lineEdit_23],
            [self.parent().lineEdit_21, self.parent().lineEdit_24, self.parent().lineEdit_20],
            [self.parent().lineEdit_26, self.parent().lineEdit_25, self.parent().lineEdit_15]
        ]
        self.solve_button = self.parent().pushButton_3
        self.result_output = self.parent().textEdit_answer

        self.solve_button.clicked.connect(self.compute_inverse)

    def compute_inverse(self):
        try:
            matrix = np.array([
                [float(self.matrix_inputs[i][j].text()) for j in range(3)] for i in range(3)
            ])

            inverse_matrix = np.linalg.inv(matrix)

            result_text = "\n".join(["\t".join(map(lambda x: f"{x:.4f}", row)) for row in inverse_matrix])
            self.result_output.setText(f"Inverse Matrix:\n{result_text}")

        except Exception as e:
            self.result_output.setText(f"Error: {e}")
