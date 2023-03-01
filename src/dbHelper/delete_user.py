from .database import Database


def delete_user(user_id):
    try:
        Database().collection['users'].delete_one(
            {"_id": user_id}
        )
        print("User deleted")
        return True
    except:
        print("User delete failed")
        return None
