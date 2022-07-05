from flask import jsonify

from app import application as app
import src.modules.loadboard.service as loadboard_service

@app.get('/loadboard/report-1')
def usersWithUsernameLoadsPosted():
    response = loadboard_service.usersWithUsernameLoadsPosted()
    return jsonify(response)

@app.get('/loadboard/report-2')
def activeLoadsGroupedByLoadBoardStatus():
    response = loadboard_service.activeLoadsGroupedByLoadBoardStatus()
    return jsonify(response)

@app.get('/loadboard/report-3')
def usersWithLoadsPostedAsOfToday():
    response = loadboard_service.usersWithLoadsPostedAsOfToday()
    return jsonify(response)

@app.get('/loadboard/report-4')
def usersWithLoadsPostedAsOfTodayToTruckerPath():
    response = loadboard_service.usersWithLoadsPostedAsOfTodayToTruckerPath()
    return jsonify(response)