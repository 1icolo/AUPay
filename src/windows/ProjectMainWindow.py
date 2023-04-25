from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login
from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow
from fnHelper.aupCard import AUPCard
import sys, os
from fnHelper import cryptography
from fnHelper.login import login

class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.loginAttempt('rfid')
        self.stackedWidget.setStyleSheet("QStackedWidget {background-color: white;}")
        self.actionLogout.triggered.connect(lambda: self.logoutAttempt())
        self.actionExit.triggered.connect(lambda: QApplication.quit())
        self.actionFullscreen.triggered.connect(lambda: self.toggleFullscreen())
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt('password'))
        self.buttonRFIDLogin_login.clicked.connect(lambda: self.loginAttempt('rfid'))
        self.actionFullscreen.setChecked(True)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Alt:
            self.menubar = self.findChild(QMenuBar, "menubar")
            if self.menubar:
                self.menubar.setVisible(not self.menubar.isVisible())
        super().keyPressEvent(event)

    def toggleFullscreen(self):
        if self.actionFullscreen.isChecked():
            self.showFullScreen()
        else:
            self.showNormal()
        
    def logoutAttempt(self):
        QApplication.quit()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def loginAttempt(self, mode):
        login(self, mode)
