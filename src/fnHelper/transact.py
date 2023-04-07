from bson import ObjectId, Timestamp
from datetime import datetime
from dbHelper import add_transaction
from fnHelper import load_user_transaction_by_id
from fnHelper.aupCard import AUPCard
from fnHelper.hashEncryption import encrypt
from dbHelper.find_user import find_user_by_card_id
from fnHelper.output_to_dict import output_to_dict
from fnHelper.checkBalanceSufficiency import checkBalanceSufficiency
from PyQt5.QtWidgets import QMessageBox


def transact(Widget, teller):
    user = find_user_by_card_id(encrypt(AUPCard().get_uid()))
    if user is None:
        return print("No RFID detected.")

    newTransaction = {
        "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
        "source_id": None,
        "destination_id": None,
        "amount": float(Widget.tellerWindow_amountLine.text()),
        "description": Widget.tellerWindow_descriptionLine.toPlainText()
    }
    
    checkBalance = None
    match Widget.comboTransaction_teller.currentText():
        
        case "Deposit":
            newTransaction['source_id'] = ObjectId(teller['_id'])
            newTransaction['destination_id'] = ObjectId(user['_id'])
            checkBalance = teller['_id']
        case "Withdraw":
            newTransaction['source_id'] = ObjectId(user['_id'])
            newTransaction['destination_id'] = ObjectId(teller['_id'])
            checkBalance = user['_id']

    if checkBalanceSufficiency(checkBalance, newTransaction['amount']):
        add_transaction(newTransaction)
        load_user_transaction_by_id(
            Widget.tellerWindow_transactions_table, teller['_id']
        )
        Widget.tellerWindow_transactions_table.setCurrentItem(None)
        Widget.buttonClearFields_teller.click()
        return QMessageBox.information(Widget, "Success", "Charge successful.")
    else:
        return QMessageBox.critical(Widget, "Error", "Insufficient Balance.")
