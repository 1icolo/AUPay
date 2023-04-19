from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from dbHelper.find_user import find_all_users
from dbHelper.find_transaction import *
# import json
from fnHelper import jsonIO
from datetime import *



def load_users_to_table(self, tableWidget):
    users = find_all_users()
    users_data = []
    for user in users:
        users_data.append([user['_id'],user['card_id'],user['school_id'],user['password'],user['otp_key'],user['user_type'],user['balance']])
    # print(users_data)
    rows = len(users_data)
    columns = len(users_data[0])
    tableWidget.setRowCount(len(users_data))
    tableWidget.hideColumn(0)
    # Add the user data to the table
    for row in range(rows):
        for column in range(columns):
            item = QTableWidgetItem(str(users_data[row][column]))
            tableWidget.setItem(row, column, item)
    tableWidget.itemSelectionChanged.connect(lambda: id_of_selected_row_user(self))

    def id_of_selected_row_user(self):
        selected_row = tableWidget.currentRow()
        _id = tableWidget.item(selected_row, 0).text()
        print(_id)

def load_transactions_to_table(self, tableWidget, user):
    transactions = find_all_transactions_aggregated()
    transaction_data = []
    transactions_data = []
    count = 0
    for transaction in transactions:
        transaction_data.append([transaction['timestamp']])
        bson_timestamp = transaction_data[count][0]
        count += 1
        dt = datetime.fromtimestamp(bson_timestamp.time)
        date_string = dt.strftime("%m/%d/%Y")
        transactions_data.append([transaction['_id'], date_string, transaction['source_id'],
                                 transaction['destination_id'], transaction['amount'], transaction['description']])
    # print(transactions_data)
    rows = len(transactions_data)
    columns = len(transactions_data[0])
    tableWidget.setRowCount(len(transactions_data))
    # Add the user data to the table
    for row in range(rows):
        for column in range(columns):
            item = QTableWidgetItem(str(transactions_data[row][column]))
            tableWidget.setItem(row, column, item)
            destination_id = transactions_data[row][3]
            if destination_id == user['school_id']:
                color = QColor(51, 255, 153)  # light green
            else:
                color = QColor(255, 255, 255)  # light red
            for column in range(columns):
                item = QTableWidgetItem(str(transactions_data[row][column]))
                item.setBackground(color)
                tableWidget.setItem(row, column, item)
    tableWidget.itemSelectionChanged.connect(lambda: id_of_selected_row_transaction(self))

    def id_of_selected_row_transaction(self):
        selected_row = tableWidget.currentRow()
        _id = tableWidget.item(selected_row, 0).text()
        print(_id)

def load_inventory_to_table(tableWidget):
    try:
        items = jsonIO.read_items()
        items_data = []
        for item in items:
            items_data.append([item['price'], item['name']])
        rows = len(items_data)
        columns = len(items_data[0])
        tableWidget.setRowCount(len(items_data))
        for row in range(rows):
            for column in range(columns):
                item = QTableWidgetItem(str(items_data[row][column]))
                tableWidget.setItem(row, column, item)
    except Exception as e:
        print(f"Exception in load_inventory_to_table\n{e}")

def load_user_transaction_by_id(tableWidget, user):
    transactions = find_all_transactions_of_user_aggregated(user['_id'])
    transaction_data = []
    transactions_data = []
    count = 0
    for transaction in transactions:
        transaction_data.append([transaction['timestamp']])
        bson_timestamp = transaction_data[count][0]
        count += 1
        dt = datetime.fromtimestamp(bson_timestamp.time)
        date_string = dt.strftime("%m/%d/%Y")

        # conversion to negative if source is the user
        if transaction['source_id'] == user['school_id']:
            transaction['amount'] = transaction['amount'] * -1
            
        transactions_data.append([transaction['_id'], date_string, transaction['source_id'],
                                 transaction['destination_id'], transaction['amount'], transaction['description']])
    # print(transactions_data)
    rows = len(transactions_data)
    # columns = len(transactions_data[0])
    if transactions_data:
        columns = len(transactions_data[0])
    else:
        columns = 0
    tableWidget.setRowCount(len(transactions_data))
    # Add the user data to the table
    for row in range(rows):
        destination_id = transactions_data[row][3]
        if destination_id == user['school_id']:
            color = QColor(198, 239, 206)  # light green
        else:
            color = QColor(255, 199, 206)  # light red
        for column in range(columns):
            item = QTableWidgetItem(str(transactions_data[row][column]))
            item.setBackground(color)
            tableWidget.setItem(row, column, item)

# from PyQt5.QtCore import QPropertyAnimation

def load_bar_chart(tableWidget, graphicsView):
    # Remove the existing layout from the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    series = QHorizontalBarSeries()

    # Get the descriptions of the visible rows in the table
    descriptions = []
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            description = tableWidget.item(row, 5).text().strip().title()
            descriptions.append(description)

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

    # Add the data to the series
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1])  # Sort from highest to lowest (reverse=True)
    bar_set = QBarSet('Items')
    labels = []
    for item_name, frequency in sorted_frequencies:
        if frequency > 0:
            bar_set.append(frequency)
            labels.append("{0} ({1})".format(item_name, total_frequencies[item_name]))
    series.append(bar_set)

    # Create and set the labels for the bars
    axis_y = QBarCategoryAxis()
    axis_y.append(labels)
    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAxisY(axis_y, series)
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Set the alignment of the legend
    chart.legend().hide()

    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    # Clear the existing layout before adding a new one
    graphicsView.setLayout(QVBoxLayout())

    # Add chartView to the layout
    graphicsView.layout().addWidget(chartView)








def refresh_bar_chart(tableWidget, graphicsView):
    pass
    # # Remove any existing chart view from the layout
    # chartView = None
    # for i in range(graphicsView.layout().count()):
    #     widget = graphicsView.layout().itemAt(i).widget()
    #     if isinstance(widget, QChartView):
    #         chartView = widget
    #         graphicsView.layout().removeWidget(chartView)
    #         break
    # if chartView is not None:
    #     chartView.deleteLater()

    # # Load the new chart and add it to the layout
    # load_bar_chart(tableWidget, graphicsView)



def search_transactions_by_date(tableWidget, date_from_edit, date_to_edit):
    # get the selected date range
    date_from = date_from_edit.date().toPyDate()
    date_to = date_to_edit.date().toPyDate()

    # iterate over each row in the inventory table
    descriptions = []
    for row in range(tableWidget.rowCount()):
        timestamp_str = tableWidget.item(row, 1).text()
        timestamp = datetime.strptime(timestamp_str, "%m/%d/%Y").date()

        # check if the timestamp falls within the date range
        if timestamp >= date_from and timestamp <= date_to:
            # show rows that fall within the selected date range
            tableWidget.setRowHidden(row, False)
            descriptions.append(tableWidget.item(row, 5).text().strip().title())
        else:
            # hide rows that do not fall within the selected date range
            tableWidget.setRowHidden(row, True)

    # refresh_bar_chart(tableWidget, graphicsView)
    return descriptions


