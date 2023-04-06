from PyQt5.QtWidgets import QDialog
from windows.ui.ui_RFIDDialog import Ui_RFIDDialog
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString
import time


class RFIDDialog(QDialog):

    def __init__(self, timeout:int = 5, parent=None):
        print(__name__)
        super(RFIDDialog, self).__init__(parent)
        self.ui = Ui_RFIDDialog()
        self.ui.setupUi(self)
        time.sleep(2)
        self.close()
        
    #     try:
    #         # define the card type
    #         cardtype = AnyCardType()

    #         # request a card connection
    #         cardrequest = CardRequest(timeout=timeout, cardType=cardtype)
    #         cardservice = cardrequest.waitforcard()

    #         # connect to the card
    #         cardservice.connection.connect()

    #         # get the UID of the card
    #         GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
    #         self.data, sw1, sw2 = cardservice.connection.transmit(GET_UID)

    #         self.close()
            
    #     except Exception:
    #         self.close()

    # def get_uid(self):
    #     # return the UID in hexadecimal format
    #     self.exec()
    #     uid = toHexString(self.data)
    #     # print(uid)
    #     self.close()
    #     return uid