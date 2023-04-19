from collections import defaultdict
from datetime import datetime
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QChartView, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout

def monthly_transaction_amounts_chart(tableWidget, graphicsView):
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

    # Create a dictionary to hold the monthly transaction amounts
    monthly_amounts = defaultdict(float)

    # Iterate over the rows of the tableWidget
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            # Get the date and amount from the tableWidget
            date = tableWidget.item(row, 1).text().strip()
            amount = float(tableWidget.item(row, 4).text().strip())

            # Convert the date to a datetime object
            date = datetime.strptime(date, '%m/%d/%Y')

            # Get the year and month of the transaction
            year_month = (date.year, date.month)

            # Add the transaction amount to the monthly total
            monthly_amounts[year_month] += amount

    # Convert the dictionary to a list of tuples and sort by year and month
    monthly_amounts = sorted(monthly_amounts.items())

    # Create a bar set to hold the data
    bar_set = QBarSet('Monthly Amounts')

    # Create a list to hold the categories (months)
    categories = []

    # Add the data to the bar set and categories list
    for (year, month), amount in monthly_amounts:
        bar_set.append(amount)
        categories.append(f'{year}-{month:02d}')

    # Create a bar series and add the bar set to it
    series = QBarSeries()
    series.append(bar_set)

    # Create a chart and add the bar series to it
    chart = QChart()
    chart.addSeries(series)

    # Create and configure the x-axis (months)
    axisX = QBarCategoryAxis()
    axisX.append(categories)
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    # Create and configure the y-axis (amounts)
    axisY = QValueAxis()
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    # Hide the legend and enable animations
    chart.legend().hide()
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view and add it to the graphicsView
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    layout.addWidget(chartView)