from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from database import Database
from login_ui import Ui_LoginMainWindow

class LoginWindow(QMainWindow, Ui_LoginMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)

        self.setupUi(self)
        self.loginButton.clicked.connect(lambda: self.loginAttempt())
    def determineUserType(self, user):
            match user:
                case "user":
                    print("user")
                case "admin":
                    print("admin")
                case "business":
                    print("business")
                case "teller":
                    print("teller")
    def loginAttempt(self):
        user = Database().find_user(self.idLine.text(), self.passwordLine.text())
        self.determineUserType(user)
    
app = QApplication([])
window = LoginWindow()
window.show()
app.exec()
