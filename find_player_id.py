
from get_all_players import player_search


def find_player_id(name: str, team: str):
    players = player_search(name)
    if team == 'PHO':
        team = 'PHX'
    if players == None:
        print(f'No matching players found. Name: {name}, Team: {team}')
        return None
    team_lower = team.lower()
    matching_player = {}
    if len(players) > 1:
        for player in players:
            if player['team']['abbreviation'].lower() == team_lower:
                matching_player = player
    else:
        matching_player = players[0]
    return (matching_player['id'])
