from .card import *


class Game:
    def __init__(self, players):
        if not 2 <= len(players) <= 10:
            raise ValueError('The number of players should be in range[2, 10]')

        self.deck = generate_std_deck(shuffle=True)
        self.players = players

