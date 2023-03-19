from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.find_transaction import load_transaction_table

def load_user_transaction_data(self):
        transaction = load_transaction_table(self)
        # print(transaction)
        rows = len(transaction)
        columns = len(transaction[0])
        self.tabletTransactions_teller.setRowCount(len(transaction))
        
        for row in range(rows):
                for column in range(columns):
                        item = QTableWidgetItem(str(transaction[row][column]))
                        self.tabletTransactions_teller.setItem(row, column, item)
        self.tabletTransactions_teller.itemSelectionChanged.connect(lambda: showData(self))

        def showData(self):
                selected_row = self.tabletTransactions_teller.currentRow()

                # put the data in the line edit/textbox
                self.lineSchoolId_teller.setText(self.tabletTransactions_teller.item(selected_row, 2).text())
                self.lineAmount_teller.setText(self.tabletTransactions_teller.item(selected_row, 4).text())
                self.textDescription_teller.setText(self.tabletTransactions_teller.item(selected_row, 5).text())

def TellerWindow(self):
        print(__name__)
        load_user_transaction_data(self)

