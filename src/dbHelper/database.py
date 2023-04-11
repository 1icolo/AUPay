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
        except Exception as e:
            print(f"Error: \n{e}")

    # Initial collection documents
    def __create_database(self):
        coinbase = ObjectId('ffffffffffffffffffffffff')
        admin = ObjectId('000000000000000000000000')
        self.database.create_collection('users', validator=user_schema)
        self.database.create_collection('transactions', validator=transaction_schema)
        
        documents = {
            'user': {
                '_id': admin,
                'card_id': "7f453b1936a11e152d5cd96c66cdd4caf13024c390509f71daf5410c1d742986",
                'school_id': "AUP52023BSIT",
                'password': "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",
                'otp_key': "d1d3b9e6f7a4a8c8d3f5e2c3b2a1d0c7f6e5d4c3b2a190807060504030201000",
                'user_type': 'admin',
                'balance': float(0.00),
            },
            'transaction': {
                'timestamp': Timestamp(1651363200, 0),
                'source_id': coinbase,
                'destination_id': admin,
                'amount': float(0.00),
                'description': "Coinbase transaction",
            }
        }
        self.collection['users'].insert_one(documents['user'])
        self.collection['transactions'].insert_one(documents['transaction'])
        print("Initial database created.")


user_schema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['_id', 'card_id', 'school_id', 'password', 'otp_key', 'user_type'],
        'properties': {
            '_id': {
                'bsonType': 'objectId'
            },
            'card_id': {
                'bsonType': 'string',
                'pattern': '^[a-fA-F0-9]{64}$'
            },
            'school_id': {
                'bsonType': 'string',
            },
            'password': {
                'bsonType': 'string',
                'pattern': '^[a-fA-F0-9]{64}$'
            },
            'otp_key': {
                'bsonType': 'string',
                'pattern': '^[a-fA-F0-9]{64}$'
            },
            'user_type': {
                'enum': ['admin', 'user', 'business', 'teller']
            },
            'balance': {
                'bsonType': 'double',
                'minimum': 0,
                'default': 0
            }
        }
    }
}

transaction_schema = {
    '$jsonSchema': {
        'bsonType': 'object',
        'required': ['timestamp', 'source_id', 'destination_id', 'amount', 'description'],
        'properties': {
            'timestamp': {
                # 'bsonType': 'int'
            },
            'source_id': {
                'bsonType': 'objectId'
            },
            'destination_id': {
                'bsonType': 'objectId'
            },
            'amount': {
                'bsonType': 'double',
                'minimum': 0
            },
            'description': {
                'bsonType': 'string',
                'minLength': 1
            }
        }
    }
}