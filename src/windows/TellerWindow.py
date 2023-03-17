from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.find_transaction import load_transaction_table

def load_user_transaction_data(self):
        transaction = load_transaction_table(self)
        print(transaction)
        rows = len(transaction)
        columns = len(transaction[0])
        self.tabletTransactions_teller.setRowCount(len(transaction))
        # self.tabletTransactions_teller.setSelectionMode(QTableWidget.SingleSelection)
        self.tabletTransactions_teller.setSelectionBehavior(QAbstractItemView.SelectRows)
        

        for row in range(rows):
                for column in range(columns):
                        item = QTableWidgetItem(str(transaction[row][column]))
                        self.tabletTransactions_teller.setItem(row, column, item)
                        self.tabletTransactions_teller.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tabletTransactions_teller.itemSelectionChanged.connect(lambda: showData(self))

        def showData(self):
                selected_row = self.tabletTransactions_teller.currentRow()
                
                # _id = self.tabletTransactions_teller.item(selected_row, 0).text()
                # date_string = self.tabletTransactions_teller.item(selected_row, 1).text()
                source_id = self.tabletTransactions_teller.item(selected_row, 2).text()
                # destination_id = self.tabletTransactions_teller.item(selected_row, 3).text()
                amount = self.tabletTransactions_teller.item(selected_row, 4).text()
                description = self.tabletTransactions_teller.item(selected_row, 5).text()

                # put the data in the line edit
                self.lineSchoolId_teller.setText(source_id)
                self.lineAmount_teller.setText(amount)
                self.textDescription_teller.setText(description)

def TellerWindow(self):
        print(__name__)
        load_user_transaction_data(self)

