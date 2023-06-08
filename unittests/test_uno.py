import unittest

import uno.card


class TestUno(unittest.TestCase):
    def test_deck(self):
        deck = uno.card.generate_std_deck(shuffle=True)
        print(deck)


if __name__ == '__main__':
    unittest.main()
