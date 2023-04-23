from .database import Database


def add_user(user):
    if user is None:
        print("Add user failed.")
        return None
    try:
        new_user = Database().collection['users'].insert_one(
            user
        )
        print(f"User {user['school_id']} added.")
        return new_user.inserted_id
    except Exception as e:
        print(f"Add user failed. \n{e}")
        return None
    
