from unittest import TestCase
from unittest.mock import patch
import combat
import io


class Test(TestCase):
    @patch('game.roll_die', side_effect=[20, 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_stayed_alive(self, mock_sysout, _):
        character = {"HP": [10, 10], "name": "Swag"}
        enemy = {"HP": [4, 4], "name": "Armaan"}
        combat.combat_round(character, enemy)
        expected = "Swag hits Armaan for 6 damage. Armaan never stood a chance and now lies dead.\n\n"
        self.assertEqual(mock_sysout.getvalue(), expected)


    @patch('game.roll_die', side_effect=[20, 3, 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_stayed_alive(self, mock_sysout, _):
        character = {"HP": [10, 10], "name": "Swag"}
        enemy = {"HP": [4, 4], "name": "Armaan"}
        combat.combat_round(character, enemy)
        expected = "Swag hits Armaan for 6 damage. Armaan never stood a chance and now lies dead.\n\n"
        self.assertEqual(mock_sysout.getvalue(), expected)
