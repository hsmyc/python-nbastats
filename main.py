from find_player_id import find_player_id
from get_daily_player_list import dfs_players
from all_player_info import all_player_info
from player_box_scores import player_box_scores
from get_stats_by_date import get_stats_by_date
from creating_chart import create_chart
import sys
import json
import os
import time


def main():
    players = dfs_players()
    player_ids = []
    playerslist = all_player_info()
    for number, player in enumerate(players):
        progress = (number / len(players)) * 100
        sys.stdout.write(
            f"\rPlayer {number} of {len(players)}. Progress: [{int(progress)//2 * '#'}{int(50 - progress)//2 * ' '}] {progress:.2f}% Complete. 'Finding player ID...")
        sys.stdout.flush()
        player_id = find_player_id(player['name'], player['team'], playerslist)
        player_ids.append(player_id)
    date = time.localtime()
    player_box_scores(player_ids, date)

    print('\nDone!')
    # print('Generating chart...')
    # time.sleep(2)
    # create_chart()


if __name__ == '__main__':
    main()
