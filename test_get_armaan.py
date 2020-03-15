from unittest import TestCase
import monster


class Test(TestCase):
    def test_get_armaan(self):
        actual = monster.get_armaan()
        expected = {"HP": [10, 10], 'name': 'Armaan',
                    'attack': 'Armaan says: Studies show students learn best when pushed to the edge!',
                    'type': 'monster'}
        self.assertEqual(actual, expected)