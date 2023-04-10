from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper import add_user, find_user_by_id, update_user, delete_user, add_transaction
from fnHelper import get_random_secret, get_totp, verify_otp
from fnHelper.load_tables import *
from windows.ui.ui_AddUserDialog import Ui_Dialog as AddUserUi_Dialog
from windows.ui.ui_EditUserDialog import Ui_Dialog as EditUserUi_Dialog
from windows.ui.ui_DeleteUserDialog import Ui_Dialog as DeleteUserUi_Dialog
from windows.ui.ui_AddTransactionDialog import Ui_Dialog as AddTransaction_Dialog
from bson import ObjectId, Timestamp
from fnHelper.aupCard import AUPCard
from fnHelper import hashEncryption
from datetime import *
from fnHelper.textSearch import *
from fnHelper.export_to_csv import *
from dbHelper.calculate_total_circulating_supply import calculate_total_circulating_supply
from fnHelper.refresh_clear import *


def editUser(self):
    selected_row = self.adminWindow_users_table.currentRow()
    item = self.adminWindow_users_table.item(selected_row, 0)
    if item is None:
        return print("select row to edit")
    id = ObjectId(self.adminWindow_users_table.item(selected_row, 0).text())
    current_user_data = find_user_by_id(id)
    edit_dialog = EditUserDialog(id)
    edit_dialog.table_updated.connect(lambda: load_users_to_table(self, self.adminWindow_users_table))
    edit_dialog.ui.cardID_editUser.setText(current_user_data['card_id'])
    edit_dialog.ui.schoolID_editUser.setText(current_user_data['school_id'])
    edit_dialog.ui.otpSecret_editUser.setText(current_user_data['otp_key'])
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
    selected_row = self.adminWindow_users_table.currentRow()
    item = self.adminWindow_users_table.item(selected_row, 0)
    if item is None:
        return print("select row to delete")
    id = self.adminWindow_users_table.item(selected_row, 0).text()
    delete_dialog = DeleteUserDialog(id)
    delete_dialog.table_updated.connect(lambda: load_users_to_table(self, self.adminWindow_users_table))
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
        self.ui.otpt_addUser.textChanged.connect(lambda: self.verifyOTP(self.ui.secret_addUser.text()))

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

    def verifyOTP(self, otpSecret):
        totp = get_totp(otpSecret)
        if(verify_otp(totp, self.ui.otpt_addUser.text())):
            self.ui.buttonSave_addUser.setEnabled(True)
        else:
            self.ui.buttonSave_addUser.setEnabled(False)

def open_add_user_dialog(self):
    # Check if there is a selected row
    selected_items = self.adminWindow_users_table.selectedItems()
    if selected_items:
        # Clear the selection
        self.adminWindow_users_table.clearSelection()
    self.add_user_dialog = AddUserDialog()
    self.add_user_dialog.ui.buttonSave_addUser.clicked.connect(lambda: reload_users_table(self))
    self.add_user_dialog.exec_()
    
def reload_users_table(self):
    load_users_to_table(self, self.adminWindow_users_table)
    self.adminWindow_users_table.setCurrentItem(None)
    self.adminWindow_user_search.setText("")
    
def addTransaction(self):
    AddTransactionDialog().exec()
class EditUserDialog(QDialog):
    table_updated = pyqtSignal()
    def __init__(self, id, parent=None):
        super(EditUserDialog, self).__init__(parent)
        self.ui = EditUserUi_Dialog()
        self.ui.setupUi(self)
        idValidator = QIntValidator()
        idValidator.setRange(0, 100000)
        # self.ui.buttonSave_editUser.setEnabled(False)
        self.ui.buttonSave_editUser.clicked.connect(lambda: self.updateUser(id))
        self.ui.buttonCancel_editUser.clicked.connect(lambda: self.close())
        self.ui.buttonGenerate_editUser.clicked.connect(lambda: self.ui.otpSecret_editUser.setText(self.generateOTPSecret()))
        self.ui.otp_editUser.textChanged.connect(lambda: self.verifyOTP(self.ui.otpSecret_editUser.text()))
        self.ui.buttonScanID_editUser.clicked.connect(lambda: self.scanId())
        self.oldCardId = self.ui
        

    def scanId(self):
        self.ui.cardID_editUser.setEnabled(True)
        self.ui.cardID_editUser.setText(AUPCard().get_uid())
        
    def updateUser(self, id):
            userData = {
                '_id': ObjectId(id),
                'card_id': (lambda: self.ui.cardID_editUser.text(), lambda: hashEncryption.encrypt(self.ui.cardID_editUser.text()))[self.ui.cardID_editUser.isEnabled()](),
                'school_id': self.ui.schoolID_editUser.text(),
                'password': hashEncryption.encrypt(self.ui.password_editUser.text()),
                'otp_key': (lambda: self.ui.otpSecret_editUser.text(), lambda: hashEncryption.encrypt(self.ui.otpSecret_editUser.text()))[self.ui.otpSecret_editUser.isEnabled()](),
                'user_type': self.ui.userType_editUser.currentText().lower(),
            }
            update_user(userData)
            self.table_updated.emit()
            self.close()
            
    def verifyOTP(self, otpSecret):
        totp = get_totp(otpSecret)
        if(verify_otp(totp, self.ui.otp_editUser.text())):
            self.ui.buttonSave_editUser.setEnabled(True)
        else:
            self.ui.buttonSave_editUser.setEnabled(False)

    def generateOTPSecret(self):
        newSecret = get_random_secret()
        self.totp = get_totp(self.ui.otpSecret_editUser.text())
        self.ui.otpSecret_editUser.setEnabled(True)
        self.ui.buttonSave_editUser.setEnabled(False)
        self.ui.otp_editUser.setEnabled(True)
        return newSecret

class DeleteUserDialog(QDialog):
    table_updated = pyqtSignal()
    def __init__(self, id, parent=None):
        super(DeleteUserDialog, self).__init__(parent)
        self.ui = DeleteUserUi_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonDelete_deleteUser.clicked.connect(lambda: self.deleteUser(id))
        self.ui.buttonCancel_deleteUser.clicked.connect(lambda: self.close())
    def deleteUser(self, id):
        delete_user(ObjectId(id))
        self.table_updated.emit()
        
        self.close()
class AddTransactionDialog(QDialog):
    table_updated = pyqtSignal()
    def __init__(self, user, parent=None):
        super(AddTransactionDialog, self).__init__(parent)
        self.ui = AddTransaction_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonSave_addTransaction.clicked.connect(lambda: self.addTransaction(user))
        self.ui.buttonCancel_addTransaction.clicked.connect(lambda: self.close())
        self.ui.adminWindow_addTransactionSourceId.setText('ffffffffffffffffffffffff') # coinbase id
        self.ui.buttonEditSourceID.clicked.connect(lambda: self.ui.adminWindow_addTransactionSourceId.setReadOnly(False))

    def addTransaction(self, user):
        newTransaction =  {
            "timestamp": Timestamp(int(datetime.today().timestamp()), 1),
            "source_id": ObjectId(self.ui.adminWindow_addTransactionSourceId.text()),
            "destination_id": ObjectId(self.ui.adminWindow_addDestinationId.text()),
            "amount": float(self.ui.adminWindow_addTransactionAmount.text()),
            "description": self.ui.adminWindow_addTransactionDescription.text()
        }
        add_transaction(newTransaction)
        self.table_updated.emit()
        self.close()

def open_add_transaction_dialog(self, user):
    # Check if there is a selected row
    selected_items = self.adminWindow_transactions_table.selectedItems()
    if selected_items:
        # Clear the selection
        self.adminWindow_transactions_table.clearSelection()
    self.add_transaction_dialog = AddTransactionDialog(user)
    self.add_transaction_dialog.ui.buttonSave_addTransaction.clicked.connect(lambda: reload_transactions_table(self, user))
    self.add_transaction_dialog.exec_()
    
def reload_transactions_table(self, user):
    load_transactions_to_table(self, self.adminWindow_transactions_table, user)
    refresh_bar_chart(self.adminWindow_transactions_table, self.graphicsView_3)
    self.adminWindow_transactions_table.setCurrentItem(None)
    self.adminWindow_transaction_search.setText("")


def AdminWindow(self, user):
    print(__name__)
    self.buttonAddUser_administrator.clicked.connect(lambda: open_add_user_dialog(self))
    self.buttonEditUser_administrator.clicked.connect(lambda: editUser(self))
    self.buttonDeleteUser_administrator.clicked.connect(lambda: deleteUser(self))
    self.buttonAddTransaction_administrator.clicked.connect(lambda: open_add_transaction_dialog(self, user))
    load_users_to_table(self, self.adminWindow_users_table)
    load_transactions_to_table(self, self.adminWindow_transactions_table, user)
    self.adminWindow_user_search.textChanged.connect(lambda text: search_users(text, self.adminWindow_users_table))
    self.adminWindow_transaction_search.textChanged.connect(lambda text: search_transactions(self, text, self.adminWindow_transactions_table))
    load_bar_chart(self.adminWindow_transactions_table, self.graphicsView_3)
    self.dateFrom_administrator.dateChanged.connect(lambda: search_transactions_by_date(self.adminWindow_transactions_table, self.dateFrom_administrator, self.dateTo_administrator))
    self.dateTo_administrator.dateChanged.connect(lambda: search_transactions_by_date(self.adminWindow_transactions_table, self.dateFrom_administrator, self.dateTo_administrator))
    self.export_administrator.clicked.connect(lambda: export_chart_to_csv(self.adminWindow_transactions_table, f"{user['school_id']}_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.csv"))
    self.buttonClearTransactions_administrator.clicked.connect(lambda: clear_date(self.dateFrom_administrator, self.dateTo_administrator))
    self.lineTotalCirculating_administrator.setText(str(calculate_total_circulating_supply()))
    






