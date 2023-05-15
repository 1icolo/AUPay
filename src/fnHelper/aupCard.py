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
            self.cardrequest = CardRequest(timeout=timeout, cardType=cardtype)
            self.cardservice = self.cardrequest.waitforcard()

            # connect to the card
            self.cardservice.connection.connect()
            
        except Exception as e:
            print(e)

    def get_uid(self):
        try:
            # get the UID of the card
            GET_UID = [0xFF, 0xCA, 0x00, 0x00, 0x00]
            self.data, sw1, sw2 = self.cardservice.connection.transmit(GET_UID)

            # return the UID in hexadecimal format
            uid = toHexString(self.data)
            return uid
        
        except Exception as e:
            print(e)

    def write_data(self, data: str):
        try:
            # convert the data to bytes
            data = data.encode('utf-8')
            
            # split the data into 16-byte chunks
            chunks = [data[i:i+16] for i in range(0, len(data), 16)]
            
            # write each chunk to the card
            for i, chunk in enumerate(chunks):
                # pad the chunk with zeros if necessary
                chunk = chunk.ljust(16, b'\x00')
                
                # construct the WRITE command
                WRITE = [0xFF, 0xD6, 0x00, i+4, 0x10] + list(chunk)
                
                # transmit the command to the card
                self.cardservice.connection.transmit(WRITE)
        
        except Exception as e:
            print(e)

    def read_data(self):
        try:
            # initialize an empty list to store the data
            data = []
            
            # read each block of data from the card
            for i in range(4, 64):
                # construct the READ command
                READ = [0xFF, 0xB0, 0x00, i, 0x10]
                
                # transmit the command to the card and append the result to the data list
                result, sw1, sw2 = self.cardservice.connection.transmit(READ)
                data.extend(result)
            
            # convert the data from bytes to string and return it
            return bytes(data).decode('utf-8').rstrip('\x00')
        
        except Exception as e:
            print(e)

    def is_write_protected(self):
        try:
            # construct the READ command
            READ = [0xFF, 0xB0, 0x00, 0x03, 0x10]
            
            # transmit the command to the card
            result, sw1, sw2 = self.cardservice.connection.transmit(READ)
            
            # print the result for debugging
            print(f"result: {result}")
            print(f"sw1: {sw1}")
            print(f"sw2: {sw2}")
            
            # check if the card is write-protected
            if result[7] == 0x00:
                return False
            else:
                return True
        
        except Exception as e:
            print(e)

    def authenticate(self):
        try:
            # construct the AUTHENTICATE command
            AUTHENTICATE = [0xFF, 0x86, 0x00, 0x00, 0x05, 0x01, 0x00, 0x03, 0x60, 0x00]
            
            # transmit the command to the card
            result, sw1, sw2 = self.cardservice.connection.transmit(AUTHENTICATE)
            
            # check if authentication was successful
            if sw1 == 0x90 and sw2 == 0x00:
                return True
            else:
                print(sw1, sw2)
                return False
        
        except Exception as e:
            print(e)