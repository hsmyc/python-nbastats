import json
import requests


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


all_players = []


def player_search(name: str):
    if 'jr' in name.lower():
        name = name.replace(' Jr.', '')
    if 'sr' in name.lower():
        name = name.replace(' Sr.', '')
    parameters = {
        'search': name,
    }
    response = requests.get(
        "https://www.balldontlie.io/api/v1/players",
        params=parameters,
        timeout=5)
    if response.status_code != 200:
        raise Exception('API response: {}'.format(response.status_code))
    response_json: dict = response.json()
    if len(response_json['data']) == 0:
        return
    players = response_json['data']
    return players
