from dbHelper import find_user_by_login

def login_attempt(id, password):
    user = find_user_by_login(id, password)
    return user
