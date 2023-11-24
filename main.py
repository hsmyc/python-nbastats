from find_player_id import find_player_id
from get_daily_player_list import dfs_players
from get_all_players import player_search
from get_stats_by_date import get_stats_by_date
import sys
import json
import os


def main():
    players = dfs_players()
    player_ids = []
    playerslist = []
    start_date = input('Enter start date (YYYY-MM-DD): ')
    end_date = input('Enter end date (YYYY-MM-DD): ')
    if os.path.exists('allplayers.json'):
        with open('allplayers.json', 'r') as infile:
            if os.path.getsize('allplayers.json') > 0:
                playerslist = json.load(infile)
            else:
                print('No players found. Generating list...')
                playerslist = player_search()
                with open('allplayers.json', 'w') as outfile:
                    json.dump(playerslist, outfile)
    else:
        print('No players found. Generating list...')
        playerslist = player_search()
        with open('allplayers.json', 'w') as outfile:
            json.dump(playerslist, outfile)

    for number, player in enumerate(players):
        progress = (number / len(players)) * 100
        sys.stdout.write(
            f"\rPlayer {number} of {len(players)}. Progress: [{int(progress)//2 * '#'}{int(50 - progress)//2 * ' '}] {progress:.2f}% Complete. 'Finding player ID...")
        sys.stdout.flush()
        player_id = find_player_id(player['name'], player['team'], playerslist)
        player_ids.append(player_id)
    get_stats_by_date(start_date, end_date, player_ids)


if __name__ == '__main__':
    main()
