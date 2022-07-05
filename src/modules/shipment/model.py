from datetime import datetime

import bson

from src.database.db import Database

# datetime.today().strftime('%Y-%m-%d')
date = "2022-07-04"


class Shipment(Database):
    doc = 'shipments'

    def __init__(self):
        super().__init__(self.doc)

    def get(self, id):
        return self.document().aggregate([
            {
                "$match": {
                    "isActive": True,
                    'loadboards': {
                        "$elemMatch": {
                            "loadboardId": bson.objectid.ObjectId(id),
                            "status": "Posted"
                        }
                    },
                    'shipper.date': {
                        "$gte": datetime.strptime(date, '%Y-%m-%d')
                    }
                }
            },
            {
                "$lookup": {
                    "from": "users",
                    "localField": "userId",
                    "foreignField": "_id",
                    "as": "userInfo"
                }
            },
            {
                "$project": {"userInfo": 1}
            },
            {
                "$unwind": "$userInfo"
            },
            {
                "$group": {
                    "_id": "$userInfo",
                    "count": {"$sum": 1},
                }
            }
        ])

    def activeLoadsGroupedByLoadBoardsStatus(self):
        loads_results = self.document().aggregate([
            {
                "$match": {
                    "isActive": True,
                    'shipper.date': {
                        "$gte": datetime.strptime(date, '%Y-%m-%d')
                    }
                }
            },
            {
                "$lookup": {
                    "from": "users",
                    "localField": "userId",
                    "foreignField": "_id",
                    "as": "userInfo"
                }
            },
            {
                "$project": {"userInfo": 1}
            },
            {
                "$unwind": "$userInfo"
            },
            {
                "$group": {
                    "_id": "$userInfo",
                    "count": {"$sum": 1},
                }
            }
        ])

        return loads_results

    def usersWithLoadsPostedAsOf(self):
        loads_result = self.document().aggregate([
            {
                "$match": {
                    "isActive": True,
                    'shipper.date': {
                        "$gte": datetime.strptime(date, '%Y-%m-%d')
                    }
                }
            },
            {
                "$lookup": {
                    "from": "users",
                    "localField": "userId",
                    "foreignField": "_id",
                    "as": "userInfo"
                }
            },
            {
                "$project": {"userInfo": 1}
            },
            {
                "$unwind": "$userInfo"
            },
            {
                "$group": {
                    "_id": "$userInfo",
                    "count": {"$sum": 1},
                }
            }
        ])

        return loads_result

    def usersWithLoadsPostedAsOfTodayToTruckerPath(self):
        return self.document().aggregate([
            {
                "$match": {
                    "isActive": True,
                    'loadboards': {
                        "$elemMatch": {
                            "loadboardId": bson.objectid.ObjectId(id),
                            "status": "Posted"
                        }
                    },
                    'shipper.date': {
                        "$gte": datetime.strptime(date, '%Y-%m-%d')
                    }
                }
            },
            {
                "$lookup": {
                    "from": "users",
                    "localField": "userId",
                    "foreignField": "_id",
                    "as": "userInfo"
                }
            },
            {
                "$project": {"userInfo": 1}
            },
            {
                "$unwind": "$userInfo"
            },
            {
                "$group": {
                    "_id": "$userInfo",
                    "count": {"$sum": 1},
                }
            }
        ])


shipment = Shipment()
