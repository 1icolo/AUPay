from .database import Database


def get_all_transactions():
    try:
        users = Database().collection['users'].find()
        return users
    except:
        print("No user exists in the database.")
        return None