from unittest import TestCase
from unittest.mock import patch
import combat
import io


class Test(TestCase):
    @patch('combat.roll_for_initiative', side_effect=[""])
    @patch('monster.get_monster', side_effect=[""])
    @patch('game.is_alive', side_effect=[True, True, False, True])
    @patch('combat.combat_round', side_effect=["", ""])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('game.play', side_effect=[""])
    def test_start_combat_survive(self, _, mock_sysout, __, ___, ____, _____):
        character = {"HP": [10, 10]}
        combat.start_combat(character)
        expected = "You outlasted your instructor!\n"
        self.assertEqual(expected, mock_sysout.getvalue())
