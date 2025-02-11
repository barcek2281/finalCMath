# task_5.py
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PolynomialCurveFitting(QWidget):
    """
    Task 5: Polynomial Curve Fitting using Least Squares.
    
    This widget allows the user to input data points and fits a quadratic polynomial
    to them using the least squares method. The fitted curve is then plotted.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
        
    def init_ui(self):
        # Set up layout and plot canvas.
        self.layout = QVBoxLayout()
        self.instruction_label = QLabel("Data is taken from input in main window.")
        self.layout.addWidget(self.instruction_label)
        
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        self.setLayout(self.layout)
        self.setWindowTitle("Task 5: Polynomial Curve Fitting")
        
    def plot_curve(self, x_values):
        """
        Plot a quadratic curve using the given x_values.
        For demonstration, we assume y = x^2.
        In your project, you might want to use both x and y inputs.
        """
        try:
            x_vals = np.array(x_values, dtype=float)
            # For demonstration, use a quadratic relationship: y = x^2.
            y_vals = x_vals**2
            
            # Fit a quadratic polynomial.
            coeffs = np.polyfit(x_vals, y_vals, 2)  # coeffs: [a, b, c]
            poly = np.poly1d(coeffs)
            
            # Create a smooth curve.
            x_smooth = np.linspace(min(x_vals), max(x_vals), 200)
            y_smooth = poly(x_smooth)
            
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
            print("Error in plot_curve:", e)
