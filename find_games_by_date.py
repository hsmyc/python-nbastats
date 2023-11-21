import json
import csv
import requests


def find_games_by_date(date: str):
    parameters = {
        'dates[]': date,
        'page': 0,
    }
    response = requests.get(
        "https://www.balldontlie.io/api/v1/games",
        params=parameters,
        timeout=5)
    response_json: dict = response.json()
    all_games = response_json['data']
    total_pages = response_json['meta']['total_pages']
    while total_pages >= parameters['page']:
        parameters['page'] += 1
        response = requests.get(
            "https://www.balldontlie.io/api/v1/games",
            params=parameters,
            timeout=5)
        response_json: dict = response.json()
        all_games.extend(response_json['data'])
    with open('gamesdata.json', 'w', encoding='utf-8') as outfile:
        json.dump(all_games, outfile, sort_keys=True, indent=4)
    with open('gamesdata.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('gamesdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'date', 'home_team_id', 'home_team_score', 'period', 'postseason', 'season', 'status',
                         'time', 'visitor_team_id', 'visitor_team_score'])
        for i in range(len(data)):
            writer.writerow([data[i]['id'], data[i]['date'], data[i]['home_team']['full_name'], data[i]['home_team']['id'], data[i]['home_team_score'],
                             data[i]['period'], data[i]['postseason'], data[i]['season'], data[i]['status'],
                             data[i]['time'], data[i]['visitor_team']['full_name'], data[i]['visitor_team']['id'], data[i]['visitor_team_score']])
    return all_games
