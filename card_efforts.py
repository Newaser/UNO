from uno.enums import *
from functions import ask

__all__ = ['do_effect']


def skip(game, _):
    game.next_turn()
    input('Player ' + game.players[game.cur_player].name + "'s turn has been skipped.")


def reverse(game, _):
    game.cur_direction = \
        (Direction.COUNTERCLOCKWISE
         if game.cur_direction is Direction.CLOCKWISE
         else Direction.CLOCKWISE)
    input('The direction of turns has been reversed')


def draw_two(game, _):
    game.next_turn()

    next_player = game.players[game.cur_player]
    game.draw(next_player, 2)
    input('Player ' + next_player.name + " drew 2 cards and skipped its turn.")


def wild(_, wild_card):
    suit_list = [suit.name for suit in Suit]
    wild_card.suit = Suit[suit_list[ask(suit_list, 'Specify a color: ')]]


def wild_draw_four(game, wd4):
    wild(game, wd4)

    game.next_turn()
    next_player = game.players[game.cur_player]
    game.draw(next_player, 4)
    input('Player ' + next_player.name + " drew 4 cards and skipped its turn.")


card_effect_dict = {
    CardType.SKIP: skip,
    CardType.REVERSE: reverse,
    CardType.DRAW_TWO: draw_two,
    CardType.WILD: wild,
    CardType.WILD_DRAW_FOUR: wild_draw_four
}


def do_effect(game, card):
    if card.type in card_effect_dict.keys():
        card_effect_dict[card.type](game, card)
