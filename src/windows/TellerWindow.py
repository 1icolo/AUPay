from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper.load_tables import *
from fnHelper.textSearch import *
from bson import *
from datetime import *
from dbHelper.add_transaction import add_transaction
from dbHelper.compute_user_balance import compute_user_balance

def selected_row_to_textbox(self):
    selected_row = self.tellerWindow_transactions_table.currentRow()
    school_id = self.tellerWindow_transactions_table.item(selected_row, 2)
    amount = self.tellerWindow_transactions_table.item(selected_row, 4)
    description = self.tellerWindow_transactions_table.item(selected_row, 5)
    if school_id and amount and description is not None:
        # put the data in the line edit/textbox
        self.tellerWindow_schoolIdLine.setText(school_id.text())
        self.tellerWindow_amountLine.setText(amount.text())
        self.tellerWindow_descriptionLine.setText(description.text())
def transact(self, user):
    if(self.comboTransaction_teller.currentText() == "Deposit"):
        print("Deposit")
        newTransaction = {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "source_id": ObjectId(self.lineTeller_teller.text()),
            "destination_id": ObjectId(self.tellerWindow_schoolIdLine.text()),
            "amount": float(self.tellerWindow_amountLine.text()),
            "description": self.tellerWindow_descriptionLine.toPlainText()
        }
        add_transaction(newTransaction)
    elif(self.comboTransaction_teller.currentText() == "Withdraw"):
        print("Withdraw")
        newTransaction = {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "source_id": ObjectId(self.tellerWindow_schoolIdLine.text()) ,
            "destination_id": ObjectId(self.lineTeller_teller.text()),
            "amount": float(self.tellerWindow_amountLine.text()),
            "description": self.tellerWindow_descriptionLine.toPlainText()
        }
        add_transaction(newTransaction)
    load_user_transaction_by_id(self.tellerWindow_transactions_table, user)
    self.tellerWindow_transactions_table.setCurrentItem(None)
    self.tellerWindow_schoolIdLine.setText("")
    self.tellerWindow_amountLine.setText("")
    self.tellerWindow_descriptionLine.setText("")

def deposit_withdraw (self):
     self.comboTransaction_teller.getText()
     self.tellerWindow_descriptionLine.setText("")

def TellerWindow(self, user):
        print(__name__)
        # load_user_transaction_data(self)
        self.lineTeller_teller.setText(str(user['_id']))
        # testing school id only
        self.tellerWindow_schoolIdLine.setText(str(user['_id']))
        load_transactions_to_table(self, self.tellerWindow_transactions_table)
        load_user_transaction_by_id(self.tellerWindow_transactions_table, user['_id'])
        self.tellerWindow_transactions_table.itemSelectionChanged.connect(lambda: selected_row_to_textbox(self))
        self.tellerWindow_transaction_search.textChanged.connect(lambda text: search_transactions(self, text, self.tellerWindow_transactions_table))
        self.buttonTransact_teller.clicked.connect(lambda: transact(self, user['_id']))
        self.lineBalance_teller.setText(compute_user_balance(user['_id']))

        



