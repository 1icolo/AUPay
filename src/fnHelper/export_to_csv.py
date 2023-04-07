from PyQt5.QtWidgets import QMessageBox
import os
import csv


def export_to_csv(tableWidget):
    # Clean up the descriptions by stripping extra spaces and converting to lowercase
    descriptions = [tableWidget.item(row, 5).text().strip().title() for row in range(tableWidget.rowCount())]

    # Split multi-item descriptions into individual items
    items = []
    for description in descriptions:
        items.extend(description.split(','))

    # Count the frequency of each item, accumulating frequencies of items with the same name
    frequencies = {}
    total_frequencies = {}
    for item in items:
        item_name = item.strip()
        if item_name not in frequencies:
            frequencies[item_name] = 0
            total_frequencies[item_name] = 0
        frequencies[item_name] += 1
        total_frequencies[item_name] += 1

    return frequencies

def export_chart_to_csv(tableWidget, filename):
    frequencies = export_to_csv(tableWidget)

    basename, ext = os.path.splitext(filename)
    output_filename = basename + '.csv'

    # Prompt to confirm download
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Export chart data to CSV")
    msg_box.setText(f"Are you sure you want to export the chart data to {output_filename}?")
    msg_box.setIcon(QMessageBox.Question)
    msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    if msg_box.exec_() == QMessageBox.Yes:
        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Item', 'Frequency'])
            for item_name, frequency in frequencies.items():
                if frequency > 0:
                    writer.writerow([item_name, frequency])

        print(f'Exported chart data to {output_filename}')


