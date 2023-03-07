from PyQt5.QtWidgets import *
from windows.ui.userWindow_ui import Ui_UserWindow


class UserWindow(QMainWindow, Ui_UserWindow):
    def __init__(self, parent = None):
        super(UserWindow, self).__init__(parent)
        self.setupUi(self)
