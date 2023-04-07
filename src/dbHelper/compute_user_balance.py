from .database import Database
from bson import ObjectId


def compute_user_balance(user_id):
    balance = Database().collection['transactions'].aggregate([
        {
            '$match': {
                '$or': [
                    {
                        'source_id': ObjectId(user_id)
                    }, {
                        'destination_id': ObjectId(user_id)
                    }
                ]
            }
        }, {
            '$group': {
                '_id': ObjectId(user_id),
                'balance': {
                    '$sum': {
                        '$cond': [
                            {
                                '$eq': [
                                    '$source_id', '$destination_id'
                                ]
                            }, float(0.00), {
                                '$cond': [
                                    {
                                        '$eq': [
                                            '$destination_id', ObjectId(
                                                user_id)
                                        ]
                                    }, '$amount', {
                                        '$multiply': [
                                            -1, '$amount'
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        }
    ])
    for result in balance:
        return result['balance']
