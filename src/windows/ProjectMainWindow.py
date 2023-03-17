from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login, logout
from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow
from fnHelper.aupCard import AUPCard
                

class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionLogout.triggered.connect(lambda: self.logoutAttempt())
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt())
        self.lineSchoolId_login.returnPressed.connect(self.loginAttempt)
        self.linePassword_login.returnPressed.connect(self.loginAttempt)
        self.buttonRFIDLogin_login.clicked.connect(lambda: self.loginRFID())


    def logoutAttempt(self):
        logout.Logout(self)

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
                UserWindow(self)
            case 'business':
                self.stackedWidget.setCurrentIndex(2)
                from windows.BusinessWindow import BusinessWindow
                BusinessWindow(self)
            case 'teller':
                self.stackedWidget.setCurrentIndex(3)
                from windows.TellerWindow import TellerWindow
                TellerWindow(self)

    def loginRFID(self):
        try:
            user = login.login_rfid(AUPCard(5).get_uid())  
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
                    UserWindow(self)
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