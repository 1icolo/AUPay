from .database import Database


def add_transaction(transaction):
    if transaction is None:
        print("Add transaction failed.")
        return None
    new_transaction = Database().collection['transactions'].insert_one(
        transaction
    )
    print(f"Transaction {new_transaction.inserted_id} added.")
    return new_transaction.inserted_id
