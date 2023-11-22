import requests
import json


def dfs_players():
    players = requests.get(
        'https://dfyql-ro.sports.yahoo.com/v2/external/playersFeed/nba',
        timeout=5)
    response_json: dict = players.json()

    players_filtered = response_json['players']['result']

    with open('players.json', 'w', encoding='utf-8') as outfile:
        json.dump(players_filtered, outfile, sort_keys=True, indent=4)
    return players_filtered
