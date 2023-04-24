from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QGraphicsView, QVBoxLayout, QTableWidget
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice, QLegend
from PyQt5.QtGui import QPainter
from collections import defaultdict
from PyQt5.QtCore import Qt

def total_withdrawal_and_deposit_chart(tableWidget, graphicsView, user=None):
    # Remove the existing layout from the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # Initialize dictionaries to store total amount and count of deposits and withdrawals
    total_amount = defaultdict(float)
    count = defaultdict(int)

    # Iterate over each row in the tableWidget
    for row in range(tableWidget.rowCount()):
        # Check if the row is hidden
        if not tableWidget.isRowHidden(row):
            # Get the source_id and destination_id from the tableWidget
            source_id = tableWidget.item(row, 2).text()
            destination_id = tableWidget.item(row, 3).text()
            # Check if source_id and destination_id are not equal to "COINBASE"
            if source_id != "COINBASE" and destination_id != "COINBASE":
                # Check if the user's school_id matches the destination_id
                if(str(user['school_id']) == tableWidget.item(row, 3).text()):
                    # Add the amount to the total_amount for deposits and increment the count for deposits
                    total_amount["Deposit"] += float(tableWidget.item(row, 4).text().strip())
                    count["Deposit"] += 1
                # Check if the user's school_id matches the source_id
                elif(str(user['school_id']) == tableWidget.item(row, 2).text()):
                    # Subtract the amount from the total_amount for withdrawals and increment the count for withdrawals
                    total_amount["Withdrawal"] += (float(tableWidget.item(row, 4).text().strip()) * -1)
                    count["Withdrawal"] += 1

    # Create a QPieSeries to store data for the pie chart
    series = QPieSeries()
    # Iterate over each category (Deposit or Withdrawal) and its corresponding amount in total_amount
    for category, amount in total_amount.items():
        # Check if the amount is greater than 0
        if amount > 0:
            # Add data to the series in the format "Category: Count, Total Amount"
            series.append("{0}: {1}, {2}".format(category, count[category], total_amount[category]), amount)

    # Create a QChart and add the series to it
    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.legend().setMarkerShape(QLegend.MarkerShapeDefault)

    # Create a QChartView to display the chart
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    # Set the layout of graphicsView to QVBoxLayout and add chartView to it
    graphicsView.setLayout(QVBoxLayout())
    graphicsView.layout().addWidget(chartView)