from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from database import Database
from admin_ui import Ui_AdminMainWindow


class AdminMainWindow(QMainWindow, Ui_AdminMainWindow):
    def __init__(self, parent = None):
        super(AdminMainWindow, self).__init__(parent)

        self.setupUi(self)
        

app = QApplication([])
window = AdminMainWindow()
window.show()
app.exec()