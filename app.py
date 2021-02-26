import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Mainwindow import *


# creating an instance(QApplication instance)
app = QApplication(sys.argv)
# sys.argv enables command line syntax in QApplication
# if no command line, then replace it by QApplication([])

# making a window 
window = Mainwindow()
window.show()



app.exec_()







