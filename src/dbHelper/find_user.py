from .database import Database


def find_user_by_login(id, password):
    output = Database().collection['users'].find_one(
        # {"school_id": id},
        {"school_id": id, "password": password}
    )
    if output is None:
        print("Login failed")
        return None
    else:
        if password == output["password"]:
            return output
        else:
            print("Login failed")
            return None


def find_user_by_id(id):
    output = Database().collection['users'].find_one*(
        {"_id": id}
    )
    if output is None:
        print("User doesn't exist.")
        return None
    return output


def find_all_users():
    try:
        users = Database().collection['users'].find()
        return users
    except:
        print("No user exists in the database.")
        return None