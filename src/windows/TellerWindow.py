from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper.load_tables import *

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

def TellerWindow(self):
        print(__name__)
        # load_user_transaction_data(self)
        load_transactions_to_table(self, self.tellerWindow_transactions_table)
        self.tellerWindow_transactions_table.itemSelectionChanged.connect(lambda: selected_row_to_textbox(self))


