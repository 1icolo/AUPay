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