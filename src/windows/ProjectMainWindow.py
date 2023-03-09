from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper import find_all_users
from bson import ObjectId

from fnHelper import login, logout
from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow


class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt())
        self.actionLogout.triggered.connect(lambda: self.logout())

    def loginAttempt(self):
        # print("hello world")
        user = login.login_attempt(self.lineSchoolId_login.text(), self.linePassword_login.text())
        try:
            match user['user_type']:
                case "user":
                    self.stackedWidget.setCurrentIndex(1)
                case "business":
                    self.stackedWidget.setCurrentIndex(2)
                case "teller":
                    self.stackedWidget.setCurrentIndex(3)
                case "admin":
                    self.stackedWidget.setCurrentIndex(4)
        except TypeError as e:
            print("")



    def logout(self):
        logout.Logout(self)

class AdministratorWindow(ProjectMainWindow):
    def __init__(self, parent=ProjectMainWindow):
        super(ProjectMainWindow).__init__(parent)
        self.buttonAddUser_administrator.clicked.connect(lambda: self.bro())
        
    def bro(self):
        print("bro")
