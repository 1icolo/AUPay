from .database import Database


def add_user(user):
    if user is None:
        print("Add user failed.")
        return None
    new_user = Database().collection['users'].insert_one(
        user
    )
    print(f"User {new_user['school_id']} added.")
    return new_user.inserted_id
