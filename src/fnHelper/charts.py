from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QGraphicsView, QVBoxLayout, QTableWidget
from PyQt5.QtChart import QPieSeries, QChart, QChartView
from PyQt5.QtGui import QPainter

def item_frequency_pie_chart(tableWidget, graphicsView):
    # Clear any existing items in the graphics view layout
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # Create a pie series
    series = QPieSeries()

    # Get the descriptions from the table widget
    descriptions = []
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            description = tableWidget.item(row, 5).text().strip().title()
            descriptions.append(description)

    # Split the descriptions into individual items
    items = []
    for description in descriptions:
        items.extend(description.split(','))

    # Count the frequency of each item
    frequencies = {}
    total_frequencies = {}
    for item in items:
        item_name = item.strip()
        if item_name not in frequencies:
            frequencies[item_name] = 0
            total_frequencies[item_name] = 0
        frequencies[item_name] += 1
        total_frequencies[item_name] += 1

    # Sort the frequencies from highest to lowest
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    # Add the top 10 items to the pie series
    count = 0
    for item_name, frequency in sorted_frequencies:
        if frequency > 0 and count < 10:
            series.append("{0} ({1})".format(item_name, total_frequencies[item_name]), frequency)
            count += 1

    # Create a chart and add the pie series to it
    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()

    # Set the alignment of the legend to the right
    chart.legend().setAlignment(QtCore.Qt.AlignRight)

    # Set the animation options for the chart
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view and set its render hint to antialiasing
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    # Set the layout of the graphics view to a vertical box layout
    graphicsView.setLayout(QVBoxLayout())

    # Add the chart view to the layout of the graphics view
    graphicsView.layout().addWidget(chartView)