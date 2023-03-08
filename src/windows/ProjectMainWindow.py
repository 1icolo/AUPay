from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper import find_user
from fnHelper import login
from windows.ui.ProjectMainWindow_ui import Ui_ProjectMainWindow


class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt())
        self.addUserButton_administrator.clicked.connect(lambda: print("hello world"))


    def loginAttempt(self):
        print("hello world")
        user = login.login_attempt(self.idLine.text(), self.passwordLine.text())
        self.stackedWidget.setCurrentIndex(2)
