from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit

def setDateRangeFields(dateFrom: QDateEdit, dateTo: QDateEdit):
    current_month = QDate.currentDate().month()
    current_year = QDate.currentDate().year()
    if 1 <= current_month <= 5:
        dateFrom.setDate(QDate(current_year, 1, 1))
    elif 6 <= current_month <= 7:
        dateFrom.setDate(QDate(current_year, 6, 1))
    else:
        dateFrom.setDate(QDate(current_year, 8, 1))
    dateTo.setDate(QDate.currentDate())


def weekly(dateFrom: QDateEdit, dateTo: QDateEdit):
    current_month = QDate.currentDate().month()
    current_year = QDate.currentDate().year()
    dateFrom.setDate(QDate(current_year, current_month, QDate.currentDate().day() - 7))
    dateTo.setDate(QDate.currentDate())


def daily(dateFrom: QDateEdit, dateTo: QDateEdit):
    dateFrom.setDate(QDate.currentDate())
    dateTo.setDate(QDate.currentDate())