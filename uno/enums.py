from enum import Enum, auto


FUNCTION_SCORE, SPECIAL_SCORE = 20, 50


class Suit(Enum):
    RED = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()


class CardType(Enum):
    # NUMBER type
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

    # FUNCTION type
    SKIP = FUNCTION_SCORE
    REVERSE = FUNCTION_SCORE + 0.1
    DRAW_TWO = FUNCTION_SCORE + 0.2

    # SPECIAL type
    WILD = SPECIAL_SCORE
    WILD_DRAW_FOUR = SPECIAL_SCORE + 0.1


class Direction(Enum):
    CLOCKWISE = -1
    COUNTERCLOCKWISE = 1
