from collections import defaultdict
from datetime import datetime
from PyQt5.QtChart import QChart, QChartView, QBarSet, QHorizontalBarSeries, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QVBoxLayout

def total_spending_amount_chart(tableWidget, graphicsView):
    # Clear any existing content in the graphics view
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
    else:
        # If the graphics view doesn't have a layout yet, create one
        graphicsView.setLayout(QVBoxLayout())
        layout = graphicsView.layout()

    # Create a dictionary to store the monthly spending amounts
    monthly_amounts = defaultdict(float)

    # Iterate over the rows in the table widget
    for row in range(tableWidget.rowCount()):
        # Check if the row is hidden
        if not tableWidget.isRowHidden(row):
            # Get the date and amount from the row
            date = tableWidget.item(row, 1).text().strip()
            amount = float(tableWidget.item(row, 4).text().strip())
            # Only consider negative amounts (spending)
            if amount < 0:
                # Convert the amount to a positive value
                amount = abs(amount)
                # Parse the date string into a datetime object
                date = datetime.strptime(date, '%m/%d/%Y')
                # Create a tuple representing the year and month
                year_month = (date.year, date.month)
                # Add the amount to the monthly total for that year and month
                monthly_amounts[year_month] += amount

    # Sort the monthly amounts by year and month
    monthly_amounts = sorted(monthly_amounts.items())

    # Create a bar set to hold the data for the chart
    bar_set = QBarSet('Monthly Amounts')
    categories = []
    for (year, month), amount in monthly_amounts:
        # Add the amount to the bar set
        bar_set.append(amount)
        # Create a label for the category axis using the year and month
        categories.append(f'{datetime(year=year, month=month, day=1).strftime("%B %Y")} ({amount:.2f})')

    # Create a horizontal bar series and add the bar set to it
    series = QHorizontalBarSeries()
    series.append(bar_set)

    # Create a chart and add the series to it
    chart = QChart()
    chart.addSeries(series)

    # Create a category axis for the y-axis using the category labels
    axisY = QBarCategoryAxis()
    axisY.append(categories)
    chart.addAxis(axisY, Qt.AlignLeft)
    series.attachAxis(axisY)

    # Create a value axis for the x-axis
    axisX = QValueAxis()
    chart.addAxis(axisX, Qt.AlignBottom)
    series.attachAxis(axisX)

    # Hide the legend and enable animations
    chart.legend().hide()
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view to display the chart and add it to the layout of the graphics view
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    layout.addWidget(chartView)