from PyQt5.QtWidgets import *
from windows.ui.tellerWindow_ui import Ui_TellerWindow


class TellerWIndow(QMainWindow, Ui_TellerWindow):
    def __init__(self, parent = None):
        super(TellerWIndow, self).__init__(parent)
        self.setupUi(self)
