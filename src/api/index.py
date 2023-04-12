from flask import Flask, request, Response
from flask_pymongo import PyMongo
from bson import json_util, ObjectId, Timestamp
from datetime import datetime


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/aupaydb"
mongo = PyMongo(app)


def to_json(data):
    return Response(
        json_util.dumps(data),
        mimetype='application/json'
    )


@app.route('/transactions', methods=['GET'])
def get_all_transactions():
    if request.method == 'GET':
        try:
            transactions = mongo.db.transactions.find()
            return to_json({'transactions': list(transactions)})
        except Exception as e:
            print(f"get_all_transactions() GET error\n{e}")


@app.route('/transactions/<user_id>', methods=['GET'])
def get_all_user_transactions(user_id):
    if request.method == 'GET':
        user_id = ObjectId(user_id)
        try:
            transactions = mongo.db.transactions.find({
                "$or": [
                    {'source_id': user_id},
                    {'destination_id': user_id}
                ]
            })
            return to_json({'transactions': list(transactions)})
        except Exception as e:
            print(f"get_all_user_transactions() GET error\n{e}")
    

@app.route('/transaction', methods=['POST'])
def add_transaction():
    if request.method == 'POST':
        try:
            transaction = request.json
            new_transaction = {
                'timestamp': Timestamp(int(datetime.today().timestamp()), 1),
                'source_id': ObjectId(transaction['source_id']),
                'destination_id': ObjectId(transaction['destination_id']),
                'amount': float(transaction['amount']),
                'description': str(transaction['description']),
            }
            mongo.db.transactions.insert_one(new_transaction)
            return to_json({'message': 'Transaction added'})
        except Exception as e:
            print(f"add_transaction() POST error\n{e}")


@app.route('/transaction/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    if request.method == 'GET':
        try:
            transaction = mongo.db.transactions.find_one({'_id': ObjectId(transaction_id)})
            return to_json(transaction)
        except Exception as e:
            print(f"get_transaction GET error\n{e}")


if __name__ == '__main__':
    app.run(host='localhost', port=3000)