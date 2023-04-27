from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDateEdit

def semestral(dateFrom: QDateEdit, dateTo: QDateEdit):
    current_month = QDate.currentDate().month()
    current_year = QDate.currentDate().year()
    if 1 <= current_month <= 5:
        dateFrom.setDate(QDate(current_year, 1, 1))
    elif 6 <= current_month <= 7:
        dateFrom.setDate(QDate(current_year, 6, 1))
    else:
        dateFrom.setDate(QDate(current_year, 8, 1))
    dateTo.setDate(QDate.currentDate())
    

def quadrennialy(dateFrom: QDateEdit, dateTo: QDateEdit):
    current_year = QDate.currentDate().year()
    dateFrom.setDate(QDate(current_year - 4, 1, 1))
    dateTo.setDate(QDate.currentDate())


def monthly(dateFrom: QDateEdit, dateTo: QDateEdit):
    current_month = QDate.currentDate().month()
    current_year = QDate.currentDate().year()
    dateFrom.setDate(QDate(current_year, current_month, 1))
    dateTo.setDate(QDate.currentDate())


def weekly(dateFrom: QDateEdit, dateTo: QDateEdit):
    current_month = QDate.currentDate().month()
    current_year = QDate.currentDate().year()
    dateFrom.setDate(QDate(current_year, current_month, QDate.currentDate().day() - 7))
    dateTo.setDate(QDate.currentDate())


def daily(dateFrom: QDateEdit, dateTo: QDateEdit):
    dateFrom.setDate(QDate.currentDate())
    dateTo.setDate(QDate.currentDate())