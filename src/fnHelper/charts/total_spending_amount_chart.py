from collections import defaultdict
from datetime import datetime
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QChartView, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout

def total_spending_amount_chart(tableWidget, graphicsView):
    # Clear any existing layout in the graphics view
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
    else:
        # If no layout exists, create a new vertical layout
        graphicsView.setLayout(QVBoxLayout())
        layout = graphicsView.layout()

    # Initialize a dictionary to store the monthly amounts
    monthly_amounts = defaultdict(float)

    # Iterate over each row in the table widget
    for row in range(tableWidget.rowCount()):
        # Only process rows that are not hidden
        if not tableWidget.isRowHidden(row):
            # Get the date and amount from the table widget
            date = tableWidget.item(row, 1).text().strip()
            amount = float(tableWidget.item(row, 4).text().strip())

            # Only process negative amounts (spending)
            if amount < 0:
                # Convert the amount to a positive value
                amount = abs(amount)
                # Convert the date string to a datetime object
                date = datetime.strptime(date, '%m/%d/%Y')
                # Get the year and month from the date
                year_month = (date.year, date.month)
                # Add the amount to the monthly total for that year and month
                monthly_amounts[year_month] += amount

    # Sort the monthly amounts by year and month
    monthly_amounts = sorted(monthly_amounts.items())

    # Create a bar set to hold the monthly amounts
    bar_set = QBarSet('Monthly Amounts')

    # Initialize a list to hold the category labels (year-month)
    categories = []

    # Iterate over each year-month and amount in the monthly amounts
    for (year, month), amount in monthly_amounts:
        # Add the amount to the bar set
        bar_set.append(amount)
        # Add the formatted year-month label with amount to the categories list
        categories.append(f'{datetime(year=year, month=month, day=1).strftime("%B %Y")} ({amount:.2f})')

    # Create a bar series and add the bar set to it
    series = QBarSeries()
    series.append(bar_set)

    # Create a chart and add the series to it
    chart = QChart()
    chart.addSeries(series)

    # Create a category axis for the x-axis using the categories list
    axisX = QBarCategoryAxis()
    axisX.append(categories)
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    # Create a value axis for the y-axis
    axisY = QValueAxis()
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    # Hide the chart legend and enable animations
    chart.legend().hide()
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view and add it to the layout of the graphics view
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    layout.addWidget(chartView)