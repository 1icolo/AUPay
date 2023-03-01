from dbHelper import find_user

def login_attempt(id, password):
    user = find_user(id, password)
    return user
