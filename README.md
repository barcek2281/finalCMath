# Computational Mathematics PyQt Application

## Overview
This application is developed using Python and PyQt to provide an interactive interface for solving various computational mathematics problems. The application supports seven different variants, each containing different mathematical tasks such as root-finding, matrix operations, curve fitting, numerical differentiation, and integration.

## Features
- **Dynamic Method Selection:** Users can choose between different computational methods using dropdown menus or radio buttons.
- **User Input Options:**
  - Coefficients for equations
  - Matrix values
  - Intervals and initial guesses
  - Subinterval values for integration
  - Additional parameters (e.g., accuracy, relaxation factors)
- **Execution and Visualization:**
  - Execute calculations with a single click
  - Display results in a designated area
  - Generate and plot graphs or tables for numerical solutions

## Installation
### Prerequisites
Ensure you have Python installed (preferably Python 3.7+). The following dependencies are required:
```bash
pip install -r requirements.txt
```

### Running the Application
To launch the application, navigate to the project directory and execute:
```bash
python main.py
```

## Usage
1. Launch the application.
2. Select the desired computational method from the provided options.
3. Enter the required input values in the designated fields.
4. Click the **Answer** button to run the calculation.
5. View the output, which may include numerical results, tables, or graphs.

## Tasks Overview (By Variant)
The application supports the following tasks across different variants:

### Variant 1:
- Graphical Method and Absolute Error
- Root-Finding (Bisection, Secant Methods)
- Jacobi Method
- Iterative Matrix Inversion
- Linear Curve Fitting
- Newton’s Forward Interpolation
- First Derivative using Newton’s Formula
- Trapezoidal Rule Integration

### Variant 2:
- Graphical Method and Absolute Error
- Root-Finding (Bisection, Secant Methods)
- Gauss-Seidel Method
- LU Factorization
- Polynomial Curve Fitting
- Lagrange Interpolation
- Second Derivative using Newton’s Formula
- Simpson’s Rule Integration

(And so on for Variants 3-7, covering different numerical methods like Eigenvalue Computation, Relaxation Methods, Runge-Kutta Methods, and more.)


## Contributing
If you wish to contribute, feel free to fork the repository, make modifications, and submit a pull request.

## License
This project is licensed under the MIT License.

