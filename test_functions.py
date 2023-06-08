import unittest
from unittest.mock import patch
from functions import *


class TestFunctions(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input')
    def testAsk(self, mock_input, _):
        mock_input.side_effect = ['p', '-1', '5', '4']

        name_list = ['Steve', 'Alex', 'Bob', 'John']
        choice = ask(name_list)
        self.assertEqual(name_list[choice], 'John')


if __name__ == '__main__':
    unittest.main()
