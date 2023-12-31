
import json
import csv
import requests


def get_player_stats_by_season(season: str, player_id: int):
    if player_id is None:
        return None
    response = requests.get(
        f"https://www.balldontlie.io/api/v1/stats?player_ids[]={player_id}&seasons[]={season}",
        timeout=5)
    response_json = response.json()

    with open('playerseasonstats.json', 'w', encoding='utf-8') as outfile:
        json.dump(response_json, outfile, sort_keys=True, indent=4)

    data = response_json.get('data', [])
    if not data:
        return None

    csv_file = 'playerseasonstats.csv'
    csv_columns = list(data[0].keys())  # Get column names from the first item

    try:
        with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
    except IOError:
        print("I/O error")

    return response_json
