from PyQt5.QtWidgets import *
from windows.ui.businessWindow_ui import Ui_BusinessWindow


class BusinessWindow(QMainWindow, Ui_BusinessWindow):
    def __init__(self, parent = None):
        super(BusinessWindow, self).__init__(parent)
        self.setupUi(self)
