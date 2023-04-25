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

    # Keep track of the last known balance
    last_balance = float(0.00)

    # Set the interval to 1 minute
    interval = 1 * 60 * 1000

    # Initialize variables for tracking the current interval
    current_interval_start = None
    current_balance = None

    # Iterate over the rows of the tableWidget
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            # Get the date and balance from the tableWidget
            date_str = tableWidget.item(row, 1).text().strip()
            date = QDateTime.fromString(date_str, 'MM/dd/yyyy')
            timestamp = date.toMSecsSinceEpoch()
            balance = float(tableWidget.item(row, 4).text().strip())

            last_balance += balance

            # Check if this is the first row or if we have moved to a new interval
            if current_interval_start is None or timestamp >= current_interval_start + interval:
                # If this is not the first row, add the data for the previous interval to the series
                if current_interval_start is not None:
                    series.append(current_interval_start, current_balance)

                # Start a new interval
                current_interval_start = timestamp - (timestamp % interval)
                current_balance = last_balance

    # Add the data for the last interval to the series
    if current_interval_start is not None:
        series.append(current_interval_start, current_balance)

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
    axisY.setMin(0)  # Set minimum value of y-axis to 0
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    # Hide the legend and enable animations
    chart.legend().hide()
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view and set its render hint to antialiasing
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    # Add the chart view to the graphics view's layout
    graphicsView.setLayout(QVBoxLayout())
    graphicsView.layout().addWidget(chartView)