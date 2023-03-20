from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.find_transaction import load_transaction_table
import json
from fnHelper import jsonIO
from windows.ui.ui_EditItemsDialog import Ui_Dialog

class EditItemsDialog(QDialog):
    def __init__(self, parent=None):
        print(__name__)
        super(EditItemsDialog, self).__init__(parent)
        self.addUserDialog()

    def addUserDialog(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.addItemButton.clicked.connect(lambda: print("add item"))
        self.ui.removeItemButton.clicked.connect(lambda: print("remove item"))
        self.ui.saveButton.clicked.connect(lambda: self.saveItems())
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def saveItems(self):
        print("save items")

def BusinessWindow(self):
    print(__name__)
    self.buttonAddToCart_business.clicked.connect(lambda: add_to_cart(self))
    self.buttonRemoveFromCart_business.clicked.connect(lambda: add_to_cart(self))
    self.buttonEditItems_business.clicked.connect(lambda: EditItemsDialog().exec())

    newList = {
        "640ec5ac5e1ed37943867e36":
        [
            {
                "name": "Terin-terin",
                "price": 30
            },
            {
                "name": "Apple Juice",
                "price": 20
            }
        ],
        "640ec6403b6dd12f789ae93b":
        [
            {
                "name": "Orange",
                "price": 20
            },
            {
                "name": "Egg Sandwich",
                "price": 50
            }
        ]
    }

    oldList = {
        "640ec6403b6dd12f789ae93b":
        [
            {
                "name": "Orange",
                "price": 20
            },
            {
                "name": "Egg Sandwich",
                "price": 50
            }
        ],
        "640ec5ac5e1ed37943867e36":
        [
            {
                "name": "Terin-terin",
                "price": 30
            },
            {
                "name": "Apple Juice",
                "price": 20
            }
        ]
    }

    print(jsonIO.read_items())
    jsonIO.write_items(newList)
    print(jsonIO.read_items())


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
        return  # print("no selected row")
    row = selectedItems[0].row()
    self.tableCart_business.insertRow(self.tableCart_business.rowCount())
    for column in range(self.tableInventory_business.columnCount()):
        item = self.tableInventory_business.item(row, column)
        if item is not None:
            newItem = QTableWidgetItem(item.text())
            self.tableCart_business.setItem(
                self.tableCart_business.rowCount()-1, column, newItem)
    self.tableInventory_business.removeRow(row)
    self.tableInventory_business.setCurrentItem(None)


