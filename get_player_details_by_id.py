# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import json
import csv
import requests


def get_player_details_by_id(player_id: int):
    if player_id is None:
        return None
    response = requests.get(
        f"https://www.balldontlie.io/api/v1/players/{player_id}",
        timeout=5)
    response_json: dict = response.json()
    with open('playerdata.json', 'w', encoding='utf-8') as outfile:
        json.dump(response_json, outfile, sort_keys=True, indent=4)
    with open('playerdata.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('playerdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['player_id', 'first_name', 'last_name', 'position', 'height_feet', 'height_inches',
                         'weight_pounds', 'team_id', 'team_name', 'team_city', 'team_conference', 'team_division'])
        writer.writerow([data['id'], data['first_name'], data['last_name'], data['position'], data['height_feet'],
                         data['height_inches'], data['weight_pounds'], data['team']['id'], data['team']['name'],
                         data['team']['city'], data['team']['conference'], data['team']['division']])
    return response_json
