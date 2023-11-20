# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from get_player_details_by_id import get_player_details_by_id
from get_player_stats_by_id import get_player_stats_by_id


def main():
    first_name = input("Enter player's first name: ")
    last_name = input("Enter player's last name: ")
    team = input("Enter player's team: ")
    season = input("Enter season: ")
    player = get_player_details_by_id(first_name, last_name, team)
    playerstats = get_player_stats_by_id(first_name, last_name, team, season)
    if player is None:
        print("Player not found")
    else:
        print(player)
    if playerstats is None:
        print("Player stats not found")
    else:
        print(playerstats)


if __name__ == '__main__':
    main()
