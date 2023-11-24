import json
import csv
import requests


def get_stats_by_game(game_ids: int):
    parameters = {
        'game_ids[]': game_ids,
        'page': 0,
    }
    response = requests.get(
        "https://www.balldontlie.io/api/v1/stats",
        params=parameters,
        timeout=5)
    response_json = response.json()
    all_stats = response_json['data']
    total_pages = response_json['meta']['total_pages']

    while total_pages >= parameters['page']:
        parameters['page'] += 1
        response = requests.get(
            "https://www.balldontlie.io/api/v1/stats",
            params=parameters,
            timeout=20)
        response_json = response.json()
        all_stats.extend(response_json['data'])

    with open('gamesstatsdata.json', 'w', encoding='utf-8') as outfile:
        json.dump(all_stats, outfile, sort_keys=True, indent=4)

    with open('gamesstatsdata.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'id', 'ast', 'blk', 'dreb', 'fg3_pct', 'fg3a', 'fg3m', 'fg_pct', 'fga', 'fgm', 'ft_pct', 'fta', 'ftm',
            'game_id', 'game_date', 'home_team_id', 'home_team_score', 'visitor_team_id', 'visitor_team_score',
            'min', 'oreb', 'pf', 'player_id', 'player_first_name', 'player_last_name', 'pts', 'reb', 'stl',
            'team_id', 'team_abbreviation', 'turnover'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for item in all_stats:
            row = {
                'id': item['id'],
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
                'player_id': item['player']['id'],
                'player_first_name': item['player']['first_name'],
                'player_last_name': item['player']['last_name'],
                'pts': item['pts'],
                'reb': item['reb'],
                'stl': item['stl'],
                'team_id': item['team']['id'],
                'team_abbreviation': item['team']['abbreviation'],
                'turnover': item['turnover']
            }
            writer.writerow(row)

    return all_stats
