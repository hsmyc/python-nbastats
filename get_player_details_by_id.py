# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import json
import requests
from find_player_id import find_player_id


def get_player_details_by_id(first_name: str, last_name: str, team: str):
    player_id = find_player_id(first_name, last_name, team)
    if player_id is None:
        return None
    response = requests.get(
        f"https://www.balldontlie.io/api/v1/players/{player_id}",
        timeout=5)
    response_json: dict = response.json()
    with open('playerdata.json', 'w', encoding='utf-8') as outfile:
        json.dump(response_json, outfile, sort_keys=True, indent=4)
    return response_json
