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
                'card_id': "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                'school_id': "",
                'password': "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                'otp_key': "D9SADSDJER3D",
                'user_type': 'admin',
                'balance': 0.00,
            },
            'transaction': {
                'timestamp': Timestamp(1651363200, 0),
                'source_id': ObjectId("63abc434a689ea6865853eb8"),
                'destination_id': ObjectId("63abc435a689ea6865853eb9"),
                'amount': 0.00,
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
