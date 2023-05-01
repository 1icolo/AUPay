from .database import Database
from .compute_user_balance import compute_user_balance


def update_user(user):
    try:
        Database().collection['users'].update_one(
            {"_id": user['_id']},
            {"$set": 
                user
            }
        )
        print(f"User {user['_id']} updated.")
        return True
    except Exception as e:
        print(f"Update user failed.\n{e}")
        return False

def update_balance(user):
    user_balance = compute_user_balance(user['_id'])
    if user_balance is None:
        user_balance = float(0.00)
    try:
        Database().collection['users'].update_one(
            {"_id": user['_id']},
            {"$set": {
                "balance": float(user_balance)}
            }
        )
        print(f"User {user['_id']} balance updated.")
    except Exception as e:
        print(f"Update balance error.\n{e}")

def update_all_balance():
    try:
        for user in Database().collection['users'].find():
            update_balance(user)
        print("All user balance updated.")
    except Exception as e:
        print(f"Update all balance error.\n{e}")