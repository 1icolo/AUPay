from dbHelper.add_transaction import add_transaction
from fnHelper.checkBalanceSufficiency import checkBalanceSufficiency
from fnHelper.load_tables import load_user_transaction_by_id, refresh_bar_chart
from bson import Timestamp, ObjectId
from datetime import datetime
from fnHelper.aupCard import AUPCard
from dbHelper.find_user import find_user_by_card_id
from fnHelper.hashEncryption import encrypt
from PyQt5.QtWidgets import QMessageBox

def charge_transaction(Widget, business):

    def refresh(self):
        Widget.businessWindow_amountLine.setText("")
        Widget.businessWindow_descriptionLine.setText("")
        Widget.businessWindow_cart_table.clearContents()
        Widget.businessWindow_cart_table.setRowCount(0)
        # Call update_bar_chart after adding a new transaction
        load_user_transaction_by_id(Widget.businessWindow_transactions_table, business['_id'])
        refresh_bar_chart(self.businessWindow_transactions_table, self.graphicsView_2)

    transaction = {
        "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
        "destination_id": ObjectId(business['_id']),
        "source_id": None,
        "amount": float(Widget.businessWindow_amountLine.text()),
        "description": Widget.businessWindow_descriptionLine.toPlainText()
    }
    try:
        transaction['source_id'] = find_user_by_card_id(encrypt(AUPCard().get_uid()))['_id']
    except:
        QMessageBox.critical(Widget, "Error", "No RFID detected.")


    if transaction['source_id'] is not None:
        if checkBalanceSufficiency(transaction['source_id'], transaction['amount']):
            add_transaction(transaction)
            refresh()
            return QMessageBox.information(Widget, "Success", "Charge successful.")
        return QMessageBox.critical(Widget, "Error", "Insufficient Balance.")
        
    
    
    
