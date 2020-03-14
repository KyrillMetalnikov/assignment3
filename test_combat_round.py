from unittest import TestCase
from unittest.mock import patch
import combat
import io


class Test(TestCase):
    @patch('game.roll_die', side_effect=[20, 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_no_retaliate(self, mock_sysout, _):
        character = {"HP": [10, 10], "name": "Swag"}
        enemy = {"HP": [4, 4], "name": "Armaan", "type": 'monster'}
        combat.combat_round(character, enemy)
        expected = """Swag sniffled in class!
Swag hits Armaan where it hurts and causes them to lose 6 sanity. Armaan has finally lost it and went completely insane.

"""
        self.assertEqual(mock_sysout.getvalue(), expected)

    @patch('game.roll_die', side_effect=[20, 6, 20, 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_with_retaliate(self, mock_sysout, _):
        character = {"HP": [10, 10], "name": "Swag"}
        enemy = {"HP": [10, 10], "name": "Armaan", "type": 'monster',
                 "attack": "Armaan says: Studies show students learn best when pushed to the edge!"}
        combat.combat_round(character, enemy)
        expected = """Swag sniffled in class!
Armaan is going crazy and loses 6 sanity!

Armaan says: Studies show students learn best when pushed to the edge!
Swag is going crazy and loses 6 sanity!

"""
        self.assertEqual(mock_sysout.getvalue(), expected)
