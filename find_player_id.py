import requests
import csv


def find_player_id(name: str, team: str, players: list):
    if team == 'NO':
        team = 'NOP'
    if team == 'NY':
        team = 'NYK'
    if team == 'SA':
        team = 'SAS'
    if team == 'GS':
        team = 'GSW'
    id = None
    for player in players:
        if player['PLAYER_NAME'] == name and player['TEAM_ABBREVIATION'] == team:
            id = player['PERSON_ID']
    if id is None:
        name = name.split(' ')
        name = name[1] + ', ' + name[0]
        for player in players:
            if player['PLAYER_NAME'] == name and player['TEAM_ABBREVIATION'] == team:
                id = player['PERSON_ID']
    return id
