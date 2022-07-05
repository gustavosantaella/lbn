import bson

from src.database.db import Database

class LoadBoard(Database):

    doc = 'loadboards'

    def __init__(self):
        super().__init__(self.doc)


shipment = LoadBoard()