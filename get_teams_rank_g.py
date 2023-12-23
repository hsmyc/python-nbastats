import csv
import requests


def get_teams_rank_g():
    url = "https://stats.nba.com/stats/leaguedashteamstats"
    params = {
        "Conference": "",
        "DateFrom": "",
        "DateTo": "",
        "Division": "",
        "GameScope": "",
        "GameSegment": "",
        "Height": "",
        "ISTRound": "",
        "LastNGames": "0",
        "LeagueID": "00",
        "Location": "",
        "MeasureType": "Opponent",
        "Month": "0",
        "OpponentTeamID": "0",
        "Outcome": "",
        "PORound": "0",
        "PaceAdjust": "N",
        "PerMode": "PerGame",
        "Period": "0",
        "PlayerExperience": "",
        "PlayerPosition": "G",
        "PlusMinus": "N",
        "Rank": "N",
        "Season": "2023-24",
        "SeasonSegment": "",
        "SeasonType": "Regular Season",
        "ShotClockRange": "",
        "StarterBench": "",
        "TeamID": "0",
        "TwoWay": "0",
        "VsConference": "",
        "VsDivision": "",
    }
    headers = {
        "Referer": "https://www.nba.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }
    response = requests.get(url, headers=headers, params=params)
    response_json: dict = response.json()
    result_sets = response_json["resultSets"]
    headers = result_sets[0]["headers"]
    rows = result_sets[0]["rowSet"]
    team_rank_grd = []
    with open("teamrankg.csv", "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = [
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_GP",
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
            "TEAM_PLUS_MINUS_RANK",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "TEAM_ID": row[headers.index("TEAM_ID")],
                    "TEAM_NAME": row[headers.index("TEAM_NAME")],
                    "TEAM_GP": row[headers.index("GP")],
                    "TEAM_W": row[headers.index("W")],
                    "TEAM_L": row[headers.index("L")],
                    "TEAM_W_PCT": row[headers.index("W_PCT")],
                    "TEAM_PLUS_MINUS": row[headers.index("PLUS_MINUS")],
                    "TEAM_W_PCT_RANK": row[headers.index("W_PCT_RANK")],
                    "TEAM_OPP_FG_PCT_RANK": row[headers.index("OPP_FG_PCT_RANK")],
                    "TEAM_OPP_FG3M_RANK": row[headers.index("OPP_FG3M_RANK")],
                    "TEAM_OPP_FG3_PCT_RANK": row[headers.index("OPP_FG3_PCT_RANK")],
                    "TEAM_OPP_FT_PCT_RANK": row[headers.index("OPP_FT_PCT_RANK")],
                    "TEAM_OPP_REB_RANK": row[headers.index("OPP_REB_RANK")],
                    "TEAM_OPP_AST_RANK": row[headers.index("OPP_AST_RANK")],
                    "TEAM_OPP_TOV_RANK": row[headers.index("OPP_TOV_RANK")],
                    "TEAM_OPP_STL_RANK": row[headers.index("OPP_STL_RANK")],
                    "TEAM_OPP_BLK_RANK": row[headers.index("OPP_BLK_RANK")],
                    "TEAM_OPP_BLKA_RANK": row[headers.index("OPP_BLKA_RANK")],
                    "TEAM_OPP_PF_RANK": row[headers.index("OPP_PF_RANK")],
                    "TEAM_OPP_PFD_RANK": row[headers.index("OPP_PFD_RANK")],
                    "TEAM_OPP_PTS_RANK": row[headers.index("OPP_PTS_RANK")],
                    "TEAM_PLUS_MINUS_RANK": row[headers.index("PLUS_MINUS_RANK")],
                }
            )

            team_rank_g.append(
                {
                    "TEAM_ID": row[headers.index("TEAM_ID")],
                    "TEAM_NAME": row[headers.index("TEAM_NAME")],
                    "TEAM_GP": row[headers.index("GP")],
                    "TEAM_W": row[headers.index("W")],
                    "TEAM_L": row[headers.index("L")],
                    "TEAM_W_PCT": row[headers.index("W_PCT")],
                    "TEAM_PLUS_MINUS": row[headers.index("PLUS_MINUS")],
                    "TEAM_W_PCT_RANK": row[headers.index("W_PCT_RANK")],
                    "TEAM_OPP_FG_PCT_RANK": row[headers.index("OPP_FG_PCT_RANK")],
                    "TEAM_OPP_FG3M_RANK": row[headers.index("OPP_FG3M_RANK")],
                    "TEAM_OPP_FG3_PCT_RANK": row[headers.index("OPP_FG3_PCT_RANK")],
                    "TEAM_OPP_FT_PCT_RANK": row[headers.index("OPP_FT_PCT_RANK")],
                    "TEAM_OPP_REB_RANK": row[headers.index("OPP_REB_RANK")],
                    "TEAM_OPP_AST_RANK": row[headers.index("OPP_AST_RANK")],
                    "TEAM_OPP_TOV_RANK": row[headers.index("OPP_TOV_RANK")],
                    "TEAM_OPP_STL_RANK": row[headers.index("OPP_STL_RANK")],
                    "TEAM_OPP_BLK_RANK": row[headers.index("OPP_BLK_RANK")],
                    "TEAM_OPP_BLKA_RANK": row[headers.index("OPP_BLKA_RANK")],
                    "TEAM_OPP_PF_RANK": row[headers.index("OPP_PF_RANK")],
                    "TEAM_OPP_PFD_RANK": row[headers.index("OPP_PFD_RANK")],
                    "TEAM_OPP_PTS_RANK": row[headers.index("OPP_PTS_RANK")],
                    "TEAM_PLUS_MINUS_RANK": row[headers.index("PLUS_MINUS_RANK")],
                }
            )

    return team_rank_g
