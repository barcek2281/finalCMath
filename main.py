import sys
import numpy as np
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from task_1 import Task1
from task_2 import Task2
from task_3 import Task3
from task_4 import Task4  # Import Task4


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi("untitled.ui", self)

        # Initialize Task1
        self.task1 = Task1(self)
        self.tab1_verticalLayout.addWidget(self.task1)
        self.tab1_toolButton.clicked.connect(self.do_task1)

        # Initialize Task2
        self.task2 = Task2(self)
        self.tab2_verticalLayout.addWidget(self.task2)
        self.pushButton_2.clicked.connect(self.do_task2)

        # Initialize Task3
        self.task3 = Task3(self)
        self.pushButton.clicked.connect(self.do_task3)

        # Initialize Task4
        self.task4 = Task4(self)

    def do_task1(self):
        try:
            x_range = tuple(map(int, self.tab1_lineEdit.text().split()))
            self.task1.plot_graph(x_range)
            roots, closest_root, absolute_error = self.task1.calc_root(x_range)
            self.tab1_label2.setText(
                f"root: {roots[0]}, closest_root: {closest_root}, absolute_error: {absolute_error}")
        except Exception as e:
            print(e)
            self.tab1_label2.setText("Error with values or no roots")

    def do_task2(self):
        try:
            a, b = map(float, self.lineEdit_answer.text().split())
            self.task2.plot_graph((a, b))
            root_fp, iter_fp = self.task2.false_position(a, b)
            root_bi, iter_bi = self.task2.bisection(a, b)
            self.label_2.setText(f"False Position: root={root_fp}, iterations={iter_fp}\n"
                                 f"Bisection: root={root_bi}, iterations={iter_bi}")
        except Exception as e:
            print(e)
            self.label_2.setText("Error with values")

    def do_task3(self):
        try:
            coefficients = [
                list(map(float, self.coeff_1.text().split())),
                list(map(float, self.coeff_2.text().split())),
                list(map(float, self.coeff_3.text().split()))
            ]
            results = list(map(float, self.results.text().split()))
            solution = self.task3.solve(coefficients, results)
            self.label_3.setText(f"Solution: {solution}")
        except Exception as e:
            print(e)
            self.label_3.setText("Error with input values")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
