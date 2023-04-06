from dbHelper.find_transaction import find_transaction
from fnHelper.aupCard import AUPCard
from fnHelper.hashEncryption import encrypt
from dbHelper.add_transaction import add_transaction
from bson import Timestamp
from datetime import datetime
from fnHelper.checkBalanceSufficiency import checkBalanceSufficiency
from PyQt5.QtWidgets import QMessageBox

def chargeback_transaction(QWidget, transaction):
    newTransaction = {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "destination_id": transaction['source_id'],
            "source_id": transaction['destination_id'],
            "amount": transaction['amount'],
            "description": (f'chargeback {transaction["_id"]}')
        }
    print(transaction['amount'])
    if checkBalanceSufficiency(transaction['destination_id'], transaction['amount']):
        # add transaction
        QMessageBox.information(QWidget, "Success", "Chargeback successful.")
        return add_transaction(newTransaction)
    return QMessageBox.critical(QWidget, "Error", "Insufficient Balance.")