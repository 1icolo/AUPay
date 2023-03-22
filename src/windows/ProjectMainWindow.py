from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login
from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow
from fnHelper.aupCard import AUPCard
import sys, os

class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loginRFID(1)
        self.actionLogout.triggered.connect(lambda: self.logoutAttempt())
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt())
        self.buttonRFIDLogin_login.clicked.connect(lambda: self.loginRFID())
        
    def logoutAttempt(self):
        QApplication.quit()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def loginAttempt(self):
        user = login.login_attempt(self.lineSchoolId_login.text(), self.linePassword_login.text())
        # if user doesn't match anything
        if user is None:
            return
        match user['user_type']:
            case 'admin':
                self.stackedWidget.setCurrentIndex(4)
                from windows.AdminWindow import AdminWindow
                AdminWindow(self)
            case 'user':
                self.stackedWidget.setCurrentIndex(1)
                from windows.UserWindow import UserWindow
                UserWindow(self, user)
            case 'business':
                self.stackedWidget.setCurrentIndex(2)
                from windows.BusinessWindow import BusinessWindow
                BusinessWindow(self)
            case 'teller':
                self.stackedWidget.setCurrentIndex(3)
                from windows.TellerWindow import TellerWindow
                TellerWindow(self)

    def loginRFID(self, seconds = 5):
        try:
            user = login.login_rfid(AUPCard(seconds).get_uid())  
            if user is None:
                return
            match user['user_type']:
                case 'admin':
                    self.stackedWidget.setCurrentIndex(4)
                    from windows.AdminWindow import AdminWindow
                    AdminWindow(self)
                case 'user':
                    self.stackedWidget.setCurrentIndex(1)
                    from windows.UserWindow import UserWindow
                    UserWindow(self, user)
                case 'business':
                    self.stackedWidget.setCurrentIndex(2)
                    from windows.BusinessWindow import BusinessWindow
                    BusinessWindow(self)
                case 'teller':
                    self.stackedWidget.setCurrentIndex(3)
                    from windows.TellerWindow import TellerWindow
                    TellerWindow(self)
        except:
            pass