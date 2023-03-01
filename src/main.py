from PyQt5.QtWidgets import *
from windows.loginWindow import LoginWindow


def main():
    app = QApplication([])
    LoginWindow().show()
    app.exec()


if __name__ == "__main__":
    main()



