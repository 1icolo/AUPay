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
                '_id': ObjectId('641d186605e44f1dfd91f8e4'),
                'card_id': "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                'school_id': "",
                'password': "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                'otp_key': "AUP52023BSIT",
                'user_type': 'admin',
                'balance': float(0.00),
            },
            'transaction': {
                '_id': ObjectId("64283b50a7a5063923cf424b"),
                'timestamp': Timestamp(1651363200, 0),
                'source_id': ObjectId("641d186605e44f1dfd91f8e4"),
                'destination_id': ObjectId("641d186605e44f1dfd91f8e4"),
                'amount': float(0.00),
                'description': "Initial transaction",
            }
        }
        self.collection['users'].insert_one(documents['user'])
        self.collection['transactions'].insert_one(documents['transaction'])
        print("Initial database created.")


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
