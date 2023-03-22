from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper import load_user_data, find_user_by_id, update_user, load_transaction_table, add_user, delete_user
from fnHelper import get_random_secret, verify_otp, get_totp
from windows.ui.ui_AddUserDialog import Ui_Dialog as AddUserUi_Dialog
from windows.ui.ui_EditUserDialog import Ui_Dialog as EditUserUi_Dialog
from windows.ui.ui_DeleteUserDialog import Ui_Dialog as DeleteUserUi_Dialog
from bson import ObjectId
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
            self.tableUsers_administrator.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    self.tableUsers_administrator.itemSelectionChanged.connect(lambda: id_of_selected_row(self))
def id_of_selected_row(self):
    selected_items = self.tableUsers_administrator.selectedItems()
    if selected_items:
        selected_row = selected_items[0].row()
        selected_row_data = {
            "_id": self.tableUsers_administrator.item(selected_row, 0).text()
        }
        self.buttonEditUser_administrator.setEnabled(True)
        self.buttonDeleteUser_administrator.setEnabled(True)
        return selected_row_data

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
            self.transactionsTable_administrator.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    # self.transactionsTable_administrator.itemSelectionChanged.connect(lambda: id_of_selected_row(self))
def editUser(self):
    selected_row = self.tableUsers_administrator.currentRow()
    id = ObjectId(self.tableUsers_administrator.item(selected_row, 0).text())
    current_user_data = find_user_by_id(id)
    edit_dialog = EditUserDialog()
    edit_dialog.ui._id_editUser.setText(self.tableUsers_administrator.item(selected_row, 0).text())
    edit_dialog.ui.cardID_editUser.setText(current_user_data['card_id'])
    edit_dialog.ui.schoolID_editUser.setText(current_user_data['school_id'])
    edit_dialog.ui.password_editUser.setText(current_user_data['password'])
    def current_user_type(user_type):
        if user_type == 'user':
            return "User"
        elif user_type == 'admin':
            return "Admin"
        elif user_type == 'business':
            return "Business"
        elif user_type == 'teller':
            return "Teller"
    edit_dialog.ui.userType_editUser.setCurrentText(current_user_type(current_user_data['user_type']))
    edit_dialog.exec()
def deleteUser(self):
    delete_dialog = DeleteUserDialog()
    selected_row = self.tableUsers_administrator.currentRow()
    id = self.tableUsers_administrator.item(selected_row, 0).text()
    delete_dialog.ui._id_deleteUser.setText(id)
    delete_dialog.exec()
class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super(AddUserDialog, self).__init__(parent)
        self.addUserDialog()

    def addUserDialog(self):
        self.ui = AddUserUi_Dialog()
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
class EditUserDialog(QDialog):
    def __init__(self, parent=None):
        super(EditUserDialog, self).__init__(parent)
        self.ui = EditUserUi_Dialog()
        self.ui.setupUi(self)
        idValidator = QIntValidator()
        idValidator.setRange(0, 100000)
        self.ui._id_editUser.hide()
        self.ui.buttonSave_editUser.clicked.connect(lambda: self.updateUser())
        self.ui.buttonCancel_editUser.clicked.connect(lambda: self.close())
        self.ui.buttonGenerate_editUser.clicked.connect(lambda: self.ui.otpSecret_editUser.setText(self.generateOTPSecret()))
    def updateUser(self):
        totp = get_totp(self.ui.otpSecret_editUser.text())
        if(verify_otp(totp, self.ui.otp_editUser.text())):
            userData = {
                '_id': ObjectId(self.ui._id_editUser.text()),
                'card_id': self.ui.cardID_editUser.text(),
                'school_id': self.ui.schoolID_editUser.text(),
                'password': self.ui.password_editUser.text(),
                'otp_key': self.ui.otp_editUser.text(),
                'user_type': self.ui.userType_editUser.currentText().lower(),
            }
            update_user(userData)
    def generateOTPSecret(self):
        newSecret = get_random_secret()
        print(get_totp(newSecret).now())
        return newSecret     
class DeleteUserDialog(QDialog):
    def __init__(self, parent=None):
        super(DeleteUserDialog, self).__init__(parent)
        self.ui = DeleteUserUi_Dialog()
        self.ui.setupUi(self)
        self.ui._id_deleteUser.hide()
        self.ui.buttonDelete_deleteUser.clicked.connect(lambda: self.deleteUser())
        self.ui.buttonCancel_deleteUser.clicked.connect(lambda: self.close())
    def deleteUser(self):
        id = ObjectId(self.ui._id_deleteUser.text())
        delete_user(id)

def AdminWindow(self):
    print(__name__)
    self.buttonEditUser_administrator.setEnabled(False)
    self.buttonDeleteUser_administrator.setEnabled(False)
    self.buttonAddUser_administrator.clicked.connect(lambda: AddUserDialog().exec())
    self.buttonEditUser_administrator.clicked.connect(lambda: editUser(self))
    self.buttonDeleteUser_administrator.clicked.connect(lambda: deleteUser(self))   
    load_users_to_table(self)
    load_transactions_to_table(self)
