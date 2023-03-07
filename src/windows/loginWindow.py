from PyQt5.QtWidgets import *
from dbHelper import find_user
from fnHelper import login
from windows.ui.loginWindow_ui import Ui_LoginWindow
from windows.adminWindow import AdminWindow
from windows.userWindow import UserWindow
from windows.businessWIndow import BusinessWindow
from windows.tellerWIndow import TellerWIndow


class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.loginButton.clicked.connect(lambda: self.loginAttempt())


    def loginAttempt(self):
        user = login.login_attempt(self.idLine.text(), self.passwordLine.text())
        self.close()
        self.window = QMainWindow()
        match user['user_type']:
            case "user":
                self.ui = UserWindow()
            case "admin":
                self.ui = AdminWindow()
            case "business":
                self.ui = BusinessWindow()
            case "teller":
                self.ui = TellerWIndow()
        self.ui.setupUi(self.window)
        self.window.show()
