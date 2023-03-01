from PyQt5.QtWidgets import *
from src.windows.ui.userWindow_ui import Ui_UserMainWindow


class UserMainWindow(QMainWindow, Ui_UserMainWindow):
    def __init__(self, parent = None):
        super(UserMainWindow, self).__init__(parent)
        
        self.setupUi(self)
        self.buttonLogout.clicked.connect(lambda: print("Logout"))



app = QApplication([])
window = UserMainWindow()
window.show()
app.exec()