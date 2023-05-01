import re
from fnHelper.load_tables import *

def countKeyword(searchBar, paragraph):
    match = re.findall(searchBar, paragraph)
    length = match.__len__()
    print(length)
    return length

def search_users(text, tablewidget):
    # iterate over each row in the inventory table
    for row in range(tablewidget.rowCount()):
        _id = tablewidget.item(row, 0).text()
        card_id = tablewidget.item(row, 1).text()
        school_id = tablewidget.item(row, 2).text()
        password = tablewidget.item(row, 3).text()
        secret_key = tablewidget.item(row, 4).text()
        user_type = tablewidget.item(row, 5).text()
        balance = tablewidget.item(row, 6).text()

        
        # check if the search text is a substring of any of the items in the row
        if text.lower() in _id.lower() or text.lower() in card_id.lower() or text.lower() in school_id.lower() or text.lower() in password.lower() or text.lower() in secret_key.lower() or text.lower() in user_type.lower() or text.lower() in balance.lower():
            tablewidget.setRowHidden(row, False)
        else:
            tablewidget.setRowHidden(row, True)


def search_transactions(text, tablewidget):
    # iterate over each row in the inventory table
    for row in range(tablewidget.rowCount()):
        _id = tablewidget.item(row, 0).text()
        timestamp = tablewidget.item(row, 1).text()
        source_id = tablewidget.item(row, 2).text()
        destination_id = tablewidget.item(row, 3).text()
        amount = tablewidget.item(row, 4).text()
        description = tablewidget.item(row, 5).text()
        
        # check if the search text is a substring of any of the items in the row
        if text.lower() in _id.lower() or text.lower() in timestamp.lower() or text.lower() in source_id.lower() or text.lower() in destination_id.lower() or text.lower() in amount.lower() or text.lower() in description.lower():
            tablewidget.setRowHidden(row, False)
        else:
            tablewidget.setRowHidden(row, True)
    # refresh_bar_chart(tablewidget, graphicsView)
        


