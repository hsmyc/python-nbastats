# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from get_all_players import player_search


def find_player_id(player_first_name: str, player_last_name: str, team: str):
    players = player_search(player_first_name)

    player_first_name_lower = player_first_name.lower()
    player_last_name_lower = player_last_name.lower()
    team_lower = team.lower()

    matching_players = [player for player in players if
                        player['first_name'].lower() == player_first_name_lower and
                        player['last_name'].lower() == player_last_name_lower and
                        player['team']['full_name'].lower() == team_lower]
    print(matching_players)
    if len(matching_players) == 0:
        print('No matching players found.')
        return None
    return next((player['id'] for player in matching_players), None)
