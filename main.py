from find_player_info import find_player_id
from get_daily_player_list import dfs_players
from all_player_info import all_player_info
from player_box_scores import player_box_scores
from get_teams_rank import get_teams_rank
from creating_chart import create_chart
import sys


def main():

    players = dfs_players()
    player_infos = []
    player_team_infos = []
    playerslist = all_player_info()
    for number, player in enumerate(players):
        progress = (number / len(players)) * 100
        sys.stdout.write(
            f"\rPlayer {number} of {len(players)}. Progress: [{int(progress)//2 * '#'}{int(50 - progress)//2 * ' '}] {progress:.2f}% Complete. 'Finding player ID...")
        sys.stdout.flush()
        player_info = find_player_id(
            player['name'], player['team'], playerslist)
        if player_info is not None:
            player_infos.append(player_info)
    player_team_infos = get_teams_rank()
    player_box_scores(player_infos, player_team_infos)
    print('\nDone!')
    # print('Generating chart...')
    # time.sleep(2)
    # create_chart()


if __name__ == '__main__':
    main()
