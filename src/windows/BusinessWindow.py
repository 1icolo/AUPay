from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.find_transaction import load_transaction_table

def BusinessWindow(self):
        print(__name__)
        self.buttonAddToCart_business.clicked.connect(lambda:add_to_cart(self))
        self.buttonRemoveFromCart_business.clicked.connect(lambda:add_to_cart(self))

        
def load_user_transaction_data(self):
        transaction = load_transaction_table(self)
        # print(transaction)
        rows = len(transaction)
        columns = len(transaction[0])
        self.tableTransactions_business.setRowCount(len(transaction))
        
        for row in range(rows):
                for column in range(columns):
                        item = QTableWidgetItem(str(transaction[row][column]))
                        self.tableTransactions_business.setItem(row, column, item)


def add_to_cart(self):
    selectedItems = self.tableInventory_business.selectedItems()
    if not selectedItems:
        return #print("no selected row")
    row = selectedItems[0].row()
    self.tableCart_business.insertRow(self.tableCart_business.rowCount())
    for column in range(self.tableInventory_business.columnCount()):
        item = self.tableInventory_business.item(row, column)
        if item is not None:
            newItem = QTableWidgetItem(item.text())
            self.tableCart_business.setItem(self.tableCart_business.rowCount()-1, column, newItem)
    self.tableInventory_business.removeRow(row)
    self.tableInventory_business.setCurrentItem(None)  