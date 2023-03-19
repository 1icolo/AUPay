from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.add_user import add_user
from dbHelper.find_user import load_user_data
from dbHelper.find_transaction import load_transaction_table
from windows.ui.ui_AddUserDialog import Ui_Dialog

def load_users_to_table(self):
    users_data = load_user_data(self)
    # print(data)
    rows = len(users_data)
    columns = len(users_data[0])
    self.tableUsers_administrator.setRowCount(len(users_data))
    self.tableUsers_administrator.hideColumn(0)
    # print(data[school_id])
    # Add the user data to the table
    for row in range(rows):
        for column in range(columns):
            item = QTableWidgetItem(str(users_data[row][column]))
            self.tableUsers_administrator.setItem(row, column, item)
    self.tableUsers_administrator.itemSelectionChanged.connect(lambda: id_of_selected_row_user(self))

    def id_of_selected_row_user(self):
        selected_row = self.tableUsers_administrator.currentRow()
        _id = self.tableUsers_administrator.item(selected_row, 0).text()
        print(_id)

def load_transactions_to_table(self):
    transactions_data = load_transaction_table(self)
    # print(transactions_data)
    rows = len(transactions_data)
    columns = len(transactions_data[0])
    self.transactionsTable_administrator.setRowCount(len(transactions_data))
    # Add the user data to the table
    for row in range(rows):
        for column in range(columns):
            item = QTableWidgetItem(str(transactions_data[row][column]))
            self.transactionsTable_administrator.setItem(row, column, item)
    self.transactionsTable_administrator.itemSelectionChanged.connect(lambda: id_of_selected_row_transaction(self))

    def id_of_selected_row_transaction(self):
        selected_row = self.transactionsTable_administrator.currentRow()
        _id = self.transactionsTable_administrator.item(selected_row, 0).text()
        print(_id)


class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super(AddUserDialog, self).__init__(parent)
        self.addUserDialog()

    def addUserDialog(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonSave_addUser.clicked.connect(lambda: self.addUser())
        self.ui.buttonCancel_addUser.clicked.connect(lambda: self.close())

    def addUser(self):
        newUser = {
            'card_id': self.ui.cardID_addUser.text(),
            'school_id': self.ui.schoolID_addUser.text(),
            'password': self.ui.password_addUser.text(),
            'otp_key': "",
            'user_type': self.ui.userType_addUser.currentText().lower(),
            'balance': self.ui.balance_addUser.text(),
        }
        add_user(newUser)


def AdminWindow(self):
    print(__name__)
    self.buttonAddUser_administrator.clicked.connect(lambda: AddUserDialog().exec())
    load_users_to_table(self)
    load_transactions_to_table(self)

    