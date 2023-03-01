from .database import Database


def update_user(user):
    Database().collection['users'].update_one(
        {"_id": user['_id']},
        {"$set": {
            user
        }}
    )
    print(f"User {user['school_id']} updated")
    return True
