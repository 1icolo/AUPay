from dbHelper.find_transaction import find_transaction
from fnHelper.aupCard import AUPCard
from fnHelper.hashEncryption import encrypt
from dbHelper.add_transaction import add_transaction
from bson import Timestamp
from datetime import datetime

def chargeback_transaction(transaction):
    newTransaction = {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "destination_id": transaction['source_id'],
            "source_id": transaction['destination_id'],
            "amount": transaction['amount'],
            "description": (f'chargeback {transaction["_id"]}')
        }
    
    # add transaction
    add_transaction(newTransaction)