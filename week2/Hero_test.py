import unittest
from Hero import Hero


class TestHero(unittest.TestCase):

    def test_hero(self):
        weak_hero = Hero("Ivo", 1, "Weakling")
        self.assertEqual(weak_hero.name, "Ivo")
        self.assertEqual(weak_hero.health, 1)
        self.assertEqual(weak_hero.nickname, "Weakling")

    def test_known_as(self):
        weak_hero = Hero("Ivo", 1, "Weakling")
        self.assertEqual(weak_hero.known_as(), "Ivo the Weakling")

    def test_get_health(self):
        weak_hero = Hero("Ivo", 1, "Weakling")
        self.assertEqual(weak_hero.get_health(), 1)

    def test_is_alive(self):
        weak_hero = Hero("Ivo", 1, "Weakling")
        weak_hero.battlehp = 0
        self.assertFalse(weak_hero.is_alive())

    def test_take_damage(self):
        weak_hero = Hero("Ivo", 100, "Weakling")
        weak_hero.take_damage(20)
        self.assertEqual(weak_hero.get_health(), 80)

    def test_take_healing(self):
        weak_hero = Hero("Ivo", 100, "Weakling")
        weak_hero.take_damage(100)
        self.assertFalse(weak_hero.take_healing(20))

    def test_take_healing2(self):
        weak_hero = Hero("Ivo", 100, "Weakling")
        weak_hero.take_damage(30)
        self.assertTrue(weak_hero.take_healing(20))

    def test_take_healing3(self):
        weak_hero = Hero("Ivo", 100, "Weakling")
        weak_hero.take_damage(10)
        weak_hero.take_healing(20)
        self.assertEqual(weak_hero.get_health(),100)


if __name__ == '__main__':
    unittest.main()
