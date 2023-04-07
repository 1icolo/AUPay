from .database import Database
from bson import ObjectId


def calculate_total_circulating_supply():
    total_circulation_supply = 0

    for user in Database().collection['users'].find():
        user_id = user['_id']
        pipeline = [
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
                                }, 0, {
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
        ]
        result = Database().collection['transactions'].aggregate(pipeline)
        for doc in result:
            total_circulation_supply += doc['balance']

    print(f'Total: {total_circulation_supply}')
