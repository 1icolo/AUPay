from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from collections import defaultdict

def total_amount_line_graph(tableWidget, graphicsView, user=None):
    # Remove the existing layout from the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    total_amount_deposit = defaultdict(float)
    total_amount_withdrawal = defaultdict(float)
    for row in range(tableWidget.rowCount()):
        # source = tableWidget.item(row, 2).text().strip()
        # destination = tableWidget.item(row, 3).text().strip()
        # amount = float(tableWidget.item(row, 4).text().strip())
        if(str(user) == tableWidget.item(row, 3).text()):
            total_amount_deposit["Deposit"] += float(tableWidget.item(row, 4).text().strip())
        elif(str(user) == tableWidget.item(row, 2).text()):
            total_amount_withdrawal["Withdrawal"] += float(tableWidget.item(row, 4).text().strip())

    # Create bar sets
    deposits_set = QBarSet('Deposits')
    withdrawals_set = QBarSet('Withdrawals')

    # Create a list to hold the categories
    categories = []

    # Add the data to the bar sets and categories list
    for deposits, amount in total_amount_deposit.items():
        deposits_set.append(amount)
        categories.append(deposits)
    for withdrawals, amount in total_amount_withdrawal.items():
        withdrawals_set.append(amount)
        categories.append(withdrawals)
    # Create a bar series and add the bar sets to it
    series = QBarSeries()
    series.append(deposits_set)
    series.append(withdrawals_set)

    # Create a chart and add the bar series to it
    chart = QChart()
    chart.addSeries(series)

    # Create and configure the x-axis (categories)
    axisX = QBarCategoryAxis()
    axisX.append(categories)
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    # Create and configure the y-axis (amounts)
    axisY = QValueAxis()
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    # Set the alignment of the legend
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    # Clear the existing layout before adding a new one
    graphicsView.setLayout(QVBoxLayout())

    # Add chartView to the layout
    graphicsView.layout().addWidget(chartView)