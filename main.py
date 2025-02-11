import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from task_5 import PolynomialCurveFitting
from task_6 import LagrangeInterpolation
from task_7 import RombergIntegration
from task_8 import RungeKuttaSecondOrder

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)
        self.task5 = PolynomialCurveFitting(self)
        self.task6 = LagrangeInterpolation(self)
        self.task7 = RombergIntegration(self)
        self.task8 = RungeKuttaSecondOrder(self)
        
        self.tab1_verticalLayout.addWidget(self.task5)
        self.tab2_verticalLayout.addWidget(self.task6)
        self.tab3_verticalLayout.addWidget(self.task7)
        self.tab4_verticalLayout.addWidget(self.task8)
        
        self.tab1_toolButton.clicked.connect(self.do_task5)
        self.tab2_toolButton.clicked.connect(self.do_task6)
        self.tab3_toolButton.clicked.connect(self.do_task7)
        self.tab4_toolButton.clicked.connect(self.do_task8)
    
    def do_task5(self):
        try:
            x_values = list(map(float, self.tab1_lineEdit.text().split()))
            self.task5.plot_curve(x_values)
        except Exception as e:
            print(e)
            self.tab1_label2.setText("Error in input values")
    
    def do_task6(self):
        try:
            x_values = list(map(float, self.tab2_x_lineEdit.text().split()))
            y_values = list(map(float, self.tab2_y_lineEdit.text().split()))
            x_target = float(self.tab2_target_lineEdit.text())
            result = self.task6.lagrange(x_values, y_values, x_target)
            self.tab2_label2.setText(f"Interpolated Value: {result}")
            self.task6.plot_interpolation(x_values, y_values, x_target)
        except Exception as e:
            print(e)
            self.tab2_label2.setText("Error in input values")
    
    def do_task7(self):
        try:
            self.task7.plot_integration()
        except Exception as e:
            print(e)
            self.tab3_label2.setText("Error in computation")
    
    def do_task8(self):
        try:
            self.task8.plot_rk2()
        except Exception as e:
            print(e)
            self.tab4_label2.setText("Error in computation")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
