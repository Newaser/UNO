from uno.card import *
from errors import *
from functions import *
from card_efforts import *
import os


class Game:
    STARTING_HANDS = 7
    DEFAULT_DIRECTION = Direction.COUNTERCLOCKWISE

    def __init__(self, players):
        if not 2 <= len(players) <= 10:
            raise ValueError('The number of players should be in range[2, 10]')

        # members
        self.players = players

        # areas
        self.deck = generate_std_deck(shuffle=True)
        self.deadwood = []
        self.hands = {player.pid: [] for player in self.players}

        # game states
        self.dealer = None
        self.cur_player = None
        self.cur_direction = None

    def shuffle(self):
        random.shuffle(self.deadwood)
        self.deck += self.deadwood
        self.deadwood.clear()

    def draw(self, player, number=1):
        drawn = []
        for _ in range(number):
            if len(self.deck) == 0:
                self.shuffle()
            if len(self.deck) == 0:
                raise OutOfCardsError()
            drawn.append(self.deck.pop())

        self.hands[player.pid].extend(drawn)
        return drawn[0] if number == 1 else drawn

    def is_playable(self, card):
        if self.get_last_card() is None:
            return True
        playable = False
        playable |= int(card.type.value) == SPECIAL_SCORE
        playable |= card.suit == self.get_last_card().suit
        playable |= card.type == self.get_last_card().type

        return playable

    def play(self, player, hand):
        self.hands[player.pid].remove(hand)
        self.deadwood.append(hand)

        # extra effects for function/special cards
        do_effect(self, hand)

    def get_last_card(self):
        try:
            return self.deadwood[-1]
        except IndexError:
            pass

    def get_cur_hands(self):
        return self.hands[self.players[self.cur_player].pid]

    def init(self):
        for _ in range(self.STARTING_HANDS):
            for player in self.players:
                self.draw(player)

        self.dealer = random.randrange(len(self.players))

    def print_prompt(self):
        print('>>>' + self.players[self.cur_player].name + "'s Turn<<<\n")
        print('--Player List(Counterclockwise)--\n Name\tHands')
        for i, player in enumerate(self.players):
            player_info = '*' if i == self.cur_player else ' '
            player_info += player.name + '\t'
            player_info += str(len(self.hands[player.pid]))
            print(player_info)
        print('\n--Current Direction--\n' + self.cur_direction.name.capitalize() + '\n')
        print(
            '--About Cards--\n' +
            'Cards in the Deck: ' +
            str(len(self.deck)) +
            '\nLast Played Card: ' +
            (self.get_last_card().get_full_repr() if self.get_last_card() is not None else 'None') +
            '\n'
        )

    def end_turn(self):
        player_num = len(self.players)
        self.cur_player = (player_num + self.cur_player + self.cur_direction.value) % player_num

    def run(self):
        self.cur_player = self.dealer
        self.cur_direction = self.DEFAULT_DIRECTION

        while True:
            os.system('cls')
            self.print_prompt()
            choice = ask(
                self.get_cur_hands() + ['Draw a Card'],
                prompt='Play or Draw a Card:'
            )
            if choice == len(self.get_cur_hands()):
                card = self.draw(self.players[self.cur_player])
                input('Card ' + str(card) + ' is drawn')
                if self.is_playable(card):
                    if bool(1 - ask(['Yes', 'No'], 'This card is playable. Play it right now? ')):
                        self.play(self.players[self.cur_player], card)
            else:
                card = self.get_cur_hands()[choice]
                if not self.is_playable(card):
                    input('This card is not playable right now.')
                    continue
                else:
                    self.play(self.players[self.cur_player], card)
            self.end_turn()
