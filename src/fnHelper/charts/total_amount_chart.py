from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *
from collections import defaultdict

def total_amount_chart(tableWidget, graphicsView, user=None):
    # Remove the existing layout from the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    total_amount = defaultdict(float)

    for row in range(tableWidget.rowCount()):
        if(str(user) == tableWidget.item(row, 3).text()):
            total_amount["Deposit"] += float(tableWidget.item(row, 4).text().strip())
        elif(str(user) == tableWidget.item(row, 2).text()):
            total_amount["Withdrawal"] += (float(tableWidget.item(row, 4).text().strip()) * -1)
    # Create bar sets
    labels = []
    bar_set = QBarSet("Item")
    for category, amount in total_amount.items():
        # print(category, amount)
        if amount > 0:
            bar_set.append(amount)
            labels.append("{0} ({1})".format(category, total_amount[category]))

    # Create and set the labels for the bars
    series = QHorizontalBarSeries()
    series.append(bar_set)
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