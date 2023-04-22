from datetime import *
from PyQt5.QtChart import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.compute_user_balance import *
from dbHelper.find_transaction import *
from fnHelper import export_window_to_pdf, login, setDateRangeFields
from fnHelper.charts import (balance_line_chart, item_frequency_pie_chart,
                             total_spending_amount_chart,
                             transaction_amounts_chart,
                             transaction_breakdown_chart,
                             transaction_volume_bar_chart)
from fnHelper.export_to_csv import *
from fnHelper.load_tables import *
from fnHelper.refresh_clear import *
from fnHelper.textSearch import *
from windows.ProjectMainWindow import ProjectMainWindow


def refresh_navbar(self: ProjectMainWindow, user):
    self.userWindow_schoolIdLine.setText(user['school_id'])
    self.userWindow_balanceLine.setText(str(user['balance']))
    self.navHome_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(0))
    self.navAnalytics_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(1))
    self.navTransactions_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(2))


def refresh_analytics(self: ProjectMainWindow, user):
    item_frequency_pie_chart(self.userWindow_transactions_table, self.transaction_distribution_user)
    balance_line_chart(self.userWindow_transactions_table, self.balance_over_time_user)
    total_spending_amount_chart(self.userWindow_transactions_table, self.monthly_transaction_amount_user)
    transaction_volume_bar_chart(self.userWindow_transactions_table, self.transaction_breakdown_user)


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


def UserWindow(self: ProjectMainWindow, user):
    print(__name__)
    refresh_all(self, user)
    self.navRefresh_user.clicked.connect(lambda: refresh_all(self, user))
    self.userWindow_transaction_search.textChanged.connect(lambda text: searchChanged(self, user, text))
    self.dateFrom_user.dateChanged.connect(lambda: dateChanged(self, user))
    self.dateTo_user.dateChanged.connect(lambda: dateChanged(self, user))
    self.exportPDF_user.clicked.connect(lambda: export_window_to_pdf(self, user))
    self.exportCSV_user.clicked.connect(lambda: export_to_csv(self.userWindow_transactions_table, user))
    self.buttonClearTransactions_user.clicked.connect(lambda: refresh_transactions(self, user))
