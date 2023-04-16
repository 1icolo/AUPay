from dbHelper import find_user_by_login
from dbHelper import find_user_by_card_id
from fnHelper.cryptography import hash
from fnHelper.aupCard import AUPCard

def login(self, mode):
    try:
        user = None
        if mode == 'password':
            user = find_user_by_login(self.lineSchoolId_login.text(), hash(self.linePassword_login.text()))
        elif mode == 'rfid':
            user = find_user_by_card_id(hash(AUPCard(0.001).get_uid()))

        if user is None:
            return

        if self.checkBoxLoginAsClient_login.isChecked():
            self.stackedWidget.setCurrentIndex(1)
            from windows.UserWindow import UserWindow
            UserWindow(self, user)
        else:
            if user['user_type'] == 'admin':
                self.stackedWidget.setCurrentIndex(4)
                from windows.AdminWindow import AdminWindow
                AdminWindow(self, user)
            elif user['user_type'] == 'user':
                self.stackedWidget.setCurrentIndex(1)
                from windows.UserWindow import UserWindow
                UserWindow(self, user)
            elif user['user_type'] == 'business':
                self.stackedWidget.setCurrentIndex(2)
                from windows.BusinessWindow import BusinessWindow
                BusinessWindow(self, user)
            elif user['user_type'] == 'teller':
                self.stackedWidget.setCurrentIndex(3)
                from windows.TellerWindow import TellerWindow
                TellerWindow(self, user)
    except Exception as e:
        print(f"Login Failed. \n{e}")
