from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper.load_tables import *
from fnHelper.textSearch import search_transactions
from bson import *
from datetime import *
from fnHelper.transact import transact
from windows.ui.ui_OTPWithdrawalDialog import Ui_Dialog as Ui_OTPWithdrawalDialog
from windows.ProjectMainWindow import ProjectMainWindow
from fnHelper.refresh_clear import clear_date
from dbHelper.find_user import find_user_by_id
from fnHelper.charts.total_amount_chart import total_amount_chart
from fnHelper.charts.total_withdrawal_and_deposit_chart import total_withdrawal_and_deposit_chart
from fnHelper.charts.transaction_frequency_chart import transaction_frequency
from fnHelper import export_window_to_pdf
from fnHelper.export_to_csv import *
from fnHelper.setDateRangeFields import weekly


def openOTPDialog(self: ProjectMainWindow, user): 
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


def navbar(self: ProjectMainWindow, user):
    self.lineBalance_teller.setText(str(user['balance']))
    self.lineTeller_teller.setText(str(user['school_id']))
    self.navLogout_teller.clicked.connect(lambda: self.logoutAttempt())
    self.navHome_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(0))
    self.navDashboard_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(1))
    self.navAnalytics_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(2))
    self.navTransactions_teller.clicked.connect(lambda: self.stackedWidget_teller.setCurrentIndex(3))

def analytics(self: ProjectMainWindow, user):
    total_amount_chart(self.tellerWindow_transactions_table, self.total_amount_teller, user)
    total_withdrawal_and_deposit_chart(self.tellerWindow_transactions_table, self.deposit_and_withdrawal_frequency_teller, user)
    transaction_frequency(self.tellerWindow_transactions_table, self.transaction_frequency_teller)

def transactions(self: ProjectMainWindow, user):
    weekly(self.dateFrom_teller, self.dateTo_teller)
    load_user_transaction_by_id(self.tellerWindow_transactions_table, user)
    

def dateChanged(self: ProjectMainWindow, user):
    search_transactions_by_date(self.tellerWindow_transactions_table, self.dateFrom_teller, self.dateTo_teller)
    analytics(self, user)

def refresh(self: ProjectMainWindow, user):
    navbar(self, user)
    transactions(self, user)
    analytics(self, user)


def TellerWindow(self: ProjectMainWindow, user):
    print(__name__)
    refresh(self, user)
    self.dateTo_teller.setDate(QDate.currentDate())
    self.tellerWindow_transaction_search.textChanged.connect(lambda text: search_transactions(text, self.tellerWindow_transactions_table))
    self.dateFrom_teller.dateChanged.connect(lambda: dateChanged(self, user))
    self.dateTo_teller.dateChanged.connect(lambda: dateChanged(self, user))
    self.buttonClearTransactions_teller.clicked.connect(lambda: clear_date(self.dateFrom_teller, self.dateTo_teller, self.tellerWindow_transactions_table))
    self.buttonTransact_teller.clicked.connect(lambda: transactAttempt(self, user))
    self.refreshButton_teller.clicked.connect(lambda: refresh(self, user))
    self.exportToCSVButton_teller.clicked.connect(lambda: export_to_csv(self.tellerWindow_transactions_table, user))
    
def transactAttempt(self: ProjectMainWindow, user):
    if not self.tellerWindow_amountLine.text() == "" and not self.tellerWindow_descriptionLine.toPlainText() == "":
        if(self.comboTransaction_teller.currentText() == "Withdraw"):
            openOTPDialog(self,user)
        elif(self.comboTransaction_teller.currentText() == "Deposit"):
            transact(self,user)


