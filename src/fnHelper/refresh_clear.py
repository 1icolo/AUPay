from PyQt5.QtCore import *
from fnHelper.load_tables import load_users_to_table

def clear_date(dateFrom, dateTo):
    # set QDateEdit to default position
    default_date = QDate(2000, 1, 1)
    dateFrom.setDate(default_date)
    dateTo.setDate(default_date)

def resfresh_table(self, tableWidget):
    load_users_to_table(self, tableWidget)
    print("Table refreshed")
