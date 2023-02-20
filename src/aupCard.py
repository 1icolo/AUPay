from smartcard.CardType import CardType
from smartcard.CardRequest import CardRequest
from smartcard.util import toHexString

class DCCardType(CardType):
    def matches( self, atr, reader=None ):
        return atr[0]==0x3B

cardtype = DCCardType()
cardrequest = CardRequest( timeout=1, cardType=cardtype )
cardservice = cardrequest.waitforcard()

cardservice.connection.connect()
print (toHexString( cardservice.connection.getATR() ))

print (cardservice.connection.getReader())