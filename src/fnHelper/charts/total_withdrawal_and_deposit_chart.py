from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QGraphicsView, QVBoxLayout, QTableWidget
from PyQt5.QtChart import QPieSeries, QChart, QChartView, QPieSlice
from PyQt5.QtGui import QPainter
from collections import defaultdict

def total_withdrawal_and_deposit_chart(tableWidget, graphicsView, user=None):
    # Clear any existing items in the graphics view layout
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    total_frequencies = defaultdict(int)

    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            if(str(user['school_id']) == tableWidget.item(row, 3).text()):
                total_frequencies["Deposit"] += 1
            elif(str(user['school_id']) == tableWidget.item(row, 2).text()):
                total_frequencies["Withdrawal"] += 1
    # Create a pie series
    series = QPieSeries()
    for category, frequency in total_frequencies.items():
        if frequency > 0:
            series.append("{0} ({1})".format(category, total_frequencies[category]), frequency)

    # Create a chart and add the pie series to it
    chart = QChart()
    # Show the percentage of each slice
    chart.addSeries(series)
    # chart.createDefaultAxes()

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