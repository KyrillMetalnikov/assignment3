from unittest import TestCase
from unittest.mock import patch
import monster


class Test(TestCase):
    @patch("random.randint", side_effect=[5])
    def test_get_monster_amir(self, _):
        actual = monster.get_monster()
        expected = {"HP": [10, 10], 'name': 'Amir', 'attack': 'Amir rolls your name on his magic device!',
                    'type': 'monster'}
        self.assertEqual(actual, expected)

    @patch("random.randint", side_effect=[1])
    def test_get_monster_chris(self, _):
        actual = monster.get_monster()
        expected = {"HP": [1000, 1000], 'name': 'Chris', 'attack': 'Chris says "see?  wasn\'t so hard was it?"',
            'type': 'monster'}
        self.assertEqual(actual, expected)
