import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from task_1 import Task1

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi("untitled.ui", self)
        self.task1 = Task1(self)
        self.tab1_verticalLayout.addWidget(self.task1)

        self.tab1_toolButton.clicked.connect(self.do_task1)

    def do_task1(self):
        try:
            x_range = tuple(map(int, self.tab1_lineEdit.text().split()))
            self.task1.plot_graph(x_range)
            roots, closest_root, absolute_error = self.task1.calc_root(x_range)
            self.tab1_label2.setText(f"root: {roots[0]}, closest_root: {closest_root}, absolute_error: {absolute_error}")
        except Exception as e:
            print(e)
            self.tab1_label2.setText("error with values or no roots")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
