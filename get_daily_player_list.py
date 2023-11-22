import requests
import json


def dfs_players():
    players = requests.get(
        'https://dfyql-ro.sports.yahoo.com/v2/external/playersFeed/nba',
        timeout=5)
    response_json: dict = players.json()

    players_filtered = response_json['players']['result']

    return players_filtered
