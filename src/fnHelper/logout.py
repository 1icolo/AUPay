from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import sys

def logoutAttempt(self):
        QApplication.quit()
        python = sys.executable
        os.execl(python, python, *sys.argv)