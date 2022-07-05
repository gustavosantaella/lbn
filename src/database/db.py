import os
from pymongo import MongoClient
import pymongo


class Database:
    URI = None
    DB_NAME = None
    CLIENT = None
    db = None
    doc = None

    def __init__(self, doc):
        self.URI = os.environ.get('URI_MONGODB')
        self.DB_NAME = os.environ.get('DB_NAME')
        self.connection()
        if doc:
            self.document()

    def connection(self):
        try:
            self.CLIENT = MongoClient(self.URI)
            print('DATABASE CONNECTED')
            self.db = self.CLIENT[self.DB_NAME]
        except Exception as e:
            print('there are error')
            print('DATABASE DISCONNECTED')
            print(e)
            self.CLIENT.close()

    def document(self):
        try:
            return self.db[self.doc]
        except:
            print('An error ocurred')
            self.CLIENT.close()
