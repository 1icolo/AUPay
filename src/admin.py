from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from database import Database
from admin_ui import Ui_AdminMainWindow


class AdminMainWindow(QMainWindow, Ui_AdminMainWindow):
    def __init__(self, parent = None):
        super(AdminMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.load_user_data(self)
    
    def load_user_data(self, data):
        data = Database().load_user_table()
        rows = len(data)
        columns = len(data[0])
        self.usersTable.setRowCount(rows)
        self.usersTable.setColumnCount(columns)
        # Add the user data to the table
        for row in range(rows):
            for column in range(columns):
                item = QTableWidgetItem(str(data[row][column]))
                self.usersTable.setItem(row, column, item)
                self.usersTable.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

app = QApplication([])
window = AdminMainWindow()
window.show()
app.exec()