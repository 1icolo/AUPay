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


def UserWindow(self, user):
    print(__name__)
    load_user_data(self, user)
    self.userWindow_transaction_search.textChanged.connect(lambda text: search_transactions(self, text, self.userWindow_transactions_table))
    load_user_transaction_by_id(self.userWindow_transactions_table, user['_id'])
    load_bar_chart(self.userWindow_transactions_table, self.graphicsView)
    # self.dateFrom_user.textChanged.connect(lambda text, selected_date: search_date_transactions(self, text, selected_date, self.userWindow_transactions_table))
    self.dateFrom_user.dateChanged.connect(lambda: search_transactions_by_date(self.userWindow_transactions_table, self.dateFrom_user, self.dateTo_user))
    self.dateTo_user.dateChanged.connect(lambda: search_transactions_by_date(self.userWindow_transactions_table, self.dateFrom_user, self.dateTo_user))
    self.export_user.clicked.connect(lambda: export_chart_to_csv(self.userWindow_transactions_table, f"{user['school_id']}_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}.csv"))
    self.buttonClearTransactions_user.clicked.connect(lambda: clear_date(self.dateFrom_user, self.dateTo_user))

def load_user_data(self, user):
    self.userWindow_schoolIdLine.setText(user['school_id'])
    self.userWindow_balanceLine.setText(str(compute_user_balance(user['_id'])))
    # self.dateFrom_user.setDate(QDate.currentDate())  # set default search date
