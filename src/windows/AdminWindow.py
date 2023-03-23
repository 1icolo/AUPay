from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper import add_user, find_user_by_id, update_user, delete_user
from fnHelper import get_random_secret, get_totp, verify_otp, load_users_to_table, load_transactions_to_table
from windows.ui.ui_AddUserDialog import Ui_Dialog as AddUserUi_Dialog
from windows.ui.ui_EditUserDialog import Ui_Dialog as EditUserUi_Dialog
from windows.ui.ui_DeleteUserDialog import Ui_Dialog as DeleteUserUi_Dialog
from bson import ObjectId

def editUser(self):
    selected_row = self.adminWindow_users_table.currentRow()
    id = ObjectId(self.adminWindow_users_table.item(selected_row, 0).text())
    current_user_data = find_user_by_id(id)
    edit_dialog = EditUserDialog(id)
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
    selected_row = self.tableUsers_administrator.currentRow()
    id = self.tableUsers_administrator.item(selected_row, 0).text()
    delete_dialog = DeleteUserDialog(id)
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
    def __init__(self, id, parent=None):
        super(EditUserDialog, self).__init__(parent)
        self.ui = EditUserUi_Dialog()
        self.ui.setupUi(self)
        idValidator = QIntValidator()
        idValidator.setRange(0, 100000)
        self.ui.buttonSave_editUser.clicked.connect(lambda: self.updateUser(id))
        self.ui.buttonCancel_editUser.clicked.connect(lambda: self.close())
        self.ui.buttonGenerate_editUser.clicked.connect(lambda: self.ui.otpSecret_editUser.setText(self.generateOTPSecret()))
    def updateUser(self, id):
        totp = get_totp(self.ui.otpSecret_editUser.text())
        if(verify_otp(totp, self.ui.otp_editUser.text())):
            userData = {
                '_id': ObjectId(id),
                'card_id': self.ui.cardID_editUser.text(),
                'school_id': self.ui.schoolID_editUser.text(),
                'password': self.ui.password_editUser.text(),
                'otp_key': self.ui.otp_editUser.text(),
                'user_type': self.ui.userType_editUser.currentText().lower(),
            }
            update_user(userData)
        update_user(userData)
    def generateOTPSecret(self):
        newSecret = get_random_secret()
        print(get_totp(newSecret).now())
        return newSecret     
class DeleteUserDialog(QDialog):
    def __init__(self, id, parent=None):
        super(DeleteUserDialog, self).__init__(parent)
        self.ui = DeleteUserUi_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonDelete_deleteUser.clicked.connect(lambda: self.deleteUser(id))
        self.ui.buttonCancel_deleteUser.clicked.connect(lambda: self.close())
    def deleteUser(self, id):
        delete_user(ObjectId(id))

def AdminWindow(self):
    print(__name__)
    self.buttonAddUser_administrator.clicked.connect(lambda: AddUserDialog().exec())
    self.buttonEditUser_administrator.clicked.connect(lambda: editUser(self))
    self.buttonDeleteUser_administrator.clicked.connect(lambda: deleteUser(self))
    load_users_to_table(self, self.adminWindow_users_table)
    load_transactions_to_table(self, self.adminWindow_transactions_table)

    