import requests


def find_player_id(name: str, team: str, players: list):
    if team == 'PHO':
        team = 'PHX'
    if team == 'NO':
        team = 'NOP'
    if team == 'SA':
        team = 'SAS'
    if team == 'NY':
        team = 'NYK'
    if team == 'GS':
        team = 'GSW'
    team_lower = team.lower()
    name_parts = name.lower().split()
    first_name = name_parts[0]
    if len(name_parts) > 1:
        if 'jr.' in name_parts or 'sr.' in name_parts or 'ii' in name_parts or 'iii' in name_parts:
            last_name = name_parts[-2]
        else:
            last_name = name_parts[-1]
    else:
        last_name = name_parts
    id = None
    potential_matches = []
    for player in players:
        if (player['team']['abbreviation'].lower() == team_lower and
                player['first_name'].lower() == first_name):
            potential_matches.append(player)
    if len(potential_matches) == 1:
        id = potential_matches[0]['id']
    else:
        for player in potential_matches:
            if last_name in player['last_name'].lower():
                id = player['id']
                if id is not None:
                    break
                else:
                    id = requests.get(
                        f'https://www.balldontlie.io/api/v1/players?search={name}').json()['data'][0]['id']
    if id is None:
        print(f'Unable to find ID for {name} ({team})')
    return id
