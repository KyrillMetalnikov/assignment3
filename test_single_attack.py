from unittest import TestCase
from unittest.mock import patch
import combat
import io


class Test(TestCase):
    @patch('game.roll_die', side_effect=[20, 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_attack_death(self, mock_sysout, _):
        character = {"HP": [10, 10], "name": "Swag"}
        enemy = {"HP": [4, 4], "name": "Armaan", "type": 'monster'}
        combat.single_attack(character, enemy)
        expected = """Swag sniffled in class!
Swag hits Armaan where it hurts and causes them to lose 6 sanity. Armaan has finally lost it and went completely insane.

"""
        self.assertEqual(mock_sysout.getvalue(), expected)

    @patch('game.roll_die', side_effect=[20, 6])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_attack_hit_and_live(self, mock_sysout, _):
        character = {"HP": [10, 10], "name": "Swag"}
        enemy = {"HP": [10, 10], "name": "Armaan", "type": 'monster'}
        combat.single_attack(character, enemy)
        expected = """Swag sniffled in class!
Armaan is going crazy and loses 6 sanity!

"""
        self.assertEqual(mock_sysout.getvalue(), expected)

    @patch('game.roll_die', side_effect=[5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_single_attack_miss(self, mock_sysout, _):
        character = {"HP": [10, 10], "name": "Swag"}
        enemy = {"HP": [10, 10], "name": "Armaan", "type": 'monster'}
        combat.single_attack(character, enemy)
        expected = """Swag sniffled in class!
Armaan is living in denial! Armaan doesn't lose any sanity!

"""
        self.assertEqual(mock_sysout.getvalue(), expected)