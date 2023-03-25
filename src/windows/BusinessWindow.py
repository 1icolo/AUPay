from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import json
from fnHelper import jsonIO
from windows.ui.ui_EditItemsDialog import Ui_Dialog
from fnHelper.load_tables import *

def BusinessWindow(self):
    print(__name__)
    self.buttonAddToCart_business.clicked.connect(lambda: add_to_cart(self))
    self.buttonRemoveFromCart_business.clicked.connect(lambda: remove_from_cart(self))
    self.buttonEditItems_business.clicked.connect(lambda: open_edit_items_dialog(self))
    load_transactions_to_table(self, self.businessWindow_transactions_table)
    load_inventory_to_table(self, self.businessWindow_inventory_table)
    self.businessWindow_inventory_table.itemSelectionChanged.connect(lambda:selected_row_to_textbox(self, self.businessWindow_inventory_table))
    self.businessWindow_cart_table.itemSelectionChanged.connect(lambda:selected_row_to_textbox(self, self.businessWindow_cart_table))

class EditItemsDialog(QDialog):
    def __init__(self, parent=None):
        print(__name__)
        super(EditItemsDialog, self).__init__(parent)
        self.addUserDialog()

    def addUserDialog(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.addItemButton.clicked.connect(lambda: self.addItem())
        self.ui.updateItemButton.clicked.connect(lambda: self.updateItem())
        self.ui.removeItemButton.clicked.connect(lambda: self.removeItem())
        self.ui.saveButton.clicked.connect(lambda: self.saveItems())
        self.ui.cancelButton.clicked.connect(lambda: self.close())
        load_inventory_to_table(self, self.ui.businessWindow_edit_dialog_table)
        self.ui.businessWindow_edit_dialog_table.itemSelectionChanged.connect(lambda: self.edit_dialog_selected_row())

        self.items = jsonIO.read_items()
        
    def addItem(self):
        new_item = {'name':self.ui.businessWindow_edit_dialog_nameLine.text(), 'price': self.ui.businessWindow_edit_dialog_priceLine.text()}
        if any(item['name'] == new_item['name'] for item in self.items):
            self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)
            return print("Item already exists")
        if not all(new_item.values()):
            self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)
            return print("Provide data to insert")
        self.items.append(new_item)
        items_data = [[item['name'], item['price']] for item in self.items]
        self.ui.businessWindow_edit_dialog_table.setRowCount(len(items_data))
        for row, item in enumerate(items_data):
            for column, value in enumerate(item):
                item = QTableWidgetItem(str(value))
                self.ui.businessWindow_edit_dialog_table.setItem(row, column, item)
        print(new_item)
        self.clear_field()
        print("Item added")
        self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)

    def updateItem(self):
        selected_item = self.ui.businessWindow_edit_dialog_table.currentItem()
        if selected_item is None:
            self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)
            return print("Select a row/item to update")
        row = self.ui.businessWindow_edit_dialog_table.currentRow()
        item_name = self.items[row]['name']
        update_item = {'name': self.ui.businessWindow_edit_dialog_nameLine.text(), 'price': self.ui.businessWindow_edit_dialog_priceLine.text()}
        if not all(update_item.values()):
            self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)
            return print("Provide data to update")
        for item in self.items:
            if item['name'] == item_name:
                item.update(update_item)
                break
        items_data = [[item['name'], item['price']] for item in self.items]
        for row, item in enumerate(items_data):
            for column, value in enumerate(item):
                item = QTableWidgetItem(str(value))
                self.ui.businessWindow_edit_dialog_table.setItem(row, column, item)
        self.clear_field()
        print("Item updated")
        self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)

    def removeItem(self):
        selectedItem = self.ui.businessWindow_edit_dialog_table.selectedItems()
        if not selectedItem:
            return print("no selected row")
        row = selectedItem[0].row()
        item_name = self.items[row]['name']

        # Show the confirmation dialog
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Delete Item")
        msg_box.setText(f"Are you sure you want to delete the item '{item_name}'?")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        msg_box.setIcon(QMessageBox.Warning)
        response = msg_box.exec()

        if response == QMessageBox.Ok:
            del self.items[row]
            self.ui.businessWindow_edit_dialog_table.removeRow(row)
            print("Item removed")
            self.clear_field()
        else: 
            print("Item removal cancelled")
        self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)

    def saveItems(self):
        jsonIO.write_items(self.items)
        print("save items")
        self.close()

    def edit_dialog_selected_row(self):
        selected_row = self.ui.businessWindow_edit_dialog_table.currentRow()
        name = self.ui.businessWindow_edit_dialog_table.item(selected_row, 0)
        price = self.ui.businessWindow_edit_dialog_table.item(selected_row, 1)
        if name and price is not None:
            # put the data in the line edit/textbox
            self.ui.businessWindow_edit_dialog_nameLine.setText(name.text())
            self.ui.businessWindow_edit_dialog_priceLine.setText(price.text())
            
    def clear_field(self):
        self.ui.businessWindow_edit_dialog_nameLine.setText("")
        self.ui.businessWindow_edit_dialog_priceLine.setText("")

def open_edit_items_dialog(self):
    self.edit_items_dialog = EditItemsDialog()
    self.edit_items_dialog.ui.saveButton.clicked.connect(lambda: reload_inventory_table(self))
    self.edit_items_dialog.exec_()
    
def reload_inventory_table(self):
    load_inventory_to_table(self, self.businessWindow_inventory_table)
    self.businessWindow_inventory_table.setCurrentItem(None)
    self.businessWindow_sourceLine.setText("")
    self.businessWindow_descriptionLine.setText("")
    self.businessWindow_amountLine.setText("")

def add_to_cart(self):
        selectedItem = self.businessWindow_inventory_table.selectedItems()
        if not selectedItem:
            return  # print("no selected row")
        row = selectedItem[0].row()
        self.businessWindow_cart_table.insertRow(self.businessWindow_cart_table.rowCount())
        for column in range(self.businessWindow_inventory_table.columnCount()):
            item = self.businessWindow_inventory_table.item(row, column)
            if item is not None:
                newItem = QTableWidgetItem(item.text())
                self.businessWindow_cart_table.setItem(self.businessWindow_cart_table.rowCount()-1, column, newItem)
        self.businessWindow_inventory_table.removeRow(row)
        self.businessWindow_inventory_table.setCurrentItem(None)

        self.businessWindow_sourceLine.setText("")
        self.businessWindow_descriptionLine.setText("")
        self.businessWindow_amountLine.setText("")
        print("added to cart")  

def remove_from_cart(self):
    selectedItem = self.businessWindow_cart_table.selectedItems()
    if not selectedItem:
        return  # print("no selected row")
    row = selectedItem[0].row()
    self.businessWindow_cart_table.removeRow(row)
    self.businessWindow_cart_table.setCurrentItem(None)

    self.businessWindow_sourceLine.setText("")
    self.businessWindow_descriptionLine.setText("")
    self.businessWindow_amountLine.setText("")
    print("removed from cart")

def selected_row_to_textbox(self, tableWidget):
    selected_row = tableWidget.currentRow()
    name = tableWidget.item(selected_row, 0)
    price = tableWidget.item(selected_row, 1)
    if name and price is not None:
        # put the data in the line edit/textbox
        self.businessWindow_descriptionLine.setText(name.text())
        self.businessWindow_amountLine.setText(price.text())

