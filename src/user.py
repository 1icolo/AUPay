from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from user_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.buttonLogout.clicked.connect(lambda: print("Logout"))



app = QApplication([])
window = MainWindow()
window.show()
app.exec()