from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from database import Database
from login_ui import Ui_LoginMainWindow
from user_ui import Ui_UserMainWindow
from teller_ui import Ui_TellerMainWindow
from admin_ui import Ui_AdminMainWindow
from business_ui import Ui_BusinessMainWindow


class LoginWindow(QMainWindow, Ui_LoginMainWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)

        self.setupUi(self)
        self.loginButton.clicked.connect(lambda: self.loginAttempt())

    def determineUserType(self, user):
            match user:
                case "user":
                    self.close()
                    self.openWindow(user)
                case "admin":
                    self.close()
                    self.openWindow(user)
                case "business":
                    self.close()
                    self.openWindow(user)
                case "teller":
                    self.close()
                    self.openWindow(user)
    def openWindow(self, userType):
        self.window = QMainWindow()
        match userType:
            case "user":
                self.ui = Ui_UserMainWindow()
            case "admin":
                self.ui = Ui_AdminMainWindow()
            case "business":
                self.ui = Ui_BusinessMainWindow()
            case "teller":
                self.ui = Ui_TellerMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def loginAttempt(self):
        user = Database().find_user(self.idLine.text(), self.passwordLine.text())
        self.determineUserType(user)
    
app = QApplication([])
window = LoginWindow()
window.show()
app.exec()
