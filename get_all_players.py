# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import json
import requests


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text


all_players = []


def player_search(player_first_name: str):
    parameters = {
        'search': player_first_name,
        'page': 0,
    }
    response = requests.get(
        "https://www.balldontlie.io/api/v1/players",
        params=parameters,
        timeout=5)
    response_json: dict = response.json()
    all_players.extend(response_json['data'])
    total_pages = response_json['meta']['total_pages']
    while total_pages >= parameters['page']:
        parameters['page'] += 1
        response = requests.get(
            "https://www.balldontlie.io/api/v1/players",
            params=parameters,
            timeout=5)
        response_json: dict = response.json()
        all_players.extend(response_json['data'])
    return all_players
