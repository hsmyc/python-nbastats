

def find_player_id(name: str, team: str, players: list):
    if team == 'NO':
        team = 'NOP'
    if team == 'NY':
        team = 'NYK'
    if team == 'SA':
        team = 'SAS'
    if team == 'GS':
        team = 'GSW'
    info = {
        'id': None,
        'name': None,
        'team': None,
        'team_id': None
    }
    for player in players:
        if player['PLAYER_NAME'] == name and player['TEAM_ABBREVIATION'] == team:
            info['id'] = player['PERSON_ID']
            info['name'] = player['PLAYER_NAME']
            info['team'] = player['TEAM_ABBREVIATION']
            info['team_id'] = player['TEAM_ID']
            break
    if info['id'] is None:
        name = name.split(' ')
        name = name[1] + ', ' + name[0]
        for player in players:
            if player['PLAYER_NAME'] == name and player['TEAM_ABBREVIATION'] == team:
                info['id'] = player['PERSON_ID']
                info['name'] = player['PLAYER_NAME']
                info['team'] = player['TEAM_ABBREVIATION']
                info['team_id'] = player['TEAM_ID']
                break
    if info['id'] is None:
        print(f'Could not find player {name} on team {team}')
        return None

    return info
