from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from fnHelper import login
from fnHelper.load_tables import *

def UserWindow(self, user):
        print(__name__)
        load_user_data(self, user)
        load_transactions_to_table(self, self.userWindow_transactions_table)

def load_user_data(self, user):
        self.userWindow_schoolIdLine.setText(user['school_id'])
        self.userWindow_balanceLine.setText(user['balance'])
