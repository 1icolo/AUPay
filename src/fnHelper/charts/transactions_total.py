from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

def transactions_total(tableWidget, graphicsView):
    # Remove the existing layout from the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    series = QHorizontalBarSeries()

    # Get the total of the visible rows in the table
    total = 0
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            amount = tableWidget.item(row, 4).text().strip()
            try:
                total += float(amount)
            except ValueError:
                pass

    # Add the data to the series
    bar_set = QBarSet('Total')
    bar_set.append(total)
    series.append(bar_set)

    # Create and set the labels for the bars
    axis_y = QBarCategoryAxis()
    axis_y.append('')
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