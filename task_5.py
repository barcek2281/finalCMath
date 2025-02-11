# task_5.py
import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Task5PolynomialFitting(QWidget):
    """
    Task 5: Polynomial Curve Fitting using Least Squares.
    
    This widget allows the user to input x and y data points (comma-separated)
    and fits a quadratic polynomial (ax² + bx + c) to the data using least squares.
    The fitted curve along with the original data points is plotted, and the
    computed coefficients are displayed.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        # Create the main layout.
        self.layout = QVBoxLayout()
        
        # Create input fields for x and y values.
        self.x_label = QLabel("Enter x values (comma-separated):")
        self.x_input = QLineEdit()
        self.x_input.setPlaceholderText("e.g., 0, 1, 2, 3, 4")
        
        self.y_label = QLabel("Enter y values (comma-separated):")
        self.y_input = QLineEdit()
        self.y_input.setPlaceholderText("e.g., 0, 1, 4, 9, 16")
        
        # Button to trigger the fitting.
        self.fit_button = QPushButton("Fit Quadratic Curve")
        self.fit_button.clicked.connect(self.fit_curve)
        
        # Label to display the fitted coefficients.
        self.coeff_label = QLabel("Coefficients: ")
        
        # Create a matplotlib canvas for plotting.
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        
        # Add all widgets to the layout.
        self.layout.addWidget(self.x_label)
        self.layout.addWidget(self.x_input)
        self.layout.addWidget(self.y_label)
        self.layout.addWidget(self.y_input)
        self.layout.addWidget(self.fit_button)
        self.layout.addWidget(self.coeff_label)
        self.layout.addWidget(self.canvas)
        
        self.setLayout(self.layout)
        self.setWindowTitle("Task 5: Polynomial Curve Fitting")
        
    def fit_curve(self):
        """
        Reads user input, fits a quadratic polynomial using least squares,
        displays the coefficients, and plots the fitted curve along with the
        data points.
        """
        # Get input values.
        x_text = self.x_input.text().strip()
        y_text = self.y_input.text().strip()
        
        try:
            # Use default values if no input is provided.
            if not x_text:
                x_vals = np.array([0, 1, 2, 3, 4], dtype=float)
            else:
                x_vals = np.array([float(val) for val in x_text.split(",")])
            
            if not y_text:
                y_vals = np.array([0, 1, 4, 9, 16], dtype=float)
            else:
                y_vals = np.array([float(val) for val in y_text.split(",")])
            
            # Check that number of x and y values match.
            if len(x_vals) != len(y_vals):
                self.coeff_label.setText("Error: Number of x and y values must match.")
                return
            
            # Fit a quadratic polynomial.
            coeffs = np.polyfit(x_vals, y_vals, 2)  # Coefficients: [a, b, c]
            poly = np.poly1d(coeffs)
            
            # Display the coefficients.
            self.coeff_label.setText(
                f"Fitted Coefficients: a = {coeffs[0]:.4f}, b = {coeffs[1]:.4f}, c = {coeffs[2]:.4f}"
            )
            
            # Generate smooth x values for plotting.
            x_smooth = np.linspace(min(x_vals), max(x_vals), 200)
            y_smooth = poly(x_smooth)
            
            # Plot the data points and fitted curve.
            self.ax.clear()
            self.ax.scatter(x_vals, y_vals, color='red', label='Data Points')
            self.ax.plot(x_smooth, y_smooth, color='blue', label='Fitted Quadratic Curve')
            self.ax.set_title("Polynomial Curve Fitting (Quadratic)")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.legend()
            self.ax.grid(True)
            
            self.canvas.draw()
        except Exception as e:
            self.coeff_label.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task5PolynomialFitting()
    window.show()
    sys.exit(app.exec())
