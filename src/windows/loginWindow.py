from PyQt5.QtWidgets import *
from dbHelper import find_user
from windows.ui.loginWindow_ui import Ui_LoginWindow
from windows.ui.userWindow_ui import Ui_UserWindow
from windows.ui.tellerWindow_ui import Ui_TellerWindow
from windows.ui.adminWindow_ui import Ui_AdminWindow
from windows.ui.businessWindow_ui import Ui_BusinessWindow

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        print(find_user("",""))
        self.setupUi(self)
        self.loginButton.clicked.connect(lambda: self.loginAttempt())

    def determineUserType(self, user):
        self.close()
        self.openWindow(user)

        
    def openWindow(self, userType):
        self.window = QMainWindow()
        match userType:
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


    def loginAttempt(self):
        user = find_user(self.idLine.text(), self.passwordLine.text())
        self.determineUserType(user)

