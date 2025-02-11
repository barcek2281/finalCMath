import numpy as np
from PyQt6.QtWidgets import QWidget


class Task3(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def solve_system(self, A, B):
        """Solves Ax = B using Gaussian elimination with partial pivoting."""
        A = np.array(A, dtype=float)
        B = np.array(B, dtype=float)
        n = len(B)

        # Forward elimination with partial pivoting
        for i in range(n):
            max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
            if i != max_row:
                A[[i, max_row]] = A[[max_row, i]]
                B[[i, max_row]] = B[[max_row, i]]

            for j in range(i + 1, n):
                factor = A[j][i] / A[i][i]
                A[j] -= factor * A[i]
                B[j] -= factor * B[i]

        # Back substitution
        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (B[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i][i]

        return x

    def compute_solution(self, window):
        try:
            A = [
                [float(window.lineEdit_6.text()), float(window.lineEdit_4.text()), float(window.lineEdit_8.text())],
                [float(window.lineEdit_10.text()), float(window.lineEdit_7.text()), float(window.lineEdit_2.text())],
                [float(window.lineEdit_9.text()), float(window.lineEdit_5.text()), float(window.lineEdit_3.text())]
            ]
            B = [
                float(window.lineEdit_11.text()),
                float(window.lineEdit_13.text()),
                float(window.lineEdit_12.text())
            ]

            solution = self.solve_system(A, B)
            window.lineEdit_14_answer.setText(f"x={solution[0]:.2f}, y={solution[1]:.2f}, z={solution[2]:.2f}")
        except Exception as e:
            window.lineEdit_14_answer.setText("Error: Invalid input or no solution.")