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
from fnHelper.charts import *
from windows.ProjectMainWindow import ProjectMainWindow

def navBar(self, user):
    self.userWindow_schoolIdLine.setText(user['school_id'])
    self.userWindow_balanceLine.setText(str(user['balance']))
    self.navHome_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(0))
    self.navAnalytics_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(1))
    self.navTransactions_user.clicked.connect(lambda: self.stackedWidget_user.setCurrentIndex(2))

def analytics(self, user):
    item_frequency_pie_chart(self.userWindow_transactions_table, self.transaction_distribution_user)

def UserWindow(self: ProjectMainWindow, user):
    print(__name__)
    navBar(self, user)
    load_user_transaction_by_id(self.userWindow_transactions_table, user['_id'])
    analytics(self, user)
    
    # self.dateFrom_user.setDate(QDate.currentDate())  # set default search date
    self.dateTo_user.setDate(QDate.currentDate())
    self.userWindow_transaction_search.textChanged.connect(lambda text: search_transactions(text, self.userWindow_transactions_table, self.graphicsView_2))
    
    # self.dateFrom_user.textChanged.connect(lambda text, selected_date: search_date_transactions(self, text, selected_date, self.userWindow_transactions_table))
    self.dateFrom_user.dateChanged.connect(lambda: search_transactions_by_date(self.userWindow_transactions_table, self.dateFrom_user, self.dateTo_user, self.graphicsView_2))
    self.dateTo_user.dateChanged.connect(lambda: search_transactions_by_date(self.userWindow_transactions_table, self.dateFrom_user, self.dateTo_user, self.graphicsView_2))
    self.export_user.clicked.connect(lambda: export_chart_to_csv(self.userWindow_transactions_table, f"{user['school_id']}_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.csv"))
    self.buttonClearTransactions_user.clicked.connect(lambda: clear_date(self.dateFrom_user, self.dateTo_user))
