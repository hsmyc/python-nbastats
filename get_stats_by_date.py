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
        'page': 1,
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
        fieldnames = [
            'name', 'id', 'ast', 'blk', 'dreb', 'fg3_pct', 'fg3a', 'fg3m', 'fg_pct', 'fga', 'fgm', 'ft_pct', 'fta', 'ftm',
            'game_id', 'game_date', 'home_team_id', 'home_team_score', 'visitor_team_id', 'visitor_team_score',
            'min', 'oreb', 'pf',  'pts', 'reb', 'stl',
            'team_id', 'team_abbreviation', 'turnover'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in all_stats:
            row = {
                'name': item['player']['first_name']+" " + item['player']['last_name'],
                'id': item['player']['id'],
                'ast': item['ast'],
                'blk': item['blk'],
                'dreb': item['dreb'],
                'fg3_pct': item['fg3_pct'],
                'fg3a': item['fg3a'],
                'fg3m': item['fg3m'],
                'fg_pct': item['fg_pct'],
                'fga': item['fga'],
                'fgm': item['fgm'],
                'ft_pct': item['ft_pct'],
                'fta': item['fta'],
                'ftm': item['ftm'],
                'game_id': item['game']['id'],
                'game_date': item['game']['date'],
                'home_team_id': item['game']['home_team_id'],
                'home_team_score': item['game']['home_team_score'],
                'visitor_team_id': item['game']['visitor_team_id'],
                'visitor_team_score': item['game']['visitor_team_score'],
                'min': item['min'],
                'oreb': item['oreb'],
                'pf': item['pf'],
                'pts': item['pts'],
                'reb': item['reb'],
                'stl': item['stl'],
                'team_id': item['team']['id'],
                'team_abbreviation': item['team']['abbreviation'],
                'turnover': item['turnover']
            }
            writer.writerow(row)
    print('Stats saved to statsdata.json and statsdata.csv')
    return all_stats
