from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper.load_tables import *

def selected_row_to_textbox(self):
        selected_row = self.tellerWindow_transactions_table.currentRow()
        # put the data in the line edit/textbox
        self.tellerWindow_schoolIdLine.setText(self.tellerWindow_transactions_table.item(selected_row, 2).text())
        self.tellerWindow_amountLine.setText(self.tellerWindow_transactions_table.item(selected_row, 4).text())
        self.tellerWindow_descriptionLine.setText(self.tellerWindow_transactions_table.item(selected_row, 5).text())

def TellerWindow(self):
        print(__name__)
        # load_user_transaction_data(self)
        load_transactions_to_table(self, self.tellerWindow_transactions_table)
        self.tellerWindow_transactions_table.itemSelectionChanged.connect(lambda: selected_row_to_textbox(self))


