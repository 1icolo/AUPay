from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.find_user import find_all_users
from dbHelper.find_transaction import find_all_transactions
# import json
from fnHelper import jsonIO


def load_users_to_table(self, tableWidget):
    users = find_all_users()
    users_data = []
    for user in users:
        users_data.append([user['_id'],user['card_id'],user['school_id'],user['password'],user['otp_key'],user['user_type'],user['balance']])
    # print(users_data)
    rows = len(users_data)
    columns = len(users_data[0])
    tableWidget.setRowCount(len(users_data))
    tableWidget.hideColumn(0)
    # Add the user data to the table
    for row in range(rows):
        for column in range(columns):
            item = QTableWidgetItem(str(users_data[row][column]))
            tableWidget.setItem(row, column, item)
    tableWidget.itemSelectionChanged.connect(lambda: id_of_selected_row_user(self))

    def id_of_selected_row_user(self):
        selected_row = tableWidget.currentRow()
        _id = tableWidget.item(selected_row, 0).text()
        print(_id)

def load_transactions_to_table(self,tableWidget):
    transactions = find_all_transactions()
    transaction_data = []
    transactions_data = []
    for transaction in transactions:
        transaction_data.append([transaction['timestamp']])
        bson_timestamp = transaction_data[0][0]
        from datetime import datetime
        dt = datetime.fromtimestamp(bson_timestamp.time)
        date_string = dt.strftime("%m/%d/%y")
        transactions_data.append([transaction['_id'], date_string, transaction['source_id'],
                                 transaction['destination_id'], transaction['amount'], transaction['description']])
    # print(transactions_data)
    rows = len(transactions_data)
    columns = len(transactions_data[0])
    tableWidget.setRowCount(len(transactions_data))
    # Add the user data to the table
    for row in range(rows):
        for column in range(columns):
            item = QTableWidgetItem(str(transactions_data[row][column]))
            tableWidget.setItem(row, column, item)
    tableWidget.itemSelectionChanged.connect(lambda: id_of_selected_row_transaction(self))

    def id_of_selected_row_transaction(self):
        selected_row = tableWidget.currentRow()
        _id = tableWidget.item(selected_row, 0).text()
        print(_id)

def load_inventory_to_table(self, tableWidget):
    items_data = jsonIO.read_items()
    tableWidget.setRowCount(sum(len(v) for v in items_data.values()))
    # print(items_data.values())
    row = 0
    for id, items in items_data.items():
        for item in items:
            tableWidget.setItem(row, 0, QTableWidgetItem(id))
            tableWidget.setItem(row, 1, QTableWidgetItem(item['name']))
            tableWidget.setItem(row, 2, QTableWidgetItem(str(item['price'])))
            row += 1