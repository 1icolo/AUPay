from windows.ui.ui_ProjectMainWindow import Ui_ProjectMainWindow

def Logout(self):
    self.stackedWidget.setCurrentIndex(0)
    self.lineSchoolId_login.setText("")
    self.linePassword_login.setText("")
    print("Logout Successfully")