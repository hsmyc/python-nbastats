from find_player_id import find_player_id
from get_daily_player_list import dfs_players
from get_all_players import player_search
import sys
import json


def main():
    players = dfs_players()
    player_ids = []
    playerslist = player_search()
    print(len(playerslist))
    for number, player in enumerate(players):
        progress = (number / len(players)) * 100
        sys.stdout.write(
            f"\rPlayer {number} of {len(players)}. Progress: [{int(progress)//2 * '#'}{int(50 - progress)//2 * ' '}] {progress:.2f}% Complete. 'Finding player ID...")
        sys.stdout.flush()
        player_id = find_player_id(player['name'], player['team'], playerslist)
        player_ids.append(player_id)

    with open('player_ids.txt', 'w') as outfile:
        for player_id in player_ids:
            outfile.write(str(player_id) + '\n')


if __name__ == '__main__':
    main()
