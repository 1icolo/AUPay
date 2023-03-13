from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dbHelper.add_user import add_user
from dbHelper.find_user import load_user_data
# from fnHelper import find_user
from windows.ui.ui_AddUserDialog import Ui_Dialog

def load_user_data_to_table(self):
    data = load_user_data(self)
    # print(data)
    rows = len(data)
    columns = len(data[0])
    self.tableUsers_administrator.setRowCount(len(data))
    # Add the user data to the table
    for row in range(rows):
        for column in range(columns):
            item = QTableWidgetItem(str(data[row][column]))
            self.tableUsers_administrator.setItem(row, column, item)
            self.tableUsers_administrator.item(row, column).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)

class AddUserDialog(QDialog):
    def __init__(self, parent=None):
        super(AddUserDialog, self).__init__(parent)
        self.addUserDialog()

    def addUserDialog(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonSave_addUser.clicked.connect(lambda: self.addUser())
        self.ui.buttonCancel_addUser.clicked.connect(lambda: self.close())

    def addUser(self):
        newUser = {
            'card_id': self.ui.cardID_addUser.text(),
            'school_id': self.ui.schoolID_addUser.text(),
            'password': self.ui.password_addUser.text(),
            'otp_key': "",
            'user_type': self.ui.userType_addUser.currentText().lower(),
            'balance': self.ui.balance_addUser.text(),
        }
        add_user(newUser)


def AdminWindow(self):
    print(__name__)
    self.buttonAddUser_administrator.clicked.connect(lambda: AddUserDialog().exec())
    load_user_data_to_table(self)
