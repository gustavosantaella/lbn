import bson

from src.modules.shipment.model import shipment

load_board_id = "620dc7d2b71e7e11f41a7bbb"


# report 1
def usersWithUsernameLoadsPosted():
    response = shipment.get(load_board_id)
    loads_rows = parser(response)
    return loads_rows


# report 2
def activeLoadsGroupedByLoadBoardStatus():
    response = shipment.activeLoadsGroupedByLoadBoardsStatus()
    loads_rows = parser(response)
    return loads_rows


# report 3
def usersWithLoadsPostedAsOfToday():
    response = shipment.usersWithLoadsPostedAsOf()

    def mapping(item):
        del item['userName']
        return item

    loads_rows = list(map(mapping, parser(response)))
    return loads_rows


# report 4
def usersWithLoadsPostedAsOfTodayToTruckerPath():
    response = shipment.activeLoadsGroupedByLoadBoardsStatus()

    def mapping(item):
        del item['userName']
        return item

    loads_rows = list(map(mapping, parser(response)))
    return loads_rows


def parser(array):
    loads_rows = []
    sum = 0
    count = 0
    for load in array:
        sum = sum + load["count"]
        count = count + 1
        loads_rows.append({
            "firstName": load["_id"]["firstName"],
            "lastName": load["_id"]["lastName"],
            "phone": load["_id"]["phone"],
            "userName": load["_id"]["userName"],
            "email": load["_id"]["email"],
            "count": load["count"]
        })

    return loads_rows
