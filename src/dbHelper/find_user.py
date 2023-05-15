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
            print("Login Successfully")
            return output
        else:
            print("Login failed")
            return None
        

def find_user_by_card_id(card_id):
    user = Database().collection['users'].find_one(
        {"card_id": card_id}
    )
    if user is None:
        print("Login failed")
        return None
    return user


def find_user_by_id(id):
    output = Database().collection['users'].find_one(
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
    

def find_all_tellers():
    try:
        users = Database().collection['users'].find({'user_type': 'teller'})
        return users
    except:
        print("No teller exists in the database.")
        return None

def find_all_admins():
    try:
        users = Database().collection['users'].find({'user_type': 'admin'})
        return users
    except Exception as e:
        print(e)
        return None