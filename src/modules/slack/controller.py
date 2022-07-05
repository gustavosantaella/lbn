from app import application as app
from slack import WebClient
from src.config.config import SLACK_BOT_USER_TOKEN
from flask import jsonify

slack = WebClient(token=SLACK_BOT_USER_TOKEN)

@app.get('/')
def start_bot():
    return jsonify(2)