from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *



def transactions_top_contributors(tableWidget, graphicsView):
    # pass
     # Clear any existing items in the graphics view layout
    layout = graphicsView.layout()
    if layout is not None:
        while layout.count() > 0:
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # Get the sources from the table widget
    sources = []
    for row in range(tableWidget.rowCount()):
        if not tableWidget.isRowHidden(row):
            source = tableWidget.item(row, 2).text().strip().title()
            sources.append(source)

    # Count the frequency of each source and calculate the total number of transactions
    source_frequencies = {}
    total_transactions = len(sources)
    for source in sources:
        source_name = source.strip()
        if source_name not in source_frequencies:
            source_frequencies[source_name] = 0
        source_frequencies[source_name] += 1

    # Create a pie series with the percentage of transactions for each source
    series = QPieSeries()
    for source_name, frequency in source_frequencies.items():
        percentage = frequency / total_transactions * 100
        series.append("{0} ({1:.1f}%)".format(source_name, percentage), frequency)

    # Create a chart and add the pie series to it
    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()

    # Set the alignment of the legend to the right
    chart.legend().setAlignment(Qt.AlignRight)

    # Set the animation options for the chart
    chart.setAnimationOptions(QChart.SeriesAnimations)

    # Create a chart view and set its render hint to antialiasing
    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)

    # Set the layout of the graphics view to a vertical box layout
    graphicsView.setLayout(QVBoxLayout())

    # Add the chart view to the layout of the graphics view
    graphicsView.layout().addWidget(chartView)