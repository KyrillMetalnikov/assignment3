from unittest import TestCase
from unittest.mock import patch
import combat


class Test(TestCase):
    @patch("game.roll_die", side_effect=[12, 8])
    def test_roll_for_initiative_char_one_wins(self, _):
        expected = True
        actual = combat.roll_for_initiative()
        self.assertEqual(expected, actual)

    @patch("game.roll_die", side_effect=[8, 12])
    def test_roll_for_initiative_char_two_wins(self, _):
        expected = False
        actual = combat.roll_for_initiative()
        self.assertEqual(expected, actual)

    @patch("game.roll_die", side_effect=[8, 8, 10, 7])
    def test_roll_for_initiative_loop_then_char_one_true(self, _):
        expected = True
        actual = combat.roll_for_initiative()
        self.assertEqual(expected, actual)
