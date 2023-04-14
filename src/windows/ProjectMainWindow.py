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
        self.LoginWindow()
        self.loginAttempt('rfid')
        self.actionLogout.triggered.connect(lambda: self.logoutAttempt())
        self.actionExit.triggered.connect(lambda: QApplication.quit())
        self.actionFullscreen.triggered.connect(lambda: self.toggleFullscreen())
        self.buttonLogin_login.clicked.connect(lambda: self.loginAttempt('password'))
        self.buttonRFIDLogin_login.clicked.connect(lambda: self.loginAttempt('rfid'))
        self.actionFullscreen.setChecked(False)

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

    def LoginWindow(self):
        scene = QGraphicsScene()
        self.graphicsView_login.setScene(scene)
        backgroundPixmap  = QPixmap("src/resources/login-wallpaper.jpg")
        backgroundItem = QGraphicsPixmapItem(backgroundPixmap)
        self.graphicsView_login.scene().addItem(backgroundItem)
        backgroundItem.setZValue(-1)