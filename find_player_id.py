

def find_player_id(name: str, team: str, players: list):
    if team == 'PHO':
        team = 'PHX'
    team_lower = team.lower()
    matching_player = {}
    for player in players:
        if player['team']['abbreviation'].lower() == team_lower and player['first_name'].lower() in name.lower() or player['last_name'].lower() in name.lower():
            matching_player = player
    print(matching_player)
    return matching_player['id']
