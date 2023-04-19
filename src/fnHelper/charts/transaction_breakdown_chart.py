from collections import defaultdict
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QChartView, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout

def transaction_breakdown_chart(tableWidget, graphicsView):
    # Clear any existing content in the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
    else:
        # If the graphicsView doesn't have a layout, create one
        graphicsView.setLayout(QVBoxLayout())
        layout = graphicsView.layout()

    # Create dictionaries to hold the transaction amounts by source and destination
    source_amounts = defaultdict(float)
    destination_amounts = defaultdict(float)

    # Iterate over the rows of the tableWidget
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            # Get the source, destination, and amount from the tableWidget
            source = tableWidget.item(row, 2).text().strip()
            destination = tableWidget.item(row, 3).text().strip()
            amount = float(tableWidget.item(row, 4).text().strip())

            # Add the transaction amount to the source and destination totals
            source_amounts[source] += amount
            destination_amounts[destination] += amount

    # Create bar sets for the sources and destinations
    source_set = QBarSet('Sources')
    destination_set = QBarSet('Destinations')

    # Create a list to hold the categories (sources and destinations)
    categories = []

    # Add the data to the bar sets and categories list
    for source, amount in source_amounts.items():
        source_set.append(amount)
        categories.append(source)
    for destination, amount in destination_amounts.items():
        destination_set.append(amount)
        categories.append(destination)

    # Create a bar series and add the bar sets to it
    series = QBarSeries()
    series.append(source_set)
    series.append(destination_set)

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

    # Enable animations
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view and add it to the graphicsView
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    layout.addWidget(chartView)