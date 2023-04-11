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
    try:
        Database().collection['users'].update_one(
            {"_id": user['_id']},
            {"$set": {
                "balance": compute_user_balance(user['_id'])}
            }
        )
        print(f"User {user['_id']} balance updated.")
    except Exception as e:
        print(e)

def update_all_balance():
    for user in Database().collection['users'].find():
        result = update_balance(user)
        if result is None:
            result = float(0.0)
    print("All user balance updated.")