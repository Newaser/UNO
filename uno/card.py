import random
from .enums import *


class Card:
    def __init__(self, card_type, suit=None):
        self.suit = suit
        self.type = card_type

    def get_score(self):
        return int(self.type.value)

    def __repr__(self):
        suit_repr = self.suit.name + ' ' if self.suit is not None and int(self.type.value) != SPECIAL_SCORE else ''
        name_repr = str(self.type.value) if 0 <= self.type.value <= 9 else self.type.name
        return suit_repr + name_repr

    def get_full_repr(self):
        suit_repr = self.suit.name + ' ' if self.suit is not None else 'NOT COLORED '
        name_repr = str(self.type.value) if 0 <= self.type.value <= 9 else self.type.name
        return suit_repr + name_repr


def generate_std_deck(shuffle=False):
    deck = []
    for suit in Suit:
        for card_type in CardType:
            if card_type.value == 0:
                deck.append(Card(card_type, suit))
            elif 1 <= card_type.value <= 9 or int(card_type.value) == FUNCTION_SCORE:
                for _ in range(2):
                    deck.append(Card(card_type, suit))
            elif int(card_type.value) == SPECIAL_SCORE:
                deck.append(Card(card_type))

    if shuffle:
        random.shuffle(deck)
    return deck
