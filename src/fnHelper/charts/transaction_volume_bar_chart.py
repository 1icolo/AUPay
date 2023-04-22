
from collections import defaultdict
from PyQt5.QtChart import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


def transaction_volume_bar_chart(tableWidget: QTableWidget, graphicsView: QGraphicsView):
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    series = QBarSeries()

    # Create a dictionary to store the transaction volume for each source account
    transaction_volume = {}

    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            source_account = tableWidget.item(row, 2).text().strip()
            amount = float(tableWidget.item(row, 4).text().strip())
            amount = abs(amount) # Convert any negative values to positive

            # Update the transaction volume for the source account
            if source_account in transaction_volume:
                transaction_volume[source_account] += amount
            else:
                transaction_volume[source_account] = amount

    # Create a bar set for each source account and add it to the series
    for source_account, volume in transaction_volume.items():
        bar_set = QBarSet(source_account)
        bar_set.append(volume)
        series.append(bar_set)

    chart = QChart()
    chart.addSeries(series)

    axisX = QBarCategoryAxis()
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    axisY = QValueAxis()
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    chart.legend().setVisible(True)
    chart.setAnimationOptions(QChart.SeriesAnimations)

    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    graphicsView.setLayout(QVBoxLayout())
    graphicsView.layout().addWidget(chartView)