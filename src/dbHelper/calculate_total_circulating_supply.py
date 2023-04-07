from .database import Database
from bson import ObjectId


def calculate_total_circulating_supply():
    total_circulation_supply = 0

    for user in Database().collection['users'].find():
        user_id = user['_id']
        result = Database().collection['transactions'].aggregate([
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
        for doc in result:
            total_circulation_supply += doc['balance']*-1
            return total_circulation_supply
