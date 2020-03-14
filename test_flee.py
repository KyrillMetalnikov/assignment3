from unittest import TestCase
from unittest.mock import patch
import combat
import io


class Test(TestCase):
    @patch("game.roll_die", side_effect=[1, 2])
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("game.play", side_effect=[""])
    def test_flee_roll_1_for_print(self, _, mock_sysout, __):
        character = {"HP": [5, 5]}
        combat.flee(character)
        expected = "You were late to a pop-quiz and got a 0! Lose 2 sanity.\n"
        self.assertEqual(mock_sysout.getvalue(), expected)
