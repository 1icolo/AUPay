from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login
from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow
import sys, os
from fnHelper.login import login

class ProjectMainWindow(QMainWindow, Ui_ProjectMainWindow):
    def __init__(self, parent=None):
        super(ProjectMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.firstTime = True
        self.loginAttempt('rfid')
        self.stackedWidget.setStyleSheet("QStackedWidget {background-color: white;}")
        self.actionLogout.triggered.connect(lambda: self.logoutAttempt())
        self.actionExit.triggered.connect(lambda: QApplication.quit())
        self.actionFullscreen.triggered.connect(lambda: self.toggleFullscreen())
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt('password'))
        self.buttonRFIDLogin_login.clicked.connect(lambda: self.loginAttempt('rfid'))
        self.actionFullscreen.setChecked(True)
        self.menubar.setVisible(False)
        self.actionHideMenu.triggered.connect(lambda: self.menubar.setVisible(False))
        

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
        if self.firstTime:
            self.firstTime = False
            return
        
        if not login(self, mode):
            QMessageBox.warning(self, "Error", "Login Failed.")

        if mode == "password":
            self.buttonLogin_login.setEnabled(False)
            QTimer.singleShot(5000, lambda: self.buttonLogin_login.setEnabled(True))
        else:
            self.buttonRFIDLogin_login.setEnabled(False)
            QTimer.singleShot(5000, lambda: self.buttonRFIDLogin_login.setEnabled(True))
