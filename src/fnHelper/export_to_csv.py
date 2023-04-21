
import csv
from PyQt5.QtWidgets import QTableWidget, QFileDialog
from datetime import datetime

def export_to_csv(table: QTableWidget, user):
    file_name, _ = QFileDialog.getSaveFileName(None, 'Save CSV', f"{user['school_id']}_{datetime.now().strftime('%m-%d-%Y_%H-%M-%S')}", 'CSV Files (*.csv)')
    if file_name:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in range(table.rowCount()):
                row_data = []
                for column in range(table.columnCount()):
                    item = table.item(row, column)
                    if item is not None:
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                writer.writerow(row_data)