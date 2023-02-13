from players import AgentRandom, AgentXleddyl
import quarto
import argparse
import time

# clear && python3 main.py -m 10

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--matches', type=int, default=1, help='num of matches')
args = parser.parse_args()

if __name__ == '__main__':
    n_matches = args.matches
    win = []
    t = []
    game = quarto.Quarto(n_matches == 1)
    players = [AgentXleddyl(game), AgentRandom(game)]

    print(f"*** {type(players[0]).__name__} vs {type(players[1]).__name__} over {n_matches} match{'es' if n_matches > 1 else ''} ***\n")
    for i in range(n_matches):
        game.reset()

        if n_matches > 1:
            print(f"progress -> {i + 1} / {n_matches}", end="\r")

        start = time.time()
        turn = i % 2
        game.set_players((players[turn], players[1 - turn]))
        winner = game.run()
        if winner == -1:
            win.append(winner)
        else:
            win.append(winner if i % 2 == 0 else 1 - winner)
        end = time.time()
        t.append(end - start)
    print(f"{type(players[0]).__name__} win rate against {type(players[1]).__name__}: {round((win.count(0)) / len(win) * 100, 2)}%")
    print('  -  {:15s}   {}'.format(type(players[0]).__name__, win.count(0)))
    print('  -  {:15s}   {}'.format(type(players[1]).__name__, win.count(1)))
    print('  -  {:15s}   {}\n'.format('ties', win.count(-1)))
    print(f"({'avg ' if n_matches > 1 else ''}match time: {round(sum(t) / len(t), 2)}s)")
