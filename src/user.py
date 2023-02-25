from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from user_ui import Ui_UserMainWindow


class UserMainWindow(QMainWindow, Ui_UserMainWindow):
    def __init__(self, parent = None):
        super(UserMainWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.buttonLogout.clicked.connect(lambda: print("Logout"))



app = QApplication([])
window = UserMainWindow()
window.show()
app.exec()