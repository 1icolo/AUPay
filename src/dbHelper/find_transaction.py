from .database import Database
from bson import ObjectId


def find_transaction(transaction_id):
    try:
        transaction = Database().collection['transactions'].find_one(
            {"_id": ObjectId(transaction_id)}
        )
        return transaction
    except:
        print("Transaction doesn't exist")
        return None


def find_all_transactions():
    try:
        transactions = Database().collection['transactions'].find()
        return transactions
    except:
        print("No transaction exists in the database.")
        return None


def find_all_transactions_aggregated():
    try:
        pipeline = [
            {
                '$lookup': {
                    'from': 'users',
                    'localField': 'source_id',
                    'foreignField': '_id',
                    'as': 'source_id'
                }
            }, {
                '$lookup': {
                    'from': 'users',
                    'localField': 'destination_id',
                    'foreignField': '_id',
                    'as': 'destination_id'
                }
            }, {
                '$addFields': {
                    'source_id': {
                        '$arrayElemAt': [
                            '$source_id', 0
                        ]
                    },
                    'destination_id': {
                        '$arrayElemAt': [
                            '$destination_id', 0
                        ]
                    }
                }
            }, {
                '$project': {
                    '_id': 1,
                    'timestamp': 1,
                    'source_id': '$source_id.school_id',
                    'destination_id': '$destination_id.school_id',
                    'amount': 1,
                    'description': 1
                }
            }, {
                '$addFields': {
                    'source_id': {
                        '$ifNull': [
                            '$source_id', 'COINBASE'
                        ]
                    },
                    'destination_id': {
                        '$ifNull': [
                            '$destination_id', 'COINBASE'
                        ]
                    }
                }
            },
            {
                '$sort': {
                    'timestamp': 1
                }
            }

        ]
        transactions = Database(
        ).collection['transactions'].aggregate(pipeline)
        return transactions
    except Exception as e:
        print(e)
        return None


def find_all_transactions_of_user(user):
    user['_id'] = ObjectId(user['_id'])
    try:
        transactions = Database().collection['transactions'].find({
            "$or": [
                {'source_id': user['_id']},
                {'destination_id': user['_id']}
            ]
        })
        return transactions
    except:
        print("Finding transactions failed.")
        return None


def find_all_transactions_of_user_aggregated(user):
    user['_id'] = ObjectId(user['_id'])
    try:
        pipeline = [
            {
                '$match': {
                    "$or": [
                        {'source_id': user['_id']},
                        {'destination_id': user['_id']}
                    ]
                }
            },
            {
                '$lookup': {
                    'from': 'users',
                    'localField': 'source_id',
                    'foreignField': '_id',
                    'as': 'source_id'
                }
            },
            {
                '$lookup': {
                    'from': 'users',
                    'localField': 'destination_id',
                    'foreignField': '_id',
                    'as': 'destination_id'
                }
            },
            {
                '$addFields': {
                    'source_id': {
                        '$arrayElemAt': [
                            '$source_id', 0
                        ]
                    },
                    'destination_id': {
                        '$arrayElemAt': [
                            '$destination_id', 0
                        ]
                    }
                }
            },
            {
                '$project': {
                    '_id': 1,
                    'timestamp': 1,
                    'source_id': '$source_id.school_id',
                    'destination_id': '$destination_id.school_id',
                    'amount': 1,
                    'description': 1
                }
            },
            {
                '$addFields': {
                    'source_id': {
                        '$ifNull': [
                            '$source_id', 'COINBASE'
                        ]
                    },
                    'destination_id': {
                        '$ifNull': [
                            '$destination_id', 'COINBASE'
                        ]
                    }
                }
            },
            {
                '$addFields': {
                    'amount': {
                        '$cond': [
                            {'$eq': ['$source_id', user['school_id']]},
                            {'$multiply': ['$amount', -1]},
                            '$amount'
                        ]
                    }
                }
            },
            {
                '$sort': {
                    'timestamp': 1
                }
            }

        ]
        transactions = Database(
        ).collection['transactions'].aggregate(pipeline)
        return transactions
    except Exception as e:
        print(f"Finding transactions failed.\n{e}")
        return None


def find_chargeback_transactions(id):
    try:
        pipeline = [
            {
                "$match": {
                    "description": {
                        "$regex": f"chargeback {id}",
                        "$options": "i"
                    }
                }
            }
        ]
        transactions = Database(
            ).collection['transactions'].aggregate(pipeline)
        return transactions
    except Exception as e:
        print(f"Finding chargeback transactions failed.\n{e}")
        return None
