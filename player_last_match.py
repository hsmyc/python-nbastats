import pandas as pd
import datetime
from get_teams_rank import get_teams_rank


def player_last_match(player_name, data, opponent_team):
    df = pd.DataFrame(data)
    today = datetime.datetime.today()

    df['GAME_DATE'] = pd.to_datetime(
        df['GAME_DATE'], format='%b %d, %Y')

    player_team = df[df['PLAYER_NAME'] ==
                     player_name]['TEAM_ABBREVIATION'].iloc[0]

    player_data = df[df['PLAYER_NAME'] == player_name]

    opponent_team_data = {}
    for team in get_teams_rank():
        if team['TEAM_NAME'] == opponent_team:
            opponent_team_data = team

    player_rest_days = today - player_data['GAME_DATE'].iloc[0]
    total_minutes = player_data['MIN'].sum()
    last_30_day_minutes = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=30))]['MIN'].sum()
    last_15_day_minutes = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=15))]['MIN'].sum()
    last_7_day_minutes = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=7))]['MIN'].sum()

    total_matches = player_data['MATCHUP'].count()
    last_30_day_matches = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=30))]['MATCHUP'].count()
    last_15_day_matches = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=15))]['MATCHUP'].count()
    last_7_day_matches = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=7))]['MATCHUP'].count()

    total_points = player_data['PTS'].sum()
    last_30_day_points = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=30))]['PTS'].sum()
    last_15_day_points = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=15))]['PTS'].sum()
    last_7_day_points = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=7))]['PTS'].sum()

    total_rebounds = player_data['REB'].sum()
    last_30_day_rebounds = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=30))]['REB'].sum()
    last_15_day_rebounds = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=15))]['REB'].sum()
    last_7_day_rebounds = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=7))]['REB'].sum()

    total_assists = player_data['AST'].sum()
    last_30_day_assists = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=30))]['AST'].sum()
    last_15_day_assists = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=15))]['AST'].sum()
    last_7_day_assists = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=7))]['AST'].sum()

    total_3pm = player_data['FG3M'].sum()
    last_30_day_3pm = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=30))]['FG3M'].sum()
    last_15_day_3pm = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=15))]['FG3M'].sum()
    last_7_day_3pm = player_data[player_data['GAME_DATE'] > (
        today - datetime.timedelta(days=7))]['FG3M'].sum()

    total_points_and_rebounds = total_points + total_rebounds
    last_30_day_points_and_rebounds = last_30_day_points + last_30_day_rebounds
    last_15_day_points_and_rebounds = last_15_day_points + last_15_day_rebounds
    last_7_day_points_and_rebounds = last_7_day_points + last_7_day_rebounds

    average_stats = {
        'player_name': player_name,
        'player_team': player_team,
        'opponent_team': opponent_team,
        'player_rest_days': player_rest_days.days,
        'total_minutes': total_minutes,
        'last_30_day_minutes': last_30_day_minutes,
        'last_15_day_minutes': last_15_day_minutes,
        'last_7_day_minutes': last_7_day_minutes,
        'total_matches': total_matches,
        'last_30_day_matches': last_30_day_matches,
        'last_15_day_matches': last_15_day_matches,
        'last_7_day_matches': last_7_day_matches,
        'total_points': total_points,
        'last_30_day_points': last_30_day_points,
        'last_15_day_points': last_15_day_points,
        'last_7_day_points': last_7_day_points,
        'total_rebounds': total_rebounds,
        'last_30_day_rebounds': last_30_day_rebounds,
        'last_15_day_rebounds': last_15_day_rebounds,
        'last_7_day_rebounds': last_7_day_rebounds,
        'total_assists': total_assists,
        'last_30_day_assists': last_30_day_assists,
        'last_15_day_assists': last_15_day_assists,
        'last_7_day_assists': last_7_day_assists,
        'total_3pm': total_3pm,
        'last_30_day_3pm': last_30_day_3pm,
        'last_15_day_3pm': last_15_day_3pm,
        'last_7_day_3pm': last_7_day_3pm,
        'total_points_and_rebounds': total_points_and_rebounds,
        'last_30_day_points_and_rebounds': last_30_day_points_and_rebounds,
        'last_15_day_points_and_rebounds': last_15_day_points_and_rebounds,
        'last_7_day_points_and_rebounds': last_7_day_points_and_rebounds,


        "O_TEAM_GP": opponent_team_data['TEAM_GP'],
        "O_TEAM_W": opponent_team_data['TEAM_W'],
        "O_TEAM_L": opponent_team_data['TEAM_L'],
        "O_TEAM_W_PCT": opponent_team_data['TEAM_W_PCT'],
        "O_TEAM_PLUS_MINUS": opponent_team_data['TEAM_PLUS_MINUS'],
        "O_TEAM_W_PCT_RANK": opponent_team_data['TEAM_W_PCT_RANK'],
        "O_TEAM_OPP_FG_PCT_RANK": opponent_team_data['TEAM_OPP_FG_PCT_RANK'],
        "O_TEAM_OPP_FG3M_RANK": opponent_team_data['TEAM_OPP_FG3M_RANK'],
        "O_TEAM_OPP_FG3_PCT_RANK": opponent_team_data['TEAM_OPP_FG3_PCT_RANK'],
        "O_TEAM_OPP_FT_PCT_RANK": opponent_team_data['TEAM_OPP_FT_PCT_RANK'],
        "O_TEAM_OPP_REB_RANK": opponent_team_data['TEAM_OPP_REB_RANK'],
        "O_TEAM_OPP_AST_RANK": opponent_team_data['TEAM_OPP_AST_RANK'],
        "O_TEAM_OPP_TOV_RANK": opponent_team_data['TEAM_OPP_TOV_RANK'],
        "O_TEAM_OPP_STL_RANK": opponent_team_data['TEAM_OPP_STL_RANK'],
        "O_TEAM_OPP_BLK_RANK": opponent_team_data['TEAM_OPP_BLK_RANK'],
        "O_TEAM_OPP_BLKA_RANK": opponent_team_data['TEAM_OPP_BLKA_RANK'],
        "O_TEAM_OPP_PF_RANK": opponent_team_data['TEAM_OPP_PF_RANK'],
        "O_TEAM_OPP_PFD_RANK": opponent_team_data['TEAM_OPP_PFD_RANK'],
        "O_TEAM_OPP_PTS_RANK": opponent_team_data['TEAM_OPP_PTS_RANK'],
        "O_TEAM_PLUS_MINUS_RANK": opponent_team_data['TEAM_PLUS_MINUS_RANK']
    }

    df_stats = pd.DataFrame([average_stats])
    df_stats.to_csv('player_last_match.csv', index=False)

    return average_stats
