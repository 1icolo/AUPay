from PyQt5 import QtWidgets, QtCore, QtGui
import img2pdf
import os
from datetime import datetime

def export_window_to_pdf(window, user):
    screen = QtWidgets.QApplication.primaryScreen()
    screenshot = screen.grabWindow(window.winId())
    file_name = f"{user['school_id']}_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}"

    screenshot.save("screenshot.png", "png")

    with open(f"{file_name}.pdf", "wb") as f:
        f.write(img2pdf.convert("screenshot.png"))

    os.remove("screenshot.png")