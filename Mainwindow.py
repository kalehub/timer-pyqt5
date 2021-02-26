import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Mainwindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Mainwindow, self).__init__(*args, **kwargs)
        self.width = 800
        self.height = 300
        self.setWindowTitle('Timer App')
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        # show timer
        self.show_time()

                
    def show_time(self):
        self.tell_time = QLabel('00:00:00',self)
        self.tell_time.setFont(QFont('', 100))
        self.tell_time.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.tell_time)

  
    
    
    












