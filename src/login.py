from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from login_ui import Ui_Dialog


class MainWindow(QDialog, Ui_Dialog):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.loginButton.clicked.connect(lambda: self.loginAttempt())

    def loginAttempt(self):
        print(self.passwordLine.text())
        



app = QApplication([])
window = MainWindow()
window.show()
app.exec()