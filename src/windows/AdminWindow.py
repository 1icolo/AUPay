from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper import add_user, find_user_by_id, update_user, delete_user
from fnHelper import get_random_secret, get_totp, verify_otp, load_users_to_table, load_transactions_to_table
from windows.ui.ui_AddUserDialog import Ui_Dialog as AddUserUi_Dialog
from windows.ui.ui_EditUserDialog import Ui_Dialog as EditUserUi_Dialog
from windows.ui.ui_DeleteUserDialog import Ui_Dialog as DeleteUserUi_Dialog
from bson import ObjectId
from fnHelper.aupCard import AUPCard
from fnHelper import hashEncryption

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
        self.ui.buttonSave_addUser.clicked.connect(lambda: self.saveButton())
        self.ui.buttonCancel_addUser.clicked.connect(lambda: self.close())
        self.ui.buttonScanId_addUser.clicked.connect(lambda: self.scanID())
        self.ui.secret_addUser.setText(get_random_secret())
        self.totp = get_totp(self.ui.secret_addUser.text())

    def scanID(self):
        self.ui.cardID_addUser.setText(AUPCard().get_uid())

    def checkFields(self):
        # paki check lahat ng fields if may laman 
        if not verify_otp(self.totp, self.ui.otpt_addUser.text()):
            print("Invalid OTP")
            return False
        return True

    def saveButton(self):
        newUser = {
            'card_id': hashEncryption.encrypt(self.ui.cardID_addUser.text()),
            'school_id': self.ui.schoolID_addUser.text(),
            'password': hashEncryption.encrypt(self.ui.password_addUser.text()),
            'otp_key': hashEncryption.encrypt(self.ui.secret_addUser.text()),
            'user_type': self.ui.userType_addUser.currentText().lower(),
            'balance': 0.00,
        }
        if self.checkFields():
            add_user(newUser)
            self.close()

class EditUserDialog(QDialog):
    def __init__(self, id, parent=None):
        super(EditUserDialog, self).__init__(parent)
        self.ui = EditUserUi_Dialog()
        self.ui.setupUi(self)
        idValidator = QIntValidator()
        idValidator.setRange(0, 100000)
        self.ui.buttonSave_editUser.setEnabled(False)
        self.ui.buttonSave_editUser.clicked.connect(lambda: self.updateUser(id))
        self.ui.buttonCancel_editUser.clicked.connect(lambda: self.close())
        self.ui.buttonGenerate_editUser.clicked.connect(lambda: self.ui.otpSecret_editUser.setText(self.generateOTPSecret()))
        self.ui.otp_editUser.textChanged.connect(lambda: self.verifyOTP(self.ui.otpSecret_editUser.text()))
    def updateUser(self, id):
            userData = {
                '_id': ObjectId(id),
                'card_id': self.ui.cardID_editUser.text(),
                'school_id': self.ui.schoolID_editUser.text(),
                'password': self.ui.password_editUser.text(),
                'otp_key': self.ui.otp_editUser.text(),
                'user_type': self.ui.userType_editUser.currentText().lower(),
            }
            update_user(userData)
    def verifyOTP(self, otpSecret):
        totp = get_totp(otpSecret)
        if(verify_otp(totp, self.ui.otp_editUser.text())):
            self.ui.buttonSave_editUser.setEnabled(True)
        else:
            self.ui.buttonSave_editUser.setEnabled(False)
    def generateOTPSecret(self):
        newSecret = get_random_secret()
        # print(get_totp(newSecret).now())
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

    