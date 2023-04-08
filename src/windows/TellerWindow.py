from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper.load_tables import *
from fnHelper.textSearch import *
from bson import *
from datetime import *
from dbHelper.add_transaction import add_transaction
from dbHelper.compute_user_balance import compute_user_balance
from fnHelper.transact import transact

def selected_row_to_textbox(self):
    selected_row = self.tellerWindow_transactions_table.currentRow()
    school_id = self.tellerWindow_transactions_table.item(selected_row, 2)
    amount = self.tellerWindow_transactions_table.item(selected_row, 4)
    description = self.tellerWindow_transactions_table.item(selected_row, 5)
    if school_id and amount and description is not None:
        # put the data in the line edit/textbox
        self.tellerWindow_amountLine.setText(amount.text())
        self.tellerWindow_descriptionLine.setText(description.text())

def TellerWindow(self, user):
    print(__name__)
    self.lineBalance_teller.setText(str(compute_user_balance(user['_id'])))
    # load_user_transaction_data(self)
    self.lineTeller_teller.setText(str(user['school_id']))
    # testing school id only
    # load_transactions_to_table(self, self.tellerWindow_transactions_table)
    load_user_transaction_by_id(self.tellerWindow_transactions_table, user['_id'])
    self.tellerWindow_transactions_table.itemSelectionChanged.connect(lambda: selected_row_to_textbox(self))
    self.tellerWindow_transaction_search.textChanged.connect(lambda text: search_transactions(self, text, self.tellerWindow_transactions_table))
    self.buttonTransact_teller.clicked.connect(lambda: transactAttempt(self, user))
    self.lineBalance_teller.setText(str(compute_user_balance(user['_id'])))

        
def transactAttempt(self, user):
    if not self.tellerWindow_amountLine.text() == "" and not self.tellerWindow_descriptionLine.toPlainText() == "":
        transact(self,user)


