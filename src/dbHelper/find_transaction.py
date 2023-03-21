from .database import Database
from bson import ObjectId


def find_transaction(transaction_id):
    try:
        transaction = Database().collection['transactions'].find_one(
            {"_id": ObjectId(transaction_id)}
        )
        return transaction
    except:
        print("Transaction doesn't exist")
        return None


def find_all_transactions():
    try:
        transactions = Database().collection['transactions'].find()
        return transactions
    except:
        print("No transaction exists in the database.")
        return None


def find_all_transactions_of_user(_id):
    _id = ObjectId(_id)
    try:
        transactions = Database().collection['transactions'].find({
            "$or": [
                {'source_id': _id},
                {'destination_id': _id}
            ]
        })
        return transactions
    except:
        print("Finding transactions failed.")
        return None


def load_transaction_table(self):
    load_transactions = Database().collection['transactions'].find()
    transaction_data = []
    transactions_data = []
    for transactions in load_transactions:
        transaction_data.append([transactions['timestamp']])
        bson_timestamp = transaction_data[0][0]
        from datetime import datetime
        dt = datetime.fromtimestamp(bson_timestamp.time)
        date_string = dt.strftime("%m/%d/%y")
        transactions_data.append([transactions['_id'], date_string, transactions['source_id'],
                                 transactions['destination_id'], transactions['amount'], transactions['description']])
    # print(transactions_data)
    return transactions_data
