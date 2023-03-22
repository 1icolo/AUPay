from .database import Database
from bson import ObjectId


def compute_user_balance(user_id):
    user_id = ObjectId(user_id)
    balance = Database().collection['transactions'].aggregate([
        {
            '$match': {
                '$or': [
                    {
                        'source_id': user_id
                    }, {
                        'destination_id': user_id
                    }
                ]
            }
        }, {
            '$group': {
                '_id': user_id,
                'balance': {
                    '$sum': {
                        '$cond': [
                            {
                                '$eq': [
                                    '$destination_id', user_id
                                ]
                            }, '$amount', {
                                '$multiply': [
                                    -1, '$amount'
                                ]
                            }
                        ]
                    }
                }
            }
        }
    ])
    return balance