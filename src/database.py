# Package Imports
from pymongo import MongoClient
from bson import Timestamp, ObjectId
from dotenv import load_dotenv
from datetime import datetime

from os import getenv

load_dotenv()
connection_string = getenv('mongodb://localhost:27017')


class Database:
    def __init__(self):
        self.client = MongoClient(connection_string)
        self.database = self.client['aupaydb']
        self.collection = {
            'users': self.database['users'],
            'transactions': self.database['transactions']
        }
        try:
            if not self.client.list_database_names().__contains__('aupaydb'):
                self.__create_database()
        except Exception:
            print("Error: " + Exception)

    # Initial collection documents
    def __create_database(self):
        documents = {
            'user': {
                'card_id': "1234567890",
                'school_id': "0000000",
                'password': "12345",
                'otp_key': "1a2b3c4b5d",
                'user_type': 'user',
                'balance': '35',
            },
            'transaction': {
                'timestamp': Timestamp(1651363200, 0),
                'source_id': ObjectId("63abc434a689ea6865853eb8"),
                'destination_id': ObjectId("63abc435a689ea6865853eb9"),
                'amount': 0,
                'description': "Initial transaction",
            }
        }
        self.collection['users'].insert_one(documents['user'])
        self.collection['transactions'].insert_one(documents['transaction'])
        print("Initial database created.")

    def find_user(self, id, password):
        output = self.collection['users'].find_one(
            # {"school_id": id},
            {"school_id": id, "password": password}
        )
        if output is None:
            print("Login failed")
        else:
            if password == output["password"]:
                # print("Login successful")
                # print(output['card_id'])
                # print(output['user_type'])
                return output['user_type']
            else:
                print("Login failed")

    def add_user(self, user):
        if user is None:
            print("Add user failed.")
            return None
        new_user = self.collection['users'].insert_one(
            user
        )
        print(f"User {new_user['school_id']} added.")
        return new_user.inserted_id

    def update_user(self, user):
        self.collection['users'].update_one(
            {"_id": user['_id']},
            {"$set": {
                user
            }}
        )
        print(f"User {user['school_id']} updated")
        return True

    def delete_user(self, user_id):
        try:
            self.collection['users'].delete_one(
                {"_id": user_id}
            )
            print("User deleted")
            return True
        except:
            print("User delete failed")
            return None

    def find_transaction(self, transaction_id):
        try:
            transaction = self.collection['transactions'].find_one(
                {"_id": ObjectId(transaction_id)}
            )
            return transaction
        except:
            print("Transaction doesn't exist")
            return None

    def add_transaction(self, transaction):
        if transaction is None:
            print("Add transaction failed.")
            return None
        new_transaction = self.collection['transactions'].insert_one(
            transaction
        )
        print(f"Transaction {new_transaction.inserted_id} added.")
        return new_transaction.inserted_id

    def load_user_table(self):
        load_users = self.collection['users'].find()
        users_data = []
        for users in load_users:
            users_data.append([users['card_id'],users['school_id'],users['password'],users['otp_key'],users['user_type'],users['balance']]) 
        # print(user_data)
        return users_data

    def load_transaction_table(self):
        load_transactions = self.collection['transactions'].find()
        transaction_data = []
        transactions_data = []
        for transactions in load_transactions:
            transaction_data.append([transactions['timestamp']])       
            bson_timestamp = transaction_data[0][0] 
            dt = datetime.fromtimestamp(bson_timestamp.time)
            date_string = dt.strftime("%m/%d/%y")
            transactions_data.append([transactions['_id'],date_string,transactions['source_id'],transactions['destination_id'],transactions['amount'],transactions['description']])
        # print(transactions_data)
        return transactions_data

user_validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['card_id', 'school_id', 'password', 'otp_key', 'user_type'],
        'properties': {
            'card_id': {},
            'school_id': {},
            'password': {},
            'otp_key': {},
            'user_type': {},
        }
    }
}
