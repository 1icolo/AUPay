from PyQt5.QtWidgets import *
import dbHelper
from windows.loginWindow import LoginWindow


def main():
    from windows import loginWindow
    app = QApplication([])
    LoginWindow().show()
    app.exec()


if __name__ == "__main__":
    main()



