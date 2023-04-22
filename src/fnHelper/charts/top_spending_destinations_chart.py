from collections import defaultdict
from PyQt5.QtChart import QBarSet, QChart, QChartView, QBarCategoryAxis, QBarSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout

def top_spending_destinations_chart(tableWidget, graphicsView, user):
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    spending = defaultdict(float)
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            if str(user['school_id']) == tableWidget.item(row, 2).text():
                destination = tableWidget.item(row, 3).text()
                amount = float(tableWidget.item(row, 4).text().strip())
                spending[destination] += amount

    labels = []
    bar_set = QBarSet("Destination")
    for destination, amount in spending.items():
        bar_set.append(amount)
        labels.append("{0} ({1})".format(destination, spending[destination]))

    series = QBarSeries()
    series.append(bar_set)
    axis_y = QBarCategoryAxis()
    axis_y.append(labels)
    axis_y.setMax("10000")
    axis_y.setMin("0")
    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAxisY(axis_y, series)
    chart.setAnimationOptions(QChart.SeriesAnimations)

    chart.legend().hide()

    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    graphicsView.setLayout(QVBoxLayout())
    graphicsView.layout().addWidget(chartView)