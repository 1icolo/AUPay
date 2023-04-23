from PyQt5 import QtWidgets
import img2pdf
import os
from datetime import datetime

def export_window_to_pdf(window, user):
    screen = QtWidgets.QApplication.primaryScreen()
    screenshot = screen.grabWindow(window.winId())
    file_name = f"{user['school_id']}_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}"

    screenshot.save("temp/screenshot.png", "png")

    save_file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save PDF', f'{file_name}.pdf', 'PDF Files (*.pdf)')
    if save_file_name:
        with open(save_file_name, "wb") as f:
            f.write(img2pdf.convert("temp/screenshot.png"))

    os.remove("temp/screenshot.png")