from dbHelper.add_transaction import add_transaction

def charge_transaction(transactionDetails):
    #scan rfid -> add transaction
    #transactionDetails['source_id'] = rfid scan
    add_transaction(transactionDetails)
