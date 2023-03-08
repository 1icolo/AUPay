from .database import Database


def get_all_transactions():
    try:
        transactions = Database().collection['transactions'].find()
        return transactions
    except:
        print("No transaction exists in the database.")
        return None