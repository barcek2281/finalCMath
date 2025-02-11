# task_7.py
import sys
import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication

class Task7RombergIntegration(QWidget):
    """
    Task 7: Romberg’s Integration.
    
    This widget applies Romberg’s Integration to approximate the integral of 
    f(x) = x² over the interval [0,1]. It uses step sizes corresponding to 
    h = 0.5, 0.25, and 0.125 (i.e. 2, 4, and 8 subintervals) to demonstrate 
    convergence. The complete Romberg table is computed and displayed.
    
    The exact value of the integral is 1/3 ≈ 0.333333.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.layout = QVBoxLayout()
        
        self.compute_button = QPushButton("Compute Romberg Integration")
        self.compute_button.clicked.connect(self.compute_romberg)
        
        self.result_label = QLabel("Romberg Table will appear here.")
        self.result_label.setStyleSheet("font-family: monospace;")
        
        self.layout.addWidget(self.compute_button)
        self.layout.addWidget(self.result_label)
        self.setLayout(self.layout)
        self.setWindowTitle("Task 7: Romberg Integration")
        
    def f(self, x):
        return x**2
        
    def compute_romberg(self):
        a = 0.0
        b = 1.0
        # We want to use h values of 0.5, 0.25, and 0.125. Notice that:
        # h = (b - a) / 2^i, so for h=0.5: i=1, for h=0.25: i=2, for h=0.125: i=3.
        # We'll compute for n_levels = 4 (i = 0,1,2,3).
        n_levels = 4
        R = np.zeros((n_levels, n_levels))
        
        # R[0,0]: trapezoidal rule with one subinterval (h = 1.0)
        h = b - a
        R[0, 0] = 0.5 * h * (self.f(a) + self.f(b))
        
        # Fill the Romberg table.
        for i in range(1, n_levels):
            h = (b - a) / (2**i)
            sum_val = 0
            # Sum the new evaluation points.
            for k in range(1, 2**(i-1) + 1):
                x = a + (2*k - 1) * h
                sum_val += self.f(x)
            R[i, 0] = 0.5 * R[i-1, 0] + h * sum_val
            for j in range(1, i+1):
                R[i, j] = R[i, j-1] + (R[i, j-1] - R[i-1, j-1]) / (4**j - 1)
        
        # Build a formatted string for the Romberg table.
        table_str = ""
        for i in range(n_levels):
            for j in range(i+1):
                table_str += f"{R[i,j]:.6f}\t"
            table_str += "\n"
        table_str += "\nExact value: 1/3 ≈ 0.333333"
        
        self.result_label.setText(table_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task7RombergIntegration()
    window.show()
    sys.exit(app.exec())
