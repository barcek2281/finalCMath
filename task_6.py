# task_6.py
import sys
import numpy as np
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication

class Task6LagrangeInterpolation(QWidget):
    """
    Task 6: Lagrange’s Interpolation Formula.
    
    This widget allows the user to input x and y data points (comma-separated)
    and an interpolation value. It computes and displays the estimated function
    value at the given x using Lagrange's interpolation formula.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        # Create the main layout.
        self.layout = QVBoxLayout()
        
        # Input fields for x and y values.
        self.x_label = QLabel("Enter x values (comma-separated):")
        self.x_input = QLineEdit()
        self.x_input.setPlaceholderText("e.g., 1, 3, 5")
        
        self.y_label = QLabel("Enter y values (comma-separated):")
        self.y_input = QLineEdit()
        self.y_input.setPlaceholderText("e.g., 2, 8, 18")
        
        # Input field for the interpolation point.
        self.x_interp_label = QLabel("Enter x value to interpolate:")
        self.x_interp_input = QLineEdit()
        self.x_interp_input.setPlaceholderText("e.g., 4")
        
        # Button to perform interpolation.
        self.interp_button = QPushButton("Interpolate")
        self.interp_button.clicked.connect(self.perform_interpolation)
        
        # Label to display the result.
        self.result_label = QLabel("Interpolated value: ")
        
        # Add widgets to the layout.
        self.layout.addWidget(self.x_label)
        self.layout.addWidget(self.x_input)
        self.layout.addWidget(self.y_label)
        self.layout.addWidget(self.y_input)
        self.layout.addWidget(self.x_interp_label)
        self.layout.addWidget(self.x_interp_input)
        self.layout.addWidget(self.interp_button)
        self.layout.addWidget(self.result_label)
        
        self.setLayout(self.layout)
        self.setWindowTitle("Task 6: Lagrange Interpolation")
        
    def perform_interpolation(self):
        """
        Reads the input values, performs Lagrange interpolation, and displays
        the interpolated value.
        """
        x_text = self.x_input.text().strip()
        y_text = self.y_input.text().strip()
        x_interp_text = self.x_interp_input.text().strip()
        
        try:
            # Use default values if input fields are empty.
            if not x_text:
                x_vals = np.array([1, 3, 5], dtype=float)
            else:
                x_vals = np.array([float(val) for val in x_text.split(",")])
            
            if not y_text:
                y_vals = np.array([2, 8, 18], dtype=float)
            else:
                y_vals = np.array([float(val) for val in y_text.split(",")])
            
            # Ensure the number of x and y values match.
            if len(x_vals) != len(y_vals):
                self.result_label.setText("Error: Number of x and y values must match.")
                return
            
            # Determine the interpolation point.
            if not x_interp_text:
                x_interp = 4.0
            else:
                x_interp = float(x_interp_text)
                
            # Compute the interpolated value using Lagrange's formula.
            result = self.lagrange_interpolation(x_vals, y_vals, x_interp)
            self.result_label.setText(f"Interpolated value at x = {x_interp}: {result:.4f}")
            
        except Exception as e:
            self.result_label.setText(f"Error: {str(e)}")
    
    def lagrange_interpolation(self, x, y, x_interp):
        """
        Compute the Lagrange interpolation for the given x value.
        
        Parameters:
            x (array-like): Array of x data points.
            y (array-like): Array of y data points.
            x_interp (float): The x value for interpolation.
        
        Returns:
            float: The interpolated value at x_interp.
        """
        n = len(x)
        total = 0.0
        for i in range(n):
            term = y[i]
            for j in range(n):
                if i != j:
                    term *= (x_interp - x[j]) / (x[i] - x[j])
            total += term
        return total

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task6LagrangeInterpolation()
    window.show()
    sys.exit(app.exec())
