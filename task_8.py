# task_8.py
import sys
import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication

class Task8RK2(QWidget):
    """
    Task 8: Runge-Kutta 2nd Order.
    
    This widget applies the Runge-Kutta second-order method to solve the IVP:
    
        dy/dx = e^x - y,    y(0) = 0
    
    The solution is computed up to x = 0.2 using a step size of h = 0.1.
    Intermediate results are displayed to show the progress of the calculation.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.layout = QVBoxLayout()
        
        self.compute_button = QPushButton("Compute RK2")
        self.compute_button.clicked.connect(self.compute_rk2)
        
        self.result_label = QLabel("Results will be displayed here.")
        self.result_label.setStyleSheet("font-family: monospace;")
        
        self.layout.addWidget(self.compute_button)
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)
        self.setWindowTitle("Task 8: Runge-Kutta 2nd Order")
    
    def f(self, x, y):
        return np.exp(x) - y
    
    def compute_rk2(self):
        h = 0.1
        x0 = 0.0
        y0 = 0.0
        x_target = 0.2
        
        results = []
        x = x0
        y = y0
        results.append(f"x = {x:.1f}, y = {y:.6f}")
        
        # Perform steps until we reach x_target.
        while x < x_target - 1e-8:
            k1 = self.f(x, y)
            k2 = self.f(x + h/2, y + (h/2)*k1)
            y = y + h * k2
            x = x + h
            results.append(f"x = {x:.1f}, y = {y:.6f}")
        
        result_str = "\n".join(results)
        self.result_label.setText(result_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task8RK2()
    window.show()
    sys.exit(app.exec())
