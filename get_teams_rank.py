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
    with open('teamrank.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            "TEAM_ID",
            "TEAM_NAME",
            "GP",
            "W",
            "L",
            "W_PCT",
            "PLUS_MINUS",
            "W_PCT_RANK",
            "OPP_FG_PCT_RANK",
            "OPP_FG3M_RANK",
            "OPP_FG3_PCT_RANK",
            "OPP_FT_PCT_RANK",
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
        for row in rows:
            writer.writerow({
                "TEAM_ID": row[headers.index('TEAM_ID')],
                "TEAM_NAME": row[headers.index('TEAM_NAME')],
                "GP": row[headers.index('GP')],
                "W": row[headers.index('W')],
                "L": row[headers.index('L')],
                "W_PCT": row[headers.index('W_PCT')],
                "PLUS_MINUS": row[headers.index('PLUS_MINUS')],
                "W_PCT_RANK": row[headers.index('W_PCT_RANK')],
                "OPP_FG_PCT_RANK": row[headers.index('OPP_FG_PCT_RANK')],
                "OPP_FG3M_RANK": row[headers.index('OPP_FG3M_RANK')],
                "OPP_FG3_PCT_RANK": row[headers.index('OPP_FG3_PCT_RANK')],
                "OPP_FT_PCT_RANK": row[headers.index('OPP_FT_PCT_RANK')],
                "OPP_REB_RANK": row[headers.index('OPP_REB_RANK')],
                "OPP_AST_RANK": row[headers.index('OPP_AST_RANK')],
                "OPP_TOV_RANK": row[headers.index('OPP_TOV_RANK')],
                "OPP_STL_RANK": row[headers.index('OPP_STL_RANK')],
                "OPP_BLK_RANK": row[headers.index('OPP_BLK_RANK')],
                "OPP_BLKA_RANK": row[headers.index('OPP_BLKA_RANK')],
                "OPP_PF_RANK": row[headers.index('OPP_PF_RANK')],
                "OPP_PFD_RANK": row[headers.index('OPP_PFD_RANK')],
                "OPP_PTS_RANK": row[headers.index('OPP_PTS_RANK')],
                "PLUS_MINUS_RANK": row[headers.index('PLUS_MINUS_RANK')]
            })

    print('Done!')


get_teams_rank()
