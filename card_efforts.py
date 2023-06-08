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

    cur_player = game.players[game.cur_player]
    cur_hands = game.get_cur_hands()
    next_player = game.players[game.cur_player + game.cur_direction.value]

    print('Player ' + next_player.name + " is about to draw 4 cards and skip its turn.")
    if bool(1 - ask(['Yes', 'No'], 'Do you challenge ' + cur_player.name + ', ' + next_player.name + '? ')):
        last_card = game.get_last_card()
        challenge_succeeded = False

        if last_card is not None:
            challenge_succeeded |= int(last_card.type.value) == SPECIAL_SCORE
            challenge_succeeded |= any(hand.suit == last_card.suit for hand in cur_hands)

        if challenge_succeeded:
            game.draw(cur_player, 4)
            print('Challenge succeeded, since Player ' + cur_player.name +
                  " has a card in the same suit as the last played card's.")
            input('As punishment, Player ' + cur_player.name + " drew 4 cards.")
        else:
            game.draw(next_player, 6)
            game.next_turn()
            print('Challenge failed, since Player ' + cur_player.name +
                  " doesn't has a card in the same suit as the last played card's.")
            input('As punishment, Player ' + next_player.name + " drew 6 cards and skipped its turn.")
    else:
        game.draw(next_player, 4)
        game.next_turn()
        input('Since Player ' + cur_player.name + ' was not challenged, Player ' + next_player.name +
              " drew 4 cards and skipped its turn.")


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
