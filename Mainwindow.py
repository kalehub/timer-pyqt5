import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import time


class Mainwindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Mainwindow, self).__init__(*args, **kwargs)
        self.width = 800
        self.height = 300
        self.setWindowTitle('Timer App - otw move on')
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)

        # show timer
        self.show_time()

        # buttons
        start_button = QPushButton('start', self)
        start_button.move(250,200) 
        start_button.clicked.connect(self.start_timer)

        stop_button = QPushButton('stop', self)
        stop_button.move(450,200)
        stop_button.clicked.connect(self.stop_timer)

                
    def show_time(self):
        self.tell_time = QLabel('00:00:00',self)
        self.tell_time.setFont(QFont('', 100))
        self.tell_time.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.tell_time)

    def start_timer(self):
        print('started')


    def stop_timer(self):
        print('stopped')
    
    
    












