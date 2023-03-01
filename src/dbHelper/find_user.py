from .database import Database


def find_user(id, password):
    output = Database().collection['users'].find_one(
        # {"school_id": id},
        {"school_id": id, "password": password}
    )
    if output is None:
        print("Login failed")
    else:
        if password == output["password"]:
            return output
        else:
            print("Login failed")