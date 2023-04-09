from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString

class AUPCard:
    def __init__(self, timeout: int = 5):
        print(f"Waiting for smartcard within {timeout} second{(lambda: '', lambda: 's')[timeout != 1]()}.")
        try:
            # define the card type
            cardtype = AnyCardType()

            # request a card connection
            cardrequest = CardRequest(timeout=timeout, cardType=cardtype)
            cardservice = cardrequest.waitforcard()

            # connect to the card
            cardservice.connection.connect()

            # get the UID of the card
            GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
            self.data, sw1, sw2 = cardservice.connection.transmit(GET_UID)
            
        except Exception as e:
            print(e)

    def get_uid(self):
        try:
            # return the UID in hexadecimal format
            uid = toHexString(self.data)
            # print(uid)
            return uid
        except Exception as e:
            print(e)