from enums import *


class Card:
    def __init__(self, suit, card_type):
        self.suit = suit
        self.type = card_type

    def get_score(self):
        return self.type.value


def generate_std_deck():
    deck = []
    for suit in Suit:
        for card_type in CardType:
            if card_type.value == 0:
                deck.append(Card(suit, card_type))
            elif 1 <= card_type.value <= 9 or card_type.value == FUNCTION_SCORE:
                for _ in range(2):
                    deck.append(Card(suit, card_type))
            elif card_type.value == SPECIAL_SCORE:
                for _ in range(4):
                    deck.append(Card(suit, card_type))

    return deck
