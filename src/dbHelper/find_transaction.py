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
