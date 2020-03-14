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

    @patch("game.roll_die", side_effect=[1, 2])
    @patch("game.play", side_effect=[""])
    def test_flee_roll_1_for_hp_change(self, _, __):
        character = {"HP": [5, 5]}
        combat.flee(character)
        actual = character
        expected = {"HP": [3, 5], "in_combat": False}
        self.assertEqual(actual, expected)

    @patch("game.roll_die", side_effect=[3])
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("game.play", side_effect=[""])
    def test_flee_successful_escape(self, _, mock_sysout, __):
        character = {"HP": [5, 5]}
        combat.flee(character)
        expected = "You managed to falsify a doctors note and got excused from class!\n"
        self.assertEqual(mock_sysout.getvalue(), expected)