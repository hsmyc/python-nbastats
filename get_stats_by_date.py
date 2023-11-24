import json
import csv
import requests
import time


def get_stats_by_date(start_date: str, end_date: str, player_id: int):
    print(player_id)
    print('Getting stats...')
    parameters = {
        'start_date': start_date,
        'end_date': end_date,
        'page': 0,
        'player_ids[]': player_id,
    }
    response = requests.get(
        "https://www.balldontlie.io/api/v1/stats",
        params=parameters,
        timeout=20)
    print('sta: ', response.status_code)
    response_json: dict = response.json()
    all_stats = response_json['data']
    total_pages = response_json['meta']['total_pages']
    print(f'Total pages: {total_pages}')
    while total_pages >= parameters['page']:
        parameters['page'] += 1
        response = requests.get(
            "https://www.balldontlie.io/api/v1/stats",
            params=parameters,
            timeout=20)
        response_json: dict = response.json()
        all_stats.extend(response_json['data'])
        time.sleep(1.01)
    with open('statsdata.json', 'w', encoding='utf-8') as outfile:
        json.dump(all_stats, outfile, sort_keys=True, indent=4)
    with open('statsdata.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('statsdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'ast', 'blk', 'dreb', 'fg3_pct', 'fg3a', 'fg3m', 'fg_pct', 'fga', 'fgm', 'ft_pct',
                         'fta', 'ftm', 'game_id', 'min', 'oreb', 'pf', 'player_id', 'pts', 'reb', 'stl', 'team_id',
                         'turnover'])
        for i in range(len(data)):
            writer.writerow([data[i]['id'], data[i]['player']['first_name'] +
                             data[i]['player']['last_name'], data[i]['ast'], data[i]['blk'], data[i]['dreb'], data[i]['fg3_pct'],
                             data[i]['fg3a'], data[i]['fg3m'], data[i]['fg_pct'], data[i]['fga'], data[i]['fgm'],
                             data[i]['ft_pct'], data[i]['fta'], data[i]['ftm'], data[i]['game']['id'], data[i]['min'],
                             data[i]['oreb'], data[i]['pf'], data[i]['player']['id'], data[i]['pts'], data[i]['reb'],
                             data[i]['stl'], data[i]['team']['id'], data[i]['turnover']])
    print('Stats saved to statsdata.json and statsdata.csv')
    return all_stats
