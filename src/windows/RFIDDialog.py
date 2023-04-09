from PyQt5.QtWidgets import QDialog
from windows.ui.ui_RFIDDialog import Ui_RFIDDialog
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
from PyQt5.QtCore import QTimer, Qt


class RFIDDialog(QDialog):
    def __init__(self, timeout:int = 1, parent=None):
        print(__name__)
        super(RFIDDialog, self).__init__(parent)
        self.rfidDialog()
        QTimer.singleShot(timeout*1000, self.close)

    def rfidDialog(self):
        self.ui = Ui_RFIDDialog()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)