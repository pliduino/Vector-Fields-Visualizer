import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from plotting import plotter


import os
import sys


FILE_PATH = os.path.dirname(os.path.abspath(__file__))

class MyApp(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

""" class Window(QWidget):
    def __init__(self, title='PyQt6 Window'):
        super().__init__()

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(FILE_PATH + '/testicon.ico'))

        self.setFixedSize(500, 300)

        self.create_widgets()

    def create_widgets(self):
        grid = QGridLayout()

        btn = QPushButton('Click me')
        btn.clicked.connect(self.clicked_btn)
        grid.addWidget(btn, 1, 0)
        grid.addWidget(btn, 1, 1)
        
        self.label = QLabel('Align this shit')
        self.label.move(250, 0)
        self.label.setFont(QFont('Times New Roman', 15))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.label, 0, 0)

        self.setLayout(grid)
    
    def clicked_btn(self):
        self.label.setText("Text is changed") """


class LoadUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_PATH + '/TestWindow.ui', self) 
        self.grid = False
        self.range = 10
        self.step = 1
        self.arrow_norm_fac = 0.25
        

    def plot_values(self):
        self.plot_new = plotter.PlotClass(range=self.range, step=self.step, arrow_norm_fac=self.arrow_norm_fac, grid=self.grid)
        if self.plot_new.plot(self.x, self.y) == 0:
            self.plot_new.show()
        else:
            self.plot_new.close()

    def set_x(self, string):
        self.x = str(string)
    
    def set_y(self, string):
        self.y = str(string)

    def set_grid(self, state):
        self.grid = False if state == 0 else True
        print(self.grid)

    def set_range(self, value):
        self.range = value

    def set_normalization(self, value):
        self.arrow_norm_fac = 1/value

    def set_step(self, value):
        self.step = value
""" 
if __name__ == '__main__':
    app = MyApp()
    #window = Window('Program Name')
    window = LoadUI()
    window.show()
    sys.exit(app.exec())
 """