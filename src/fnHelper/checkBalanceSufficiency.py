from dbHelper.compute_user_balance import compute_user_balance
from dbHelper.find_user import find_user_by_id, find_user_by_id

def checkBalanceSufficiency(user_id, transactionAmount, credit = False):
    user_balance = compute_user_balance(user_id)
    if credit:
        user_max_credit = find_user_by_id(user_id)['max_credit']
    else:
        user_max_credit = 0
    total_amount_available = user_balance + user_max_credit
    print(total_amount_available)
    try:
        if total_amount_available < transactionAmount:
            return False
        return True
    except Exception as e:
        print(f"check balance sufficiency error.\n{e}")