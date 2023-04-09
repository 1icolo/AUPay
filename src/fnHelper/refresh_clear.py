from PyQt5.QtCore import *

def clear_date(dateFrom, dateTo):
    # set QDateEdit to default position
    default_date = QDate(2000, 1, 1)
    dateFrom.setDate(default_date)
    dateTo.setDate(default_date)