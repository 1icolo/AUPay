from re import A

from numpy import add
from dbHelper.find_transaction import find_transaction
from fnHelper.aupCard import AUPCard
from fnHelper.cryptography.sha256_hash import hash
from dbHelper.add_transaction import add_transaction
from bson import Timestamp
from datetime import datetime
from fnHelper.checkBalanceSufficiency import checkBalanceSufficiency
from PyQt5.QtWidgets import QMessageBox
from fnHelper.load_tables import load_user_transaction_by_id
from dbHelper import find_user_by_id

def chargeback_transaction(Widget, transaction, description = ""):
    newTransaction = {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "destination_id": transaction['source_id'],
            "source_id": transaction['destination_id'],
            "amount": transaction['amount'],
            "description": description
        }
    print(transaction['amount'])
    if checkBalanceSufficiency(transaction['destination_id'], Widget.ui.amountLineEdit.value()):
        # if transaction['amount'] == newTransaction['amount']:
        #     QMessageBox.information(Widget, "Success", "Chargeback successful.")
        #     add_transaction(newTransaction)
        # else:
            # add_transaction(newTransaction)
            if float(Widget.ui.amountLineEdit.value()) < transaction['amount']:
                newTransaction['amount'] = float(Widget.ui.amountLineEdit.value())
                print(f"New transaction amount: {newTransaction['amount']}")
                if add_transaction(newTransaction):
                    QMessageBox.information(Widget, "Success", "Chargeback successful.")
                    # refresh(user)
            elif float(Widget.ui.amountLineEdit.value()) == transaction['amount']:
                if add_transaction(newTransaction):
                    QMessageBox.information(Widget, "Success", "Chargeback successful.")
            else:
                QMessageBox.critical(Widget, "Failed", "Chargeback failed\nAmount should be less than or equal to the transaction.")
    else:
        QMessageBox.critical(Widget, "Error", "Insufficient Balance.")