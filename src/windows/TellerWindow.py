from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper.load_tables import *
from fnHelper.textSearch import *
from bson import *
from datetime import *
from dbHelper.add_transaction import add_transaction
from dbHelper.compute_user_balance import compute_user_balance
from fnHelper.transact import transact
from windows.ui.ui_OTPWithdrawalDialog import Ui_Dialog as Ui_OTPWithdrawalDialog

def selected_row_to_textbox(self):
    selected_row = self.tellerWindow_transactions_table.currentRow()
    school_id = self.tellerWindow_transactions_table.item(selected_row, 2)
    amount = self.tellerWindow_transactions_table.item(selected_row, 4)
    description = self.tellerWindow_transactions_table.item(selected_row, 5)
    if school_id and amount and description is not None:
        # put the data in the line edit/textbox
        self.tellerWindow_amountLine.setText(amount.text())
        self.tellerWindow_descriptionLine.setText(description.text())
def openOTPDialog(self, user): 
    self.OTPDialog = OTPWithdrawalDialog(user)
    self.OTPDialog.exec_()
class OTPWithdrawalDialog(QDialog):
    def __init__(self, user, parent=None):
        print(__name__)
        super(OTPWithdrawalDialog, self).__init__(parent)
        self.OTPDialog(user)
    def OTPDialog(self, user):
        self.ui = Ui_OTPWithdrawalDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(lambda: self.verifyOTP(self.ui.otp_Withdraw.text(), user))
        self.ui.buttonBox.rejected.connect(self.reject)
    def verifyOTP(self, OTP, user):
        transact(self, user, OTP)


def navbar(self, user):
    self.navHome_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(0))
    self.navDashboard_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(1))
    self.navAnalytics_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(2))
    self.navTransactions_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(3))
    

def TellerWindow(self, user):
    print(__name__)
    navbar(self, user)
    self.lineBalance_teller.setText(str(user['balance']))
    self.lineTeller_teller.setText(str(user['school_id']))
    # load_user_transaction_data(self)
    # testing school id only
    # load_transactions_to_table(self, self.tellerWindow_transactions_table)
    load_user_transaction_by_id(self.tellerWindow_transactions_table, user['_id'])
    load_bar_chart(self.tellerWindow_transactions_table, self.graphicsView_4)
    self.tellerWindow_transactions_table.itemSelectionChanged.connect(lambda: selected_row_to_textbox(self))
    self.tellerWindow_transaction_search.textChanged.connect(lambda text: search_transactions(self, text, self.tellerWindow_transactions_table))
    self.buttonTransact_teller.clicked.connect(lambda: transactAttempt(self, user))
    self.lineBalance_teller.setText(str(compute_user_balance(user['_id'])))
        
def transactAttempt(self, user):
    if not self.tellerWindow_amountLine.text() == "" and not self.tellerWindow_descriptionLine.toPlainText() == "":
        if(self.comboTransaction_teller.currentText() == "Withdraw"):
            openOTPDialog(self,user)
        elif(self.comboTransaction_teller.currentText() == "Deposit"):
            transact(self,user, OTP=None)


