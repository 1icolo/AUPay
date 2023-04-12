from PyQt5.QtWidgets import *
from windows.ProjectMainWindow import ProjectMainWindow


def main():
    app = QApplication([])
    ProjectMainWindow().show()
    app.exec()


if __name__ == "__main__":
    main()

