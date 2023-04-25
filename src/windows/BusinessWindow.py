from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from bson import *
from datetime import *
from fnHelper import jsonIO
from windows.ui.ui_EditItemsDialog import Ui_Dialog
from windows.ui.ui_ChargebackTransactionDialog import Ui_Dialog as Ui_ChargebackTransactionDialog
from fnHelper.load_tables import *
from fnHelper.textSearch import *
from dbHelper.add_transaction import add_transaction
from fnHelper.charge import charge_transaction
from dbHelper.find_transaction import find_transaction
from fnHelper.aupCard import AUPCard
from dbHelper.find_user import find_user_by_id
from fnHelper.cryptography import hash
from fnHelper.chargeback import chargeback_transaction
from dbHelper.compute_user_balance import compute_user_balance
from fnHelper.export_to_csv import *
from fnHelper import export_window_to_pdf
from fnHelper.refresh_clear import *
from fnHelper.charts import item_frequency_pie_chart, transactions_top_contributors, transactions_count_per_month
from windows.ProjectMainWindow import ProjectMainWindow



def charge(self, user):
    if not self.businessWindow_amountLine.text() == "":
        charge_transaction(self, user)

    # print(newTransaction)
def search_inventory(self, text):
    # iterate over each row in the inventory table
    for row in range(self.businessWindow_inventory_table.rowCount()):
        item_name = self.businessWindow_inventory_table.item(row, 0).text()
        item_price = self.businessWindow_inventory_table.item(row, 1).text()

        # check if the search text is a substring of any of the items in the row
        if text.lower() in item_name.lower() or text.lower() in item_price.lower():
            self.businessWindow_inventory_table.setRowHidden(row, False)
        else:
            self.businessWindow_inventory_table.setRowHidden(row, True)

def chargebackTransaction(self):
    selected_row = self.businessWindow_transactions_table.currentRow()
    item = self.businessWindow_transactions_table.item(selected_row, 0)
    if item is None:
        return print("select row to chargeback")
    id = ObjectId(self.businessWindow_transactions_table.item(selected_row, 0).text())
    current_transaction_data = find_transaction(id)
    if current_transaction_data['description'].__contains__("chargeback"):
        QMessageBox.warning(self, "Error", "This transaction is a chargeback transaction.")
    else:
        ChargebackDialog(current_transaction_data).exec()


class ChargebackDialog(QDialog):
    table_updated = pyqtSignal()
    def __init__(self, transaction_data, parent=None):
        print(__name__)
        super(ChargebackDialog, self).__init__(parent)
        self.chargebackDialog()
        self.ui.sourceIDLineEdit.setText(str(transaction_data['destination_id']))
        self.ui.destinationIDLineEdit.setText(str(transaction_data['source_id']))
        self.ui.amountLineEdit.setText(str(transaction_data['amount']))
        self.ui.descriptionLineEdit.setText(f'chargeback transaction {transaction_data["_id"]}')
        self.ui.buttonSave_addTransaction.clicked.connect(lambda: self.chargeback(transaction_data))
        self.ui.buttonScanBusiness.clicked.connect(lambda: self.scanId('business', transaction_data))
        self.ui.buttonScanUser.clicked.connect(lambda: self.scanId('user', transaction_data))
    
    def chargebackDialog(self):
        self.ui = Ui_ChargebackTransactionDialog()
        self.ui.setupUi(self)

    def scanId(self, user_type, transaction_data):
        match user_type:
            case 'business':
                user = find_user_by_id(transaction_data['destination_id'])
                if hash(AUPCard().get_uid()) == user['card_id']:
                    print("Business verified")
                    self.ui.checkBoxBusiness.setChecked(True)
            case 'user': 
                user = find_user_by_id(transaction_data['source_id'])
                if hash(AUPCard().get_uid()) == user['card_id']:
                    print("User verified")
                    self.ui.checkBoxUser.setChecked(True)

    def chargeback(self, transaction_data):
        if self.ui.checkBoxBusiness.isChecked() and self.ui.checkBoxUser.isChecked():
            chargeback_transaction(self, transaction_data)
            self.table_updated.emit()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Business and User verification required")

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
        load_inventory_to_table(self.ui.businessWindow_edit_dialog_table)
        self.ui.businessWindow_edit_dialog_table.itemSelectionChanged.connect(lambda: self.edit_dialog_selected_row())
        self.ui.moveUpButton.clicked.connect(lambda: self.move_row_up())
        self.ui.moveDownButton.clicked.connect(lambda: self.move_row_down())
        

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
        items_data = [[item['price'], item['name']] for item in self.items]
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
        items_data = [[item['price'], item['name']] for item in self.items]
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
        items_data = []
        for row in range(self.ui.businessWindow_edit_dialog_table.rowCount()):
            item_name = self.ui.businessWindow_edit_dialog_table.item(row, 1).text()
            item_price = self.ui.businessWindow_edit_dialog_table.item(row, 0).text()
            if item_name and item_price:
                items_data.append({'name': item_name, 'price': item_price})
        jsonIO.write_items(items_data)
        self.items = items_data
        self.close()
        print("Items saved")

    def edit_dialog_selected_row(self):
        selected_row = self.ui.businessWindow_edit_dialog_table.currentRow()
        price = self.ui.businessWindow_edit_dialog_table.item(selected_row, 0)
        name = self.ui.businessWindow_edit_dialog_table.item(selected_row, 1)
        if name and price is not None:
            # put the data in the line edit/textbox
            self.ui.businessWindow_edit_dialog_nameLine.setText(name.text())
            self.ui.businessWindow_edit_dialog_priceLine.setText(price.text())
            
    def clear_field(self):
        self.ui.businessWindow_edit_dialog_nameLine.setText("")
        self.ui.businessWindow_edit_dialog_priceLine.setText("")

    def move_row_up(self):
        current_row = self.ui.businessWindow_edit_dialog_table.currentRow()
        if current_row > 0:
            # Remove entire row and insert at row above
            row_items = []
            for col in range(self.ui.businessWindow_edit_dialog_table.columnCount()):
                item = self.ui.businessWindow_edit_dialog_table.takeItem(current_row, col)
                row_items.append(item)
            self.ui.businessWindow_edit_dialog_table.removeRow(current_row)
            self.ui.businessWindow_edit_dialog_table.insertRow(current_row - 1)
            for col, item in enumerate(row_items):
                self.ui.businessWindow_edit_dialog_table.setItem(current_row - 1, col, item)
            # Update selection to moved row
            self.ui.businessWindow_edit_dialog_table.selectRow(current_row - 1)

    def move_row_down(self):
        current_row = self.ui.businessWindow_edit_dialog_table.currentRow()
        if current_row < self.ui.businessWindow_edit_dialog_table.rowCount() - 1:
            # Remove entire row and insert at row below
            row_items = []
            for col in range(self.ui.businessWindow_edit_dialog_table.columnCount()):
                item = self.ui.businessWindow_edit_dialog_table.takeItem(current_row, col)
                row_items.append(item)
            self.ui.businessWindow_edit_dialog_table.removeRow(current_row)
            self.ui.businessWindow_edit_dialog_table.insertRow(current_row + 1)
            for col, item in enumerate(row_items):
                self.ui.businessWindow_edit_dialog_table.setItem(current_row + 1, col, item)
            # Update selection to moved row
            self.ui.businessWindow_edit_dialog_table.selectRow(current_row + 1)

def open_edit_items_dialog(self, user):
    self.edit_items_dialog = EditItemsDialog()
    self.edit_items_dialog.ui.saveButton.clicked.connect(lambda: reload_inventory_table(self, user))
    self.edit_items_dialog.exec_()
    
def reload_inventory_table(self, user):
    load_inventory_to_table(self.businessWindow_inventory_table)    
    self.businessWindow_inventory_table.setCurrentItem(None)
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
        self.businessWindow_inventory_table.setCurrentItem(None)
        print("added to cart")  
        get_cart_data(self)

def get_cart_data(self):
    total_amount = 0
    description = ""
    
    # iterate over each row in the cart table
    for row in range(self.businessWindow_cart_table.rowCount()):
        item_price = self.businessWindow_cart_table.item(row, 0).text()
        item_name = self.businessWindow_cart_table.item(row, 1).text()

        total_amount += float(item_price)

        if description == "":
            description += item_name
        else:
            description += ", " + item_name

    self.businessWindow_amountLine.setText(str(total_amount))
    self.businessWindow_descriptionLine.setText(description)


def remove_from_cart(self):
    selectedItem = self.businessWindow_cart_table.selectedItems()
    if not selectedItem:
        return  # print("no selected row")
    row = selectedItem[0].row()
    self.businessWindow_cart_table.removeRow(row)
    self.businessWindow_cart_table.setCurrentItem(None)
    print("removed from cart")
    get_cart_data(self)

def add_item_shortcut(self, event):
    for row in range(self.businessWindow_inventory_table.rowCount()):
        if row <= 12:
            item_price = self.businessWindow_inventory_table.item(row, 0).text()
            item_name = self.businessWindow_inventory_table.item(row, 1).text()
            
            if event.key() == Qt.Key_F1:
                row_index = 0
            elif event.key() == Qt.Key_F2:
                row_index = 1
            elif event.key() == Qt.Key_F3:
                row_index = 2
            elif event.key() == Qt.Key_F4:
                row_index = 3
            elif event.key() == Qt.Key_F5:
                row_index = 4
            elif event.key() == Qt.Key_F6:
                row_index = 5
            elif event.key() == Qt.Key_F7:
                row_index = 6
            elif event.key() == Qt.Key_F8:
                row_index = 7
            elif event.key() == Qt.Key_F9:
                row_index = 8
            elif event.key() == Qt.Key_F10:
                row_index = 9
            elif event.key() == Qt.Key_F11:
                row_index = 10
            elif event.key() == Qt.Key_F12:
                row_index = 11
            else:
                return

            # Check if the selected row corresponds to the pressed key
            if row == row_index:
                # Add the selected item to the cart table
                cart_table = self.businessWindow_cart_table
                row_count = cart_table.rowCount()
                cart_table.insertRow(row_count)
                cart_table.setItem(row_count, 1, QTableWidgetItem(item_name))
                cart_table.setItem(row_count, 0, QTableWidgetItem(str(item_price)))
            get_cart_data(self)


def navbar(self: ProjectMainWindow, business):
    self.dateTo_business.setDate(QDate.currentDate())
    self.lineBalance_business.setText(str(business['balance']))
    self.lineBusiness_business.setText(business['school_id'])
    self.navHome_business.clicked.connect(lambda: self.stackedWidget_business.setCurrentIndex(0))
    self.navDashboard_business.clicked.connect(lambda: self.stackedWidget_business.setCurrentIndex(1))
    self.navAnalytics_business.clicked.connect(lambda: self.stackedWidget_business.setCurrentIndex(2))
    self.navTransactions_business.clicked.connect(lambda: self.stackedWidget_business.setCurrentIndex(3))

def analytics(self: ProjectMainWindow):
    item_frequency_pie_chart(self.businessWindow_transactions_table, self.graphicsView_business_1)
    transactions_count_per_month(self.businessWindow_transactions_table, self.graphicsView_business_2)
    transactions_top_contributors(self.businessWindow_transactions_table, self.graphicsView_business_3)

def tables(self: ProjectMainWindow, business):
    load_user_transaction_by_id(self.businessWindow_transactions_table, business)
    load_inventory_to_table(self.businessWindow_inventory_table)

def dateChanged(self: ProjectMainWindow, business):
    search_transactions_by_date(self.businessWindow_transactions_table, self.dateFrom_business, self.dateTo_business)
    analytics(self)

def searchChanged(self: ProjectMainWindow):
    self.businessWindow_transaction_search.textChanged.connect(lambda text: search_transactions(text, self.businessWindow_transactions_table))
    analytics(self)

def clearField(self: ProjectMainWindow, business):
    self.buttonClearTransactions_business.clicked.connect(lambda: clear_date(self.dateFrom_business, self.dateTo_business, self.businessWindow_transactions_table))
    analytics(self)

def refresh(self: ProjectMainWindow, business):
    navbar(self, business)
    tables(self, business)
    analytics(self)

def BusinessWindow(self: ProjectMainWindow, business):
    print(__name__)
    refresh(self, business)
    self.refreshButton_business.clicked.connect(lambda: refresh(self, business))
    self.businessWindow_transaction_search.textChanged.connect(lambda: searchChanged(self))
    self.dateFrom_business.dateChanged.connect(lambda: dateChanged(self, business))
    self.dateTo_business.dateChanged.connect(lambda: dateChanged(self, business))
    self.buttonClearTransactions_business.clicked.connect(lambda: clearField(self, business))
    self.exportCSV_business.clicked.connect(lambda: export_to_csv(self.businessWindow_transactions_table, business))
    self.exportPDF_business.clicked.connect(lambda: export_window_to_pdf(self, business))

    #business
    self.buttonAddToCart_business.clicked.connect(lambda: add_to_cart(self))
    self.buttonRemoveFromCart_business.clicked.connect(lambda: remove_from_cart(self))
    self.buttonEditItems_business.clicked.connect(lambda: open_edit_items_dialog(self, business))
    self.buttonCharge.clicked.connect(lambda: charge(self, business))
    self.businessWindow_inventory_search.textChanged.connect(lambda text: search_inventory(self, text))
    self.keyPressEvent = (lambda event: add_item_shortcut(self, event))
    self.buttonChargeback_business.clicked.connect(lambda: chargebackTransaction(self))

