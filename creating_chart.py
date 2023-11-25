import pandas as pd
import matplotlib.pyplot as plt


def create_chart():
    df = pd.read_csv('statsdata.csv')
    df = df.sort_values('game_date', ascending=True)
    name = input('Enter player name: ')

    player = df[df['name'] == name]

    if player.empty:
        print(f"No data found for player: {name}")
        return

    plt.figure(figsize=(12, 8))

    plt.barh(player['game_date'], player['min'])
    plt.xlabel('Minutes Played')
    plt.ylabel('Date')
    plt.title(f'Minutes Played by {name} in Each Match')
    plt.tight_layout()
    plt.show()
