from dbHelper import find_user_by_login
from dbHelper import find_user_by_card_id

def login_attempt(id, password):
    user = find_user_by_login(id, password)
    return user

def login_rfid(card_id):
    user = find_user_by_card_id(card_id)
    return user