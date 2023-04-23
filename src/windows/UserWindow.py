from datetime import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.compute_user_balance import *
from dbHelper.find_transaction import *
from fnHelper import cryptography, export_window_to_pdf, setDateRangeFields
from fnHelper.charts import (balance_line_chart, 
                             item_frequency_pie_chart,
                             total_spending_amount_chart,
                             top_spending_destinations_chart)
from fnHelper.export_to_csv import *
from fnHelper.load_tables import *
from fnHelper.refresh_clear import *
from fnHelper.textSearch import *
from windows.ProjectMainWindow import ProjectMainWindow
from windows.ui.ui_ChangePasswordDialog import Ui_Dialog as ChangePasswordUi_Dialog
from windows.ui.ui_ChangeOTPDialog import Ui_Dialog as ChangeOTPUi_Dialog
from fnHelper.otpAuth import *
import os
from fnHelper import update_user


class ChangePasswordDialog(QDialog):
    def __init__(self, user, parent=None):
        super(ChangePasswordDialog, self).__init__(parent)
        self.ui = ChangePasswordUi_Dialog()
        self.ui.setupUi(self)
        self.ui.button_change_password.clicked.connect(lambda: self.change_password(user))
        if user['password'] == cryptography.hash('Shine On, Dear AUP!'):
            self.ui.line_old_password.setHidden(True)

    def change_password(self, user):
        if self.ui.line_new_password.text() != "" and self.ui.line_confirm_password.text() != "":
            if user['password'] == cryptography.hash(self.ui.line_old_password.text()) or user['password'] == cryptography.hash('Shine On, Dear AUP!'):
                if self.ui.line_new_password.text() == self.ui.line_confirm_password.text():
                    userData = {
                        '_id': ObjectId(user['_id']),
                        'card_id': user['card_id'],
                        'school_id': user['school_id'],
                        'password': cryptography.hash(self.ui.line_confirm_password.text()),
                        'otp_key': user['otp_key'],
                        'user_type': user['user_type'],
                    }
                    update_user(userData)
                    QMessageBox.information(self, "Success", f"Password Changed")
                    self.close()
                else:
                    QMessageBox.warning(self, "Warning", "New password must be the same with the confirmation")
            else:
                QMessageBox.warning(self, "Warning", "Old password is incorrect")
        else:
            QMessageBox.warning(self, "Warning", "All fields are required")

class ChangeOTPDialog(QDialog):
    def __init__(self, user, parent=None):
        super(ChangeOTPDialog, self).__init__(parent)
        self.ui = ChangeOTPUi_Dialog()
        self.ui.setupUi(self)
        self.generate(user)
        self.ui.button_confirm_otp.clicked.connect(lambda: self.change_otp(user))

    def generate(self, user):
        self.secret_key = get_random_secret()
        self.totp = get_totp(self.secret_key)
        # self.ui.qrcodeimg.setPixmap(QPixmap(generate_qr(self.secret_key, user['school_id'])))
        generate_qr(self.secret_key, user['school_id'])
        self.ui.qrcodeimg.setPixmap(QPixmap('qr_code.png'))
        os.remove('qr_code.png')

    def change_otp(self, user):
        verification_otp = verify_otp(self.totp, self.ui.line_otp.text())
        verification_password = user['password'] == cryptography.hash(self.ui.line_password.text())
        if verification_otp and verification_password:
            userData = {
                        '_id': ObjectId(user['_id']),
                        'card_id': user['card_id'],
                        'school_id': user['school_id'],
                        'password': user['password'],
                        'otp_key': self.secret_key,
                        'user_type': user['user_type'],
                    }
            update_user(userData)
            QMessageBox.information(self, "Success", "OTP updated")
            self.close()
        else:
            QMessageBox.warning(self, "Warning", "Password or OTP is incorrect")

def refresh_navbar(self: ProjectMainWindow, user):
    self.userWindow_schoolIdLine.setText(user['school_id'])
    self.userWindow_balanceLine.setText(str(user['balance']))
    self.navHome_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(0))
    self.navAnalytics_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(1))
    self.navTransactions_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(2))
    self.navAccount_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(3))


def refresh_analytics(self: ProjectMainWindow, user):
    item_frequency_pie_chart(self.userWindow_transactions_table, self.transaction_distribution_user)
    balance_line_chart(self.userWindow_transactions_table, self.balance_over_time_user)
    total_spending_amount_chart(self.userWindow_transactions_table, self.monthly_transaction_amount_user)
    top_spending_destinations_chart(self.userWindow_transactions_table, self.transaction_breakdown_user, user)


def refresh_transactions(self: ProjectMainWindow, user):
    load_user_transaction_by_id(self.userWindow_transactions_table, user)
    setDateRangeFields(self.dateFrom_user, self.dateTo_user)
    self.userWindow_transaction_search.setText("")


def dateChanged(self: ProjectMainWindow, user):
    search_transactions_by_date(self.userWindow_transactions_table, self.dateFrom_user, self.dateTo_user)
    refresh_analytics(self, user)


def searchChanged(self: ProjectMainWindow, user, text):
    search_transactions(text, self.userWindow_transactions_table)
    refresh_analytics(self, user)


def refresh_all(self: ProjectMainWindow, user):
    refresh_navbar(self, user)
    refresh_transactions(self, user)
    refresh_analytics(self, user)

def check_otp_and_password(self: ProjectMainWindow, user):
    if not user['password'] == cryptography.hash('Shine On, Dear AUP!'):
        self.password_status_client.setText("Already Set")
    if not user['otp_key'] == "":
        self.secret_status_client.setText("Already Set")


def UserWindow(self: ProjectMainWindow, user):
    print(__name__)
    refresh_all(self, user)
    check_otp_and_password(self, user)
    self.navRefresh_user.clicked.connect(lambda: refresh_all(self, user))
    self.userWindow_transaction_search.textChanged.connect(lambda text: searchChanged(self, user, text))
    self.dateFrom_user.dateChanged.connect(lambda: dateChanged(self, user))
    self.dateTo_user.dateChanged.connect(lambda: dateChanged(self, user))
    self.exportPDF_user.clicked.connect(lambda: export_window_to_pdf(self, user))
    self.exportCSV_user.clicked.connect(lambda: export_to_csv(self.userWindow_transactions_table, user))
    self.buttonClearTransactions_user.clicked.connect(lambda: refresh_transactions(self, user))
    self.change_password_client.clicked.connect(lambda: ChangePasswordDialog(user).exec())
    self.change_otp_client.clicked.connect(lambda: ChangeOTPDialog(user).exec())
