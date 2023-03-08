from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper import find_all_users
from bson import ObjectId

from fnHelper import login
from windows.ui.ProjectMainWindow_ui import Ui_ProjectMainWindow


class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt())

    def loginAttempt(self):
        print("hello world")
        user = login.login_attempt(self.lineSchoolId_login.text(), self.linePassword_login.text())
        self.stackedWidget.setCurrentIndex(4)


# class AdministratorWindow(ProjectMainWindow):
#     def __init__(self, parent=ProjectMainWindow):
#         super(ProjectMainWindow).__init__(parent)
#         self.buttonAddUser_administrator.clicked.connect(lambda: self.bro())
        
#     def bro(self):
#         print("bro")
