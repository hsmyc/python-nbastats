# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

from get_player_details_by_id import get_player_details_by_id


def main():
    first_name = input("Enter player's first name: ")
    last_name = input("Enter player's last name: ")
    team = input("Enter player's team: ")
    player = get_player_details_by_id(first_name, last_name, team)
    print(player)


if __name__ == '__main__':
    main()
