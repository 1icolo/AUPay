from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login
from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow
from fnHelper.aupCard import AUPCard
import sys, os
from fnHelper import hashEncryption
from fnHelper.login import login

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
        login(self, mode)
