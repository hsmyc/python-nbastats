import requests
import csv
from constants import nba_teams_abbreviations


def player_box_scores(player_infos, player_team_infos):
    all_players_box_scores = []
    opponent_team_info = []
    opponent_team_name = ''
    with open('all_players_box.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'PLAYER_NAME', "TEAM_ABBREVIATION", "SEASON_ID", "Player_ID", "Game_ID", "GAME_DATE", "MATCHUP", "WL", "MIN",
            "FGM", "FGA", "FG_PCT", "FG3M", "FG3A", "FG3_PCT", "FTM", "FTA", "FT_PCT",
            "OREB", "DREB", "REB", "AST", "STL", "BLK", "TOV", "PF", "PTS",
            "PLUS_MINUS", "VIDEO_AVAILABLE",  "TEAM_NAME", "TEAM_GP",
            "TEAM_W",
            "TEAM_L",
            "TEAM_W_PCT",
            "TEAM_PLUS_MINUS",
            "TEAM_W_PCT_RANK",
            "TEAM_OPP_FG_PCT_RANK",
            "TEAM_OPP_FG3M_RANK",
            "TEAM_OPP_FG3_PCT_RANK",
            "TEAM_OPP_FT_PCT_RANK",
            "TEAM_OPP_REB_RANK",
            "TEAM_OPP_AST_RANK",
            "TEAM_OPP_TOV_RANK",
            "TEAM_OPP_STL_RANK",
            "TEAM_OPP_BLK_RANK",
            "TEAM_OPP_BLKA_RANK",
            "TEAM_OPP_PF_RANK",
            "TEAM_OPP_PFD_RANK",
            "TEAM_OPP_PTS_RANK",
            "TEAM_PLUS_MINUS_RANK"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player_info in player_infos:
            player_id = player_info['id']
            url = f'https://stats.nba.com/stats/playergamelog?DateFrom=&DateTo=&LeagueID=00&PlayerID={player_id}&Season=2023-24&SeasonType=Regular%20Season'
            headers = {
                'Referer': 'https://www.nba.com/',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                print(f'Error getting box score for player {player_id}')
                continue
            response_json = response.json()
            result_sets = response_json['resultSets']
            headers = result_sets[0]['headers']
            rows = result_sets[0]['rowSet']
            for row in rows:
                opponent_team_abbreviation = row[headers.index('MATCHUP')].split(
                    ' ')[2]
                if opponent_team_abbreviation in nba_teams_abbreviations:
                    opponent_team_name = nba_teams_abbreviations[opponent_team_abbreviation]
                    opponent_team_info = next(
                        (team for team in player_team_infos if team['TEAM_NAME'] == opponent_team_name), None)

                    if opponent_team_info is not None:
                        player_data = {
                            "PLAYER_NAME": player_info['name'],
                            "TEAM_ABBREVIATION": player_info['team'],
                            "SEASON_ID": row[headers.index('SEASON_ID')],
                            "Player_ID": row[headers.index('Player_ID')],
                            "Game_ID": row[headers.index('Game_ID')],
                            "GAME_DATE": row[headers.index('GAME_DATE')],
                            "MATCHUP": row[headers.index('MATCHUP')],
                            "WL": row[headers.index('WL')],
                            "MIN": row[headers.index('MIN')],
                            "FGM": row[headers.index('FGM')],
                            "FGA": row[headers.index('FGA')],
                            "FG_PCT": row[headers.index('FG_PCT')],
                            "FG3M": row[headers.index('FG3M')],
                            "FG3A": row[headers.index('FG3A')],
                            "FG3_PCT": row[headers.index('FG3_PCT')],
                            "FTM": row[headers.index('FTM')],
                            "FTA": row[headers.index('FTA')],
                            "FT_PCT": row[headers.index('FT_PCT')],
                            "OREB": row[headers.index('OREB')],
                            "DREB": row[headers.index('DREB')],
                            "REB": row[headers.index('REB')],
                            "AST": row[headers.index('AST')],
                            "STL": row[headers.index('STL')],
                            "BLK": row[headers.index('BLK')],
                            "TOV": row[headers.index('TOV')],
                            "PF": row[headers.index('PF')],
                            "PTS": row[headers.index('PTS')],
                            "PLUS_MINUS": row[headers.index('PLUS_MINUS')],
                            "VIDEO_AVAILABLE": row[headers.index('VIDEO_AVAILABLE')],
                            "TEAM_NAME": opponent_team_info['TEAM_NAME'],
                            "TEAM_GP": opponent_team_info['TEAM_GP'],
                            "TEAM_W": opponent_team_info['TEAM_W'],
                            "TEAM_L": opponent_team_info['TEAM_L'],
                            "TEAM_W_PCT": opponent_team_info['TEAM_W_PCT'],
                            "TEAM_PLUS_MINUS": opponent_team_info['TEAM_PLUS_MINUS'],
                            "TEAM_W_PCT_RANK": opponent_team_info['TEAM_W_PCT_RANK'],
                            "TEAM_OPP_FG_PCT_RANK": opponent_team_info['TEAM_OPP_FG_PCT_RANK'],
                            "TEAM_OPP_FG3M_RANK": opponent_team_info['TEAM_OPP_FG3M_RANK'],
                            "TEAM_OPP_FG3_PCT_RANK": opponent_team_info['TEAM_OPP_FG3_PCT_RANK'],
                            "TEAM_OPP_FT_PCT_RANK": opponent_team_info['TEAM_OPP_FT_PCT_RANK'],
                            "TEAM_OPP_REB_RANK": opponent_team_info['TEAM_OPP_REB_RANK'],
                            "TEAM_OPP_AST_RANK": opponent_team_info['TEAM_OPP_AST_RANK'],
                            "TEAM_OPP_TOV_RANK": opponent_team_info['TEAM_OPP_TOV_RANK'],
                            "TEAM_OPP_STL_RANK": opponent_team_info['TEAM_OPP_STL_RANK'],
                            "TEAM_OPP_BLK_RANK": opponent_team_info['TEAM_OPP_BLK_RANK'],
                            "TEAM_OPP_BLKA_RANK": opponent_team_info['TEAM_OPP_BLKA_RANK'],
                            "TEAM_OPP_PF_RANK": opponent_team_info['TEAM_OPP_PF_RANK'],
                            "TEAM_OPP_PFD_RANK": opponent_team_info['TEAM_OPP_PFD_RANK'],
                            "TEAM_OPP_PTS_RANK": opponent_team_info['TEAM_OPP_PTS_RANK'],
                            "TEAM_PLUS_MINUS_RANK": opponent_team_info['TEAM_PLUS_MINUS_RANK']}
                        all_players_box_scores.append(player_data)
        writer.writerows(all_players_box_scores)

    return all_players_box_scores
