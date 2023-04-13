from PyQt5.QtCore import *
from fnHelper.load_tables import load_users_to_table
from datetime import *

def clear_date(dateFrom, dateTo):
    # set QDateEdit to default position
    dateFrom.setDate(QDate(2000, 1, 1))
    dateTo.setDate(QDate.currentDate())


