# Package Imports
from pymongo import MongoClient
from bson import Timestamp, ObjectId
from dotenv import load_dotenv

from os import getenv

load_dotenv()
connection_string = getenv('DB_URI')


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

    def findUser(self, id, password):
        output = self.collection['users'].find_one(
            # {"school_id": id},
            {"school_id": id, "password": password}
        )
        if output is None:
            print("Login failed")
        else:
            if password == output["password"]:
                print("Login successful")
                print(output['card_id'])
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
