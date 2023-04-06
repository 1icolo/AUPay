from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login
from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow
from fnHelper.aupCard import AUPCard
import sys, os
from fnHelper import hashEncryption

class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loginAttempt('rfid')
        self.actionLogout.triggered.connect(lambda: self.logoutAttempt())
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt('password'))
        self.buttonRFIDLogin_login.clicked.connect(lambda: self.loginAttempt('rfid'))
        
    def logoutAttempt(self):
        QApplication.quit()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def loginAttempt(self, mode):
        try: 
            user = None
            match mode:
                case 'password': user = login.login_attempt(self.lineSchoolId_login.text(), hashEncryption.encrypt(self.linePassword_login.text()))
                case 'rfid': user = login.login_rfid(hashEncryption.encrypt(AUPCard(0.001).get_uid())) 

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
                    BusinessWindow(self, user)
                case 'teller':
                    self.stackedWidget.setCurrentIndex(3)
                    from windows.TellerWindow import TellerWindow
                    TellerWindow(self, user)
        except Exception:
            print('No RFID detected.')
