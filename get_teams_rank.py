import json
import csv
import requests
import time
import requests


def get_teams_rank():
    print('Getting teams rank...')
    url = 'https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType=Opponent&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2023-24&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision='
    headers = {
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response_json: dict = response.json()
    result_sets = response_json['resultSets']
    headers = result_sets[0]['headers']
    rows = result_sets[0]['rowSet']
    all_stats = []
    for row in rows:
        stats = dict(zip(headers, row))
        all_stats.append(stats)
    with open('teamrank.json', 'w', encoding='utf-8') as outfile:
        json.dump(all_stats, outfile, sort_keys=True, indent=4)
    with open('teamrank.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('teamrank.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "TEAM_ID",
            "TEAM_NAME",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "OPP_FGM",
            "OPP_FGA",
            "OPP_FG_PCT",
            "OPP_FG3M",
            "OPP_FG3A",
            "OPP_FG3_PCT",
            "OPP_FTM",
            "OPP_FTA",
            "OPP_FT_PCT",
            "OPP_OREB",
            "OPP_DREB",
            "OPP_REB",
            "OPP_AST",
            "OPP_TOV",
            "OPP_STL",
            "OPP_BLK",
            "OPP_BLKA",
            "OPP_PF",
            "OPP_PFD",
            "OPP_PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "OPP_FGM_RANK",
            "OPP_FGA_RANK",
            "OPP_FG_PCT_RANK",
            "OPP_FG3M_RANK",
            "OPP_FG3A_RANK",
            "OPP_FG3_PCT_RANK",
            "OPP_FTM_RANK",
            "OPP_FTA_RANK",
            "OPP_FT_PCT_RANK",
            "OPP_OREB_RANK",
            "OPP_DREB_RANK",
            "OPP_REB_RANK",
            "OPP_AST_RANK",
            "OPP_TOV_RANK",
            "OPP_STL_RANK",
            "OPP_BLK_RANK",
            "OPP_BLKA_RANK",
            "OPP_PF_RANK",
            "OPP_PFD_RANK",
            "OPP_PTS_RANK",
            "PLUS_MINUS_RANK"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print('Done!')


get_teams_rank()
