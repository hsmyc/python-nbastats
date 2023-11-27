import csv
import requests


def all_player_id():
    print('Getting all player IDs...')
    url = 'https://stats.nba.com/stats/playerindex?College=&Country=&DraftPick=&DraftRound=&DraftYear=&Height=&Historical=1&LeagueID=00&Season=2023-24&SeasonType=Regular%20Season&TeamID=0&Weight='
    headers = {
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    response_json: dict = response.json()
    result_sets = response_json['resultSets']
    headers = result_sets[0]['headers']
    rows = result_sets[0]['rowSet']

    with open('allplayers.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "PERSON_ID",
            "PLAYER_LAST_NAME",
            "PLAYER_FIRST_NAME",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                "PERSON_ID": row[headers.index('PERSON_ID')],
                "PLAYER_LAST_NAME": row[headers.index('PLAYER_LAST_NAME')],
                "PLAYER_FIRST_NAME": row[headers.index('PLAYER_FIRST_NAME')],
                "TEAM_ID": row[headers.index('TEAM_ID')],
                "TEAM_NAME": row[headers.index('TEAM_NAME')],
                "TEAM_ABBREVIATION": row[headers.index('TEAM_ABBREVIATION')],
            })
    print('Done!')


all_player_id()
