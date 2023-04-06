from bson import ObjectId, Timestamp
from datetime import datetime
from dbHelper import add_transaction
from fnHelper import load_user_transaction_by_id
from fnHelper.aupCard import AUPCard
from fnHelper.hashEncryption import encrypt
from dbHelper.find_user import find_user_by_card_id
from fnHelper.output_to_dict import output_to_dict

def transact(Widget, teller):
    user = find_user_by_card_id(encrypt(AUPCard().get_uid()))
    if user is None:
        return print("No RFID detected.")
    if(Widget.comboTransaction_teller.currentText() == "Deposit"):
        print("Deposit")
        newTransaction = {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "source_id": ObjectId(teller['_id']),
            "destination_id": ObjectId(user['_id']),
            "amount": float(Widget.tellerWindow_amountLine.text()),
            "description": Widget.tellerWindow_descriptionLine.toPlainText()
        }
    elif(Widget.comboTransaction_teller.currentText() == "Withdraw"):
        print("Withdraw")
        newTransaction = {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "source_id": ObjectId(user['_id']),
            "destination_id": ObjectId(teller['_id']),
            "amount": float(Widget.tellerWindow_amountLine.text()),
            "description": Widget.tellerWindow_descriptionLine.toPlainText()
        }
    add_transaction(newTransaction)
        
    load_user_transaction_by_id(Widget.tellerWindow_transactions_table, teller['_id'])
    Widget.tellerWindow_transactions_table.setCurrentItem(None)
    Widget.tellerWindow_schoolIdLine.setText("")
    Widget.tellerWindow_amountLine.setText("")
    Widget.tellerWindow_descriptionLine.setText("")