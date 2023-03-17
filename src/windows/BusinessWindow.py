from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.find_transaction import load_transaction_table

def load_user_transaction_data(self):
        transaction = load_transaction_table(self)
        print(transaction)
        rows = len(transaction)
        columns = len(transaction[0])
        self.tableTransactions_business.setRowCount(len(transaction))
        # self.tableTransactions_business.setSelectionMode(QTableWidget.SingleSelection)
        self.tableTransactions_business.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        for row in range(rows):
                for column in range(columns):
                        item = QTableWidgetItem(str(transaction[row][column]))
                        self.tableTransactions_business.setItem(row, column, item)
                        self.tableTransactions_business.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

def BusinessWindow(self):
        print(__name__)
        load_user_transaction_data(self)