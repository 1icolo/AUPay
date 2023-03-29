from dbHelper.find_transaction import find_transaction

def refund_transaction(transaction_id):
    # get transaction if transaction exists
    transaction = find_transaction(transaction_id)
    if transaction is None:
        print('Transaction does not exist')
        return

    # scan rfid of user


    # scan rfid of admin/teller


    # add transaction
    pass