from PyQt5.QtChart import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtCore import QDateTime, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout

def balance_line_chart(tableWidget, graphicsView):
    # Clear any existing content in the graphicsView
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # Create a line series to hold the data
    series = QLineSeries()

    # Iterate over the rows of the tableWidget
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            # Get the date and balance from the tableWidget
            date = tableWidget.item(row, 1).text().strip()
            balance = float(tableWidget.item(row, 4).text().strip())

            # Add the data to the line series
            series.append(QDateTime.fromString(date, 'MM/dd/yyyy').toMSecsSinceEpoch(), balance)

    # Create a chart and add the line series to it
    chart = QChart()
    chart.addSeries(series)

    # Create and configure the x-axis (date)
    axisX = QDateTimeAxis()
    axisX.setFormat("MM/dd/yyyy")
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    # Create and configure the y-axis (balance)
    axisY = QValueAxis()
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    # Hide the legend and enable animations
    chart.legend().hide()
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view and add it to the graphicsView
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    graphicsView.setLayout(QVBoxLayout())
    graphicsView.layout().addWidget(chartView)