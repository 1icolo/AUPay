from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import *

def transaction_frequency(tableWidget, graphicsView):
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