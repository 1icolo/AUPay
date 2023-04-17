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
from fnHelper.refresh_clear import *
from dbHelper.find_user import *

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
    self.OTPDialog = OTPWithdrawalDialog(self, user)
    self.OTPDialog.exec_()
class OTPWithdrawalDialog(QDialog):
    def __init__(self, ProjectMainWindow, user, parent=None):
        print(__name__)
        super(OTPWithdrawalDialog, self).__init__(parent)
        self.OTPDialog(ProjectMainWindow, user)
    def OTPDialog(self, ProjectMainWindow, user):
        self.ui = Ui_OTPWithdrawalDialog()
        self.ui.setupUi(self)
        self.ui.otp_Withdraw.setValidator(QIntValidator())
        self.ui.buttonBox.accepted.connect(lambda: self.verifyOTP(ProjectMainWindow, self.ui.otp_Withdraw.text(), user))
        self.ui.buttonBox.rejected.connect(self.reject)
    def verifyOTP(self, ProjectMainWindow, OTP, user):
        transact(ProjectMainWindow, user, OTP)


def navbar(self, user):
    self.navHome_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(0))
    self.navDashboard_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(1))
    self.navAnalytics_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(2))
    self.navTransactions_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(3))
    

def TellerWindow(self, user):
    print(__name__)
    navbar(self, user)
    # Reload the balance
    teller = find_user_by_id(user['_id'])
    balance = teller['balance']
    self.lineBalance_teller.setText(str(balance))
    # self.lineBalance_teller.setText(str(user['balance']))
    self.lineTeller_teller.setText(str(user['school_id']))
    self.dateTo_teller.setDate(QDate.currentDate())
    # load_user_transaction_data(self)
    # testing school id only
    # load_transactions_to_table(self, self.tellerWindow_transactions_table)
    load_user_transaction_by_id(self.tellerWindow_transactions_table, user['_id'])
    load_bar_chart(self.tellerWindow_transactions_table, self.graphicsView_4)
    self.tellerWindow_transactions_table.itemSelectionChanged.connect(lambda: selected_row_to_textbox(self))
    self.tellerWindow_transaction_search.textChanged.connect(lambda text: search_transactions(text, self.tellerWindow_transactions_table))
    self.dateFrom_teller.dateChanged.connect(lambda: search_transactions_by_date(self.tellerWindow_transactions_table, self.dateFrom_teller, self.dateTo_teller))
    self.dateTo_teller.dateChanged.connect(lambda: search_transactions_by_date(self.tellerWindow_transactions_table, self.dateFrom_teller, self.dateTo_teller))
    self.buttonClearTransactions_teller.clicked.connect(lambda: clear_date(self.dateFrom_teller, self.dateTo_teller))
    self.buttonTransact_teller.clicked.connect(lambda: transactAttempt(self, user))
    self.lineBalance_teller.setText(str(compute_user_balance(user['_id'])))
        
def transactAttempt(self, user):
    if not self.tellerWindow_amountLine.text() == "" and not self.tellerWindow_descriptionLine.toPlainText() == "":
        if(self.comboTransaction_teller.currentText() == "Withdraw"):
            openOTPDialog(self,user)
        elif(self.comboTransaction_teller.currentText() == "Deposit"):
            transact(self,user, OTP=None)


