from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from fnHelper import jsonIO
from windows.ui.ui_EditItemsDialog import Ui_Dialog
from fnHelper.load_tables import *

class EditItemsDialog(QDialog):
    def __init__(self, parent=None):
        print(__name__)
        super(EditItemsDialog, self).__init__(parent)
        self.addUserDialog()
        load_inventory_to_table(self, self.ui.businessWindow_edit_dialog_table)

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
    self.buttonRemoveFromCart_business.clicked.connect(lambda: remove_from_cart(self))
    self.buttonEditItems_business.clicked.connect(lambda: EditItemsDialog().exec())
    load_transactions_to_table(self, self.businessWindow_transactions_table)
    load_inventory_to_table(self, self.businessWindow_inventory_table)

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

def add_to_cart(self):
        selectedItems = self.businessWindow_inventory_table.selectedItems()
        if not selectedItems:
            return  # print("no selected row")
        row = selectedItems[0].row()
        self.businessWindow_cart_table.insertRow(self.businessWindow_cart_table.rowCount())
        for column in range(self.businessWindow_inventory_table.columnCount()):
            item = self.businessWindow_inventory_table.item(row, column)
            if item is not None:
                newItem = QTableWidgetItem(item.text())
                self.businessWindow_cart_table.setItem(
                    self.businessWindow_cart_table.rowCount()-1, column, newItem)
        self.businessWindow_inventory_table.removeRow(row)
        self.businessWindow_inventory_table.setCurrentItem(None)

def remove_from_cart(self):
    row = self.businessWindow_cart_table.selectedItems()[0].row()
    self.businessWindow_cart_table.removeRow(row)
    self.businessWindow_cart_table.setCurrentItem(None)



