# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from get_player_stats_by_season import get_player_stats_by_season
from get_player_details_by_id import get_player_details_by_id
from get_stats_by_date import get_stats_by_date
from find_player_id import find_player_id


def main():
    first_name = input("Enter player's first name: ")
    last_name = input("Enter player's last name: ")
    team = input("Enter player's team: ")

    player_id = find_player_id(first_name, last_name, team)
    if player_id is None:
        print("Player not found")
        return
    get_player_details_by_id(player_id)
    choice = input(
        "Do you want to get stats by season or stats by date? (Enter 'season' or 'date'): ").lower()

    if choice == 'season':
        season = input("Enter season: ")
        playerstats = get_player_stats_by_season(
            first_name, last_name, team, season, player_id)
        if playerstats is None:
            print("Player stats not found")
        else:
            print(playerstats)

    elif choice == 'date':
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        playerstatsbydate = get_stats_by_date(start_date, end_date, player_id)
        if playerstatsbydate is None:
            print("Player stats by date not found")
        else:
            print(playerstatsbydate)

    else:
        print("Invalid choice")


if __name__ == '__main__':
    main()
