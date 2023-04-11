from .database import Database
from .update_user import update_balance


def add_transaction(transaction):
    if transaction is None:
        print("Add transaction failed.")
        return None
    users = [
        {"_id": transaction['source_id']},
        {"_id": transaction['destination_id']}
    ]
    for user in users:
        update_balance(user)
    new_transaction = Database().collection['transactions'].insert_one(
        transaction
    )
    print(f"Transaction {new_transaction.inserted_id} added.")
    return new_transaction.inserted_id
