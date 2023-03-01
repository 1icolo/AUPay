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
            # print("Login successful")
            # print(output['card_id'])
            # print(output['user_type'])
            return output['user_type']
        else:
            print("Login failed")