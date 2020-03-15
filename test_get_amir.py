from unittest import TestCase
import monster


class Test(TestCase):
    def test_get_amir(self):
        actual = monster.get_amir()
        expected = {"HP": [10, 10], 'name': 'Amir', 'attack': 'Amir rolls your name on his magic device!',
                    'type': 'monster'}
        self.assertEqual(actual, expected)