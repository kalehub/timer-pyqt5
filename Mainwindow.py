import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import time


class Mainwindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Mainwindow, self).__init__(*args, **kwargs)
        self.req_time = int(input('Set timer to : '))
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
        mins, secs = divmod(self.req_time,60)
        hrs, mins = divmod(mins, 60)
        self.time_left  = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        self.tell_time = QLabel(self.time_left,self)
        self.tell_time.setFont(QFont('', 100))
        self.tell_time.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.tell_time)

    def start_timer(self):
        print(self.req_time)
        while self.req_time:
            mins, secs = divmod(self.req_time,60)
            hrs, mins = divmod(mins, 60)
            self.time_left  = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
            print(self.time_left, end='\r')
            #self.tell_time.setText(self.time_left)
            time.sleep(1)
            self.req_time -= 1

        print('time is up')

    def stop_timer(self):
        print('stopped')
        self.tell_time.setText(self.time_left)


    
    
    












