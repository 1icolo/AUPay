from .database import Database
from .compute_user_balance import compute_user_balance


def update_user(user):
    Database().collection['users'].update_one(
        {"_id": user['_id']},
        {"$set": 
            user
        }
    )
    print(f"User {user['_id']} updated.")
    return True
def update_balance(user):
    Database().collection['users'].update_one(
        {"_id": user['_id']},
        {"$set": {
            "balance": compute_user_balance(user['_id'])}
        }
    )
    print(f"User {user['_id']} updated.")
    return True
def update_all_balance(user):
    updated = Database().collection['users'].update_many(
        {"_id": user['_id']},
        {"$set": {
            "balance": compute_user_balance(user['_id'])}
        }
    )
    print(f"{updated.modified_count} balance updated.")
    return True
