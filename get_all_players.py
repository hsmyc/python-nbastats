import json
import time
import requests


all_players = []


def player_search():
    page = 1
    print('Getting all players...')
    all_players = []
    response = requests.get(
        "https://www.balldontlie.io/api/v1/players",
        timeout=5)
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    response_json: dict = response.json()
    total_pages = response_json['meta']['total_pages']
    while page <= total_pages:
        response = requests.get(
            "https://www.balldontlie.io/api/v1/players?page=" + str(page),
            timeout=5)
        if response.status_code != 200:
            raise Exception('API response: {}'.format(response.status_code))
        time.sleep(1.01)
        response_json: dict = response.json()
        players = response_json['data']
        for player in players:
            all_players.append(player)
        page += 1
    if len(response_json['data']) == 0:
        return
    with open('allplayers.json', 'w') as outfile:
        json.dump(all_players, outfile)
    print('Done getting all players.')
    return all_players
