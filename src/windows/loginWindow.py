from PyQt5.QtWidgets import *
from dbHelper import find_user
from fnHelper import login
from windows.ui.loginWindow_ui import Ui_LoginWindow
from windows.ui.userWindow_ui import Ui_UserWindow
from windows.ui.tellerWindow_ui import Ui_TellerWindow
from windows.ui.adminWindow_ui import Ui_AdminWindow
from windows.ui.businessWindow_ui import Ui_BusinessWindow

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
                self.ui = Ui_UserWindow()
            case "admin":
                self.ui = Ui_AdminWindow()
            case "business":
                self.ui = Ui_BusinessWindow()
            case "teller":
                self.ui = Ui_TellerWindow()
        self.ui.setupUi(self.window)
        self.window.show()
