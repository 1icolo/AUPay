from PyQt5.QtWidgets import *
from windows.ui.adminWindow_ui import Ui_AdminWindow


class AdminWindow(QMainWindow, Ui_AdminWindow):
    def __init__(self, parent = None):
        super(AdminWindow, self).__init__(parent)
        self.setupUi(self)
        # self.load_user_data(self)
        # self.load_transactions_data(self)
    
    # def load_user_data(self, user_data):
    #     user_data = Database().load_user_table()
    #     rows = len(user_data)
    #     columns = len(user_data[0])
    #     self.usersTable.setRowCount(rows)
    #     self.usersTable.setColumnCount(columns)
    #     # Add the user data to the table
    #     for row in range(rows):
    #         for column in range(columns):
    #             item = QTableWidgetItem(str(user_data[row][column]))
    #             self.usersTable.setItem(row, column, item)
    #             self.usersTable.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
    
    # def load_transactions_data(self, transaction_data):
    #     transaction_data = Database().load_transaction_table()
    #     rows = len(transaction_data)
    #     columns = len(transaction_data[0])
    #     self.transactionsTable.setRowCount(rows)
    #     self.transactionsTable.setColumnCount(columns)
    #     # Add the user data to the table
    #     for row in range(rows):
    #         for column in range(columns):
    #             item = QTableWidgetItem(str(transaction_data[row][column]))
    #             self.transactionsTable.setItem(row, column, item)
    #             self.transactionsTable.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
