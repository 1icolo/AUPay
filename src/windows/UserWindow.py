from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from fnHelper import login
from fnHelper.load_tables import *
from fnHelper.textSearch import *
from dbHelper.compute_user_balance import *
from dbHelper.find_transaction import *
from datetime import *
from fnHelper.export_to_csv import *
from fnHelper.refresh_clear import *
from fnHelper.charts import item_frequency_pie_chart
from windows.ProjectMainWindow import ProjectMainWindow
from fnHelper import export_window_to_pdf
from fnHelper.charts import balance_line_chart, transaction_breakdown_chart, total_spending_amount_chart, transaction_amounts_chart
from fnHelper import setDateRangeFields

def navBar(self: ProjectMainWindow, user):
    self.userWindow_schoolIdLine.setText(user['school_id'])
    self.userWindow_balanceLine.setText(str(user['balance']))
    self.navHome_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(0))
    self.navAnalytics_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(1))
    self.navTransactions_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(2))

def analytics(self: ProjectMainWindow, user):
    item_frequency_pie_chart(self.userWindow_transactions_table, self.transaction_distribution_user)
    balance_line_chart(self.userWindow_transactions_table, self.balance_over_time_user)
    total_spending_amount_chart(self.userWindow_transactions_table, self.monthly_transaction_amount_user)
    transaction_breakdown_chart(self.userWindow_transactions_table, self.transaction_breakdown_user)

def transactions(self: ProjectMainWindow, user):
    load_user_transaction_by_id(self.userWindow_transactions_table, user)
    setDateRangeFields(self.dateFrom_user, self.dateTo_user)
    self.userWindow_transaction_search.setText("")

def dateChanged(self: ProjectMainWindow, user):
    search_transactions_by_date(self.userWindow_transactions_table, self.dateFrom_user, self.dateTo_user)
    analytics(self, user)

def refresh(self: ProjectMainWindow, user):
    navBar(self, user)
    transactions(self, user)
    analytics(self, user)

def UserWindow(self: ProjectMainWindow, user):
    print(__name__)
    refresh(self, user)
    self.navRefresh_user.clicked.connect(lambda: refresh(self, user))
    self.userWindow_transaction_search.textChanged.connect(lambda text: search_transactions(text, self.userWindow_transactions_table))
    self.dateFrom_user.dateChanged.connect(lambda: dateChanged(self, user))
    self.dateTo_user.dateChanged.connect(lambda: dateChanged(self, user))
    # self.export_user.clicked.connect(lambda: export_chart_to_csv(self.userWindow_transactions_table, f"{user['school_id']}_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.csv"))
    self.exportPDF_user.clicked.connect(lambda: export_window_to_pdf(self, user))
    self.exportCSV_user.clicked.connect(lambda: export_to_csv(self.userWindow_transactions_table, user))
    self.buttonClearTransactions_user.clicked.connect(lambda: transactions(self, user))
