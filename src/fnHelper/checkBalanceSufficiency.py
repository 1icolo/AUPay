from dbHelper.compute_user_balance import compute_user_balance

def checkBalanceSufficiency(user_id, transactionAmount):
    if compute_user_balance(user_id) < transactionAmount:
        return False
    return True