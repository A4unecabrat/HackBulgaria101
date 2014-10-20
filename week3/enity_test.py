import unittest
from enity import Enity


class Testenity(unittest.TestCase):

    def test_hero(self):
        something = Enity("Ivo", 1,)
        self.assertEqual(something.name, "Ivo")
        self.assertEqual(something.health, 1)

    def test_get_health(self):
        something = Enity("Ivo", 1)
        self.assertEqual(something.get_health(), 1)

    def test_is_alive(self):
        something = Enity("Ivo", 1)
        something.battlehp = 0
        self.assertFalse(something.is_alive())

    def test_take_damage(self):
        something = Enity("Ivo", 100)
        something.take_damage(20)
        self.assertEqual(something.get_health(), 80)

    def test_take_healing(self):
        something = Enity("Ivo", 100)
        something.take_damage(100)
        self.assertFalse(something.take_healing(20))

    def test_take_healing2(self):
        something = Enity("Ivo", 100,)
        something.take_damage(30)
        self.assertTrue(something.take_healing(20))

    def test_take_healing3(self):
        something = Enity("Ivo", 100,)
        something.take_damage(10)
        something.take_healing(20)
        self.assertEqual(something.get_health(), 100)

if __name__ == '__main__':
    unittest.main()
