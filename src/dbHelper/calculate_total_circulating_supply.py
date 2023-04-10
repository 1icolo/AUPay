from .database import Database
from bson import ObjectId
from .compute_user_balance import compute_user_balance


def calculate_total_circulating_supply():
    total_circulation_supply = 0.0
    for user in Database().collection['users'].find():
        user_id = user['_id']
        result = compute_user_balance(user_id)
        if result is None:
            result = float(0.0)
        total_circulation_supply += result
    return total_circulation_supply
