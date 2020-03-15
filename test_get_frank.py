from unittest import TestCase
import monster


class Test(TestCase):
    def test_get_frank(self):
        actual = monster.get_frank()
        expected = {"HP": [10, 10], 'name': 'Frank', 'attack': 'Frank assigns an assignment that\'s 100% fun!',
                    'type': 'monster'}
        self.assertEqual(actual, expected)
