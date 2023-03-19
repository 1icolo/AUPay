from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login
from dbHelper.find_transaction import load_transaction_table

def UserWindow(self, user):
        print(__name__)
        load_user_data(self, user)
        load_user_transaction_data(self)

def load_user_data(self, user):
        print(self.lineSchoolId_user.setText(user['school_id']))
        print("Hello")
        self.lineBalance_user.setText(user['balance'])


def load_user_transaction_data(self):
        transaction = load_transaction_table(self)
        # print(transaction)
        rows = len(transaction)
        columns = len(transaction[0])
        self.userTable_Window.setRowCount(len(transaction))
        # self.userTable_Window.setSelectionMode(QTableWidget.SingleSelection)
        self.userTable_Window.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Add the user data to the table
        for row in range(rows):
                for column in range(columns):
                        item = QTableWidgetItem(str(transaction[row][column]))
                        self.userTable_Window.setItem(row, column, item)
                        self.userTable_Window.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)