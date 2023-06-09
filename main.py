from uno.player import Player
from game import Game
from functions import generate_rand_number_seq

if __name__ == '__main__':
    name_list = ['Steve', 'Alex', 'Alice', 'John']
    players = []
    for name in name_list:
        players.append(Player(generate_rand_number_seq(10), name))

    game = Game(players)
    game.run()
