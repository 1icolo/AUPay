from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from login_ui import Ui_MainWindow
from database import Database


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.loginButton.clicked.connect(lambda: self.loginAttempt())

    def loginAttempt(self): 
        Database().findUser(self.idLine.text(), self.passwordLine.text())


app = QApplication([])
window = MainWindow()
window.show()
app.exec()