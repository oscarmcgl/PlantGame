#https://www.pythonguis.com/tutorials/pyside6-signals-slots-events/

import retrieve as r
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QRadioButton
import sys
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Plants!')
        
        button1 = QRadioButton('Monstera')
        button1.clicked.connect(lambda: self.button_clicked(0))

        button2 = QPushButton('Snake Plant')
        button2.setCheckable(True)
        button2.clicked.connect(lambda: self.button_clicked(1))

        self.setCentralWidget(button1)
    
    def button_clicked(self, num):
        print('Button clicked!')
        title = r.retrieve_data(num, 'name')
        MainWindow.changeTitle(self, title)
    
    def button_check(self, checked):
        print('Checked:', checked)
    
    def changeTitle(self, title):
        self.setWindowTitle(title)

class InfoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
    
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

info_window = InfoWindow()

app.exec()