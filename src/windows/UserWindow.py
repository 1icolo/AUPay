from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from fnHelper import login
from fnHelper.load_tables import *
from fnHelper.textSearch import *
from dbHelper.compute_user_balance import *
from dbHelper.find_transaction import *

def UserWindow(self, user):
    print(__name__)
    load_user_data(self, user)
    self.userWindow_transaction_search.textChanged.connect(lambda text: search_transactions(self, text, self.userWindow_transactions_table))
    load_user_transaction_by_id(self.userWindow_transactions_table, user['_id'])
    load_bar_chart(self.userWindow_transactions_table, self.graphicsView)

def load_user_data(self, user):
    self.userWindow_schoolIdLine.setText(user['school_id'])
    self.userWindow_balanceLine.setText(str(compute_user_balance(user['_id'])))

