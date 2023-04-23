from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
import datetime

def transactions_count_per_month(tableWidget, graphicsView):
    # Clear any existing content in the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # Create a horizontal bar series to hold the data
    series = QHorizontalBarSeries()

    # Count the frequency of transactions per month
    transaction_counts = {}
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            timestamp = QDateTime.fromString(tableWidget.item(row, 1).text(), "MM/dd/yyyy").toMSecsSinceEpoch()
            month = QDateTime.fromMSecsSinceEpoch(timestamp).toString("MMMM yyyy")
            if month not in transaction_counts:
                transaction_counts[month] = 0
            transaction_counts[month] += 1

    # Add the data to the series
    sorted_months = sorted(transaction_counts.keys(), key=lambda x: datetime.datetime.strptime(x, '%B %Y'))
    bar_set = QBarSet('Transaction Count')
    for month in sorted_months:
        count = transaction_counts[month]
        label = f"{month} ({count})"
        bar_set.append(count)
        sorted_months[sorted_months.index(month)] = label
    series.append(bar_set)

    # Create and set the labels for the bars
    axis_y = QBarCategoryAxis()
    axis_y.append(sorted_months)

    # Create a chart and add the horizontal bar series to it
    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAxisY(axis_y, series)
    chart.setAnimationOptions(QChart.SeriesAnimations)
    # chart.setTitle("Transaction Count per Month")

    # Hide the legend and enable animations
    chart.legend().hide()

    # Create a chart view and add it to the graphicsView
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    graphicsView.setLayout(QVBoxLayout())
    graphicsView.layout().addWidget(chartView)
