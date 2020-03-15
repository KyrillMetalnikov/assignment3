from unittest import TestCase
import monster


class Test(TestCase):
    def test_get_chris(self):
        actual = monster.get_chris()
        expected = {"HP": [1000, 1000], 'name': 'Chris', 'attack': 'Chris says "see?  wasn\'t so hard was it?"',
                    'type': 'monster'}
        self.assertEqual(actual, expected)
