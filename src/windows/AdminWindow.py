from dbHelper import add_user
from windows.ui.ui_AddUserDialog import Ui_Dialog

def AdminWindow(self):
        print(__name__)

def addUserDialog(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonSave_addUser.clicked.connect(lambda: addUser(self))
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