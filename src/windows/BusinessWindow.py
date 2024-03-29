from os import name
from typing import ItemsView
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
from bson import *
from datetime import *
from fnHelper import jsonIO, transact
from windows.ui.ui_EditItemsDialog import Ui_Dialog
from windows.ui.ui_ChargebackTransactionDialog import Ui_Dialog as Ui_ChargebackTransactionDialog
from fnHelper.load_tables import *
from fnHelper.textSearch import *
from dbHelper.add_transaction import add_transaction
from fnHelper.charge import charge_transaction
from dbHelper.find_transaction import find_transaction
from fnHelper.aupCard import AUPCard
from dbHelper.find_user import find_user_by_id
from fnHelper.cryptography.sha256_hash import hash
from fnHelper.chargeback import chargeback_transaction
from dbHelper.compute_user_balance import compute_user_balance
from fnHelper.export_to_csv import *
from fnHelper import export_window_to_pdf
from fnHelper.refresh_clear import *
from fnHelper.charts import item_frequency_pie_chart, transactions_count_per_month, transactions_total
from windows.ProjectMainWindow import ProjectMainWindow
from fnHelper import setDateRangeFields
from fnHelper import item_counter, item_counter_deductive


def charge(self: ProjectMainWindow, user):
    if not self.businessWindow_amountLine.text() == "" and not self.businessWindow_descriptionLine.toPlainText() == "":
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


def compute_valid_amount(transaction_id):
    transactions = find_chargeback_transactions(transaction_id)
    total_valid_amount = float(0)
    for transaction in transactions:
        total_valid_amount = float(transaction['amount']) + total_valid_amount
    return total_valid_amount


def chargebackTransaction(self):
    selected_row = self.businessWindow_transactions_table.currentRow()
    item = self.businessWindow_transactions_table.item(selected_row, 0)
    if item is None:
        return print("select row to chargeback")
    id = ObjectId(self.businessWindow_transactions_table.item(
        selected_row, 0).text())
    current_transaction_data = find_transaction(id)
    if current_transaction_data['description'].__contains__("chargeback"):
        QMessageBox.warning(
            self, "Error", "This transaction is a chargeback transaction.")
    else:
        valid_amount = current_transaction_data['amount'] - \
            compute_valid_amount(current_transaction_data['_id'])
        if valid_amount > 0:
            ChargebackDialog(current_transaction_data, valid_amount).exec_()
        else:
            QMessageBox.warning(
                self, "Error", "Transaction cannot be chargedback.")


class ChargebackDialog(QDialog):
    def __init__(self, transaction_data, valid_amount, parent=None):
        print(__name__)
        super(ChargebackDialog, self).__init__(parent)
        self.chargebackDialog()
        self.valid_amount = valid_amount
        self.item_rows = []
        self.chargebacked_items = []
        self.ui.buttonSave_addTransaction.clicked.connect(
            lambda: self.chargeback(transaction_data))
        self.ui.buttonScanBusiness.clicked.connect(
            lambda: self.scanId('business', transaction_data))
        self.ui.buttonScanUser.clicked.connect(
            lambda: self.scanId('user', transaction_data))
        self.ui.amountLineEdit.valueChanged.connect(
            lambda: self.chargeback_enable_checker())
        for count, item in enumerate(item_counter_deductive(transaction_data['description'])):
            self.create_row(item['name'], int(item['price']), int(item['quantity']), count)

    def get_form_data(self):
        data = []
        for i in range(self.ui.form_layout_item_list.rowCount()):
            item_name_label = self.ui.form_layout_item_list.itemAt(
                i, QFormLayout.LabelRole).widget()
            item_name = item_name_label.text()
            item_quantity_spinbox = self.ui.form_layout_item_list.itemAt(
                i, QFormLayout.FieldRole).widget()
            item_quantity = item_quantity_spinbox.value()
            data.append({'name': item_name, 'quantity': item_quantity})
        return data

    def create_row(self, item_name: str, item_price: int, item_quantity: int, row_number: int):
        self.item_name = QLabel(self.ui.scroll_area_container)
        self.item_name.setObjectName(f"item_{item_name}_label")
        self.item_name.setText(f"{item_name}")
        self.ui.form_layout_item_list.setWidget(
            row_number, QFormLayout.LabelRole, self.item_name)

        self.item_quantity = QDoubleSpinBox(self.ui.scroll_area_container)
        self.item_quantity.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.item_quantity.setDecimals(0)
        self.item_quantity.setMaximum(item_quantity)
        self.item_quantity.setObjectName(f"item_{item_name}_quantity")
        self.item_quantity.setValue(0)
        self.ui.form_layout_item_list.setWidget(
            row_number, QFormLayout.FieldRole, self.item_quantity)
        
        self.item_rows.append({'name': item_name, 'price': item_price, 'quantity': item_quantity})
        self.item_quantity.valueChanged.connect(lambda: self.calculate_amount())

    def calculate_amount(self):
        all_items_price = 0
        for count, item in enumerate(self.get_form_data()):
            current_item_price = item['quantity'] * self.item_rows[count]['price']
            all_items_price += current_item_price
        self.ui.amountLineEdit.setValue(all_items_price)

    def chargebackDialog(self):
        self.ui = Ui_ChargebackTransactionDialog()
        self.ui.setupUi(self)

    def scanId(self, user_type, transaction_data):
        match user_type:
            case 'business':
                user = find_user_by_id(transaction_data['destination_id'])
                if hash(AUPCard().get_uid()) == user['card_id']:
                    self.ui.buttonScanBusiness.setEnabled(False)
                    self.ui.buttonScanBusiness.setText("Business Verified")
            case 'user':
                user = find_user_by_id(transaction_data['source_id'])
                if hash(AUPCard().get_uid()) == user['card_id']:
                    self.ui.buttonScanUser.setEnabled(False)
                    self.ui.buttonScanUser.setText("User Verified")
        self.chargeback_enable_checker()

    def chargeback_enable_checker(self):
        if not self.ui.buttonScanUser.isEnabled() and not self.ui.buttonScanBusiness.isEnabled() and self.ui.amountLineEdit.value() <= self.valid_amount:
            self.ui.buttonSave_addTransaction.setEnabled(True)
        else:
            self.ui.buttonSave_addTransaction.setEnabled(False)

    def chargeback(self, transaction_data):
        description = f"chargeback {transaction_data['_id']}"
        for item in self.get_form_data():
            if item['quantity'] > 0:
                self.chargebacked_items.append(item)
        for item in self.chargebacked_items:
            description = f"{description}\n{int(item['quantity'])} x {item['name']}"
        chargeback_transaction(self, transaction_data, description)
        self.close()


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
        self.ui.removeAllItemButton.clicked.connect(
            lambda: self.removeAllItems())
        self.ui.saveButton.clicked.connect(lambda: self.saveItems())
        self.ui.cancelButton.clicked.connect(lambda: self.close())
        load_inventory_to_table(self.ui.businessWindow_edit_dialog_table)
        self.ui.businessWindow_edit_dialog_table.itemSelectionChanged.connect(
            lambda: self.edit_dialog_selected_row())
        self.ui.moveUpButton.clicked.connect(lambda: self.move_row_up())
        self.ui.moveDownButton.clicked.connect(lambda: self.move_row_down())

        self.items = jsonIO.read_items()

    def addItem(self):
        new_item = {'name': self.ui.businessWindow_edit_dialog_nameLine.text(
        ), 'price': self.ui.businessWindow_edit_dialog_priceLine.text()}
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
                self.ui.businessWindow_edit_dialog_table.setItem(
                    row, column, item)
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
        update_item = {'name': self.ui.businessWindow_edit_dialog_nameLine.text(
        ), 'price': self.ui.businessWindow_edit_dialog_priceLine.text()}
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
                self.ui.businessWindow_edit_dialog_table.setItem(
                    row, column, item)
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
        msg_box.setText(
            f"Are you sure you want to delete the item '{item_name}'?")
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

    def removeAllItems(self):
        num_rows = self.ui.businessWindow_edit_dialog_table.rowCount()
        if num_rows == 0:
            return print("no items to remove")

        # Show the confirmation dialog
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Delete All Items")
        msg_box.setText(f"Are you sure you want to delete all items?")
        msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        msg_box.setIcon(QMessageBox.Warning)
        response = msg_box.exec()

        if response == QMessageBox.Ok:
            self.items.clear()
            self.ui.businessWindow_edit_dialog_table.setRowCount(0)
            print("All items removed")
            self.clear_field()
        else:
            print("Item removal cancelled")
        self.ui.businessWindow_edit_dialog_table.setCurrentItem(None)

    def saveItems(self):
        items_data = []
        for row in range(self.ui.businessWindow_edit_dialog_table.rowCount()):
            item_name = self.ui.businessWindow_edit_dialog_table.item(
                row, 1).text()
            item_price = self.ui.businessWindow_edit_dialog_table.item(
                row, 0).text()
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
                item = self.ui.businessWindow_edit_dialog_table.takeItem(
                    current_row, col)
                row_items.append(item)
            self.ui.businessWindow_edit_dialog_table.removeRow(current_row)
            self.ui.businessWindow_edit_dialog_table.insertRow(current_row - 1)
            for col, item in enumerate(row_items):
                self.ui.businessWindow_edit_dialog_table.setItem(
                    current_row - 1, col, item)
            # Update selection to moved row
            self.ui.businessWindow_edit_dialog_table.selectRow(current_row - 1)

    def move_row_down(self):
        current_row = self.ui.businessWindow_edit_dialog_table.currentRow()
        if current_row < self.ui.businessWindow_edit_dialog_table.rowCount() - 1:
            # Remove entire row and insert at row below
            row_items = []
            for col in range(self.ui.businessWindow_edit_dialog_table.columnCount()):
                item = self.ui.businessWindow_edit_dialog_table.takeItem(
                    current_row, col)
                row_items.append(item)
            self.ui.businessWindow_edit_dialog_table.removeRow(current_row)
            self.ui.businessWindow_edit_dialog_table.insertRow(current_row + 1)
            for col, item in enumerate(row_items):
                self.ui.businessWindow_edit_dialog_table.setItem(
                    current_row + 1, col, item)
            # Update selection to moved row
            self.ui.businessWindow_edit_dialog_table.selectRow(current_row + 1)


def open_edit_items_dialog(self, user):
    self.edit_items_dialog = EditItemsDialog()
    self.edit_items_dialog.ui.saveButton.clicked.connect(
        lambda: reload_inventory_table(self, user))
    self.edit_items_dialog.exec_()


def reload_inventory_table(self, user):
    load_inventory_to_table(self.businessWindow_inventory_table)
    self.businessWindow_inventory_table.setCurrentItem(None)
    self.businessWindow_descriptionLine.setText("")
    self.businessWindow_amountLine.setText("")


def add_to_cart(self: ProjectMainWindow):
    selectedItem = self.businessWindow_inventory_table.selectedItems()
    if selectedItem:
        row = selectedItem[0].row()
        self.businessWindow_cart_table.insertRow(
            self.businessWindow_cart_table.rowCount())
        for column in range(self.businessWindow_inventory_table.columnCount()):
            item = self.businessWindow_inventory_table.item(row, column)
            if item is not None:
                newItem = QTableWidgetItem(item.text())
                self.businessWindow_cart_table.setItem(
                    self.businessWindow_cart_table.rowCount()-1, column, newItem)
        self.businessWindow_inventory_table.setCurrentItem(None)
        print("added to cart")
        get_cart_data(self)


def get_cart_data(self: ProjectMainWindow):
    total_amount = 0
    description = ""

    # iterate over each row in the cart table
    for row in range(self.businessWindow_cart_table.rowCount()):
        item_price = self.businessWindow_cart_table.item(row, 0).text()
        item_name = self.businessWindow_cart_table.item(row, 1).text()
        item_quantity = 0

        total_amount += float(item_price)

        if description == "":
            description += f"{item_name},{item_price}"
        else:
            description += f"\n{item_name},{item_price}"

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
            item_price = self.businessWindow_inventory_table.item(
                row, 0).text()
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
                cart_table.setItem(
                    row_count, 0, QTableWidgetItem(str(item_price)))
            get_cart_data(self)


def clear_fields(self):
    self.businessWindow_amountLine.setText("")
    self.businessWindow_descriptionLine.setText("")
    self.businessWindow_cart_table.clearContents()
    self.businessWindow_cart_table.setRowCount(0)


def refresh_navbar(self: ProjectMainWindow, user):
    self.dateTo_business.setDate(QDate.currentDate())
    self.lineBalance_business.setText(str(user['balance']))
    self.lineBusiness_business.setText(user['school_id'])
    self.navLogout_business.clicked.connect(lambda: self.logoutAttempt())
    self.navHome_business.clicked.connect(
        lambda: self.stackedWidget_business.setCurrentIndex(0))
    self.navDashboard_business.clicked.connect(
        lambda: self.stackedWidget_business.setCurrentIndex(1))
    self.navAnalytics_business.clicked.connect(
        lambda: self.stackedWidget_business.setCurrentIndex(2))
    self.navTransactions_business.clicked.connect(
        lambda: self.stackedWidget_business.setCurrentIndex(3))


def refresh_analytics(self: ProjectMainWindow, user):
    item_frequency_pie_chart(
        self.businessWindow_transactions_table, self.graphicsView_business_1)
    transactions_count_per_month(
        self.businessWindow_transactions_table, self.graphicsView_business_2)
    transactions_total(self.businessWindow_transactions_table,
                       self.graphicsView_business_3)


def refresh_transactions(self: ProjectMainWindow, user):
    self.userWindow_transaction_search.setText("")
    setDateRangeFields.semestral(self.dateFrom_business, self.dateTo_business)
    self.comboBox_date_range_business.setCurrentText("Semestral")
    load_user_transaction_by_id(self.businessWindow_transactions_table, user)
    load_inventory_to_table(self.businessWindow_inventory_table)
    search_transactions_by_date(
        self.businessWindow_transactions_table, self.dateFrom_business, self.dateTo_business)
    refresh_analytics(self, user)


def date_changed(self: ProjectMainWindow, user):
    search_transactions_by_date(
        self.businessWindow_transactions_table, self.dateFrom_business, self.dateTo_business)
    refresh_analytics(self, user)


def range_changed(self: ProjectMainWindow, user):
    date_range = self.comboBox_date_range_business.currentText()
    if date_range == "Semestral":
        setDateRangeFields.semestral(
            self.dateFrom_business, self.dateTo_business)
    elif date_range == "Daily":
        setDateRangeFields.daily(self.dateFrom_business, self.dateTo_business)
    elif date_range == "Weekly":
        setDateRangeFields.weekly(self.dateFrom_business, self.dateTo_business)
    elif date_range == "Monthly":
        setDateRangeFields.monthly(
            self.dateFrom_business, self.dateTo_business)
    elif date_range == "All Time":
        setDateRangeFields.quadrennialy(
            self.dateFrom_business, self.dateTo_business)
        search_transactions("", self.businessWindow_transactions_table)
    refresh_analytics(self, user)


def search_changed(self: ProjectMainWindow, text, user):
    search_transactions(text, self.businessWindow_transactions_table)
    refresh_analytics(self, user)


def clearField(self: ProjectMainWindow, user):
    self.buttonClearTransactions_business.clicked.connect(lambda: clear_date(
        self.dateFrom_business, self.dateTo_business, self.businessWindow_transactions_table))
    search_transactions("", self.businessWindow_transactions_table)
    refresh_analytics(self, user)


def refresh_all(self: ProjectMainWindow, user):
    refresh_navbar(self, user)
    refresh_transactions(self, user)
    refresh_analytics(self, user)


def BusinessWindow(self: ProjectMainWindow, user):
    print(__name__)
    refresh_all(self, user)
    self.refreshButton_business.clicked.connect(
        lambda: refresh_all(self, user))
    self.businessWindow_transaction_search.textChanged.connect(
        lambda text: search_changed(self, text, user))
    self.dateFrom_business.dateChanged.connect(
        lambda: date_changed(self, user))
    self.dateTo_business.dateChanged.connect(lambda: date_changed(self, user))
    self.buttonClearTransactions_business.clicked.connect(
        lambda: refresh_transactions(self, user))
    self.exportCSV_business.clicked.connect(
        lambda: export_to_csv(self.businessWindow_transactions_table, user))

    # business
    self.buttonAddToCart_business.clicked.connect(lambda: add_to_cart(self))
    self.buttonRemoveFromCart_business.clicked.connect(
        lambda: remove_from_cart(self))
    self.buttonEditItems_business.clicked.connect(
        lambda: open_edit_items_dialog(self, user))
    self.buttonCharge.clicked.connect(lambda: charge(self, user))
    self.businessWindow_inventory_search.textChanged.connect(
        lambda text: search_inventory(self, text))
    self.keyPressEvent = (lambda event: add_item_shortcut(self, event))
    self.buttonChargeback_business.clicked.connect(
        lambda: chargebackTransaction(self))
    self.buttonClearFields_business.clicked.connect(lambda: clear_fields(self))
    self.comboBox_date_range_business.currentTextChanged.connect(
        lambda: range_changed(self, user))
    # self.businessWindow_transactions_table.selectionChanged(lambda selected: print(selected))
