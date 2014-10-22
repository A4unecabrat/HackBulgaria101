import unittest
from Orc import Orc
from Weapon import Weapon


class TestHero(unittest.TestCase):

    def test_hero(self):
        strong_orc = Orc("NotIvo", 1, 1)
        self.assertEqual(strong_orc.name, "NotIvo")
        self.assertEqual(strong_orc.health, 1)
        self.assertEqual(strong_orc.berserkfactor, 1)

    def test_get_health(self):
        strong_orc = Orc("NotIvo", 1, 1)
        self.assertEqual(strong_orc.get_health(), 1)

    def test_is_alive(self):
        strong_orc = Orc("NotIvo", 1, 1)
        strong_orc.battlehp = 0
        self.assertFalse(strong_orc.is_alive())

    def test_take_damage(self):
        strong_orc = Orc("NotIvo", 100, 1)
        strong_orc.take_damage(20)
        self.assertEqual(strong_orc.get_health(), 80)

    def test_take_healing(self):
        strong_orc = Orc("NotIvo", 100, 1)
        strong_orc.take_damage(100)
        self.assertFalse(strong_orc.take_healing(20))

    def test_take_healing2(self):
        strong_orc = Orc("NotIvo", 100, 1)
        strong_orc.take_damage(30)
        self.assertTrue(strong_orc.take_healing(20))

    def test_take_healing3(self):
        strong_orc = Orc("NotIvo", 100, 1)
        strong_orc.take_damage(10)
        strong_orc.take_healing(20)
        self.assertEqual(strong_orc.get_health(), 100)

    def test_orc_attack_with_weapon(self):
        strong_orc = Orc("NotIvo", 100, 2)
        strong_orc.equip_weapon(Weapon("axe", 35, 0.5))
        self.assertEqual(strong_orc.attack(), 70)

    def test_or_attack_wothout_weapon(self):
        strong_orc = Orc("NotIvo", 100, 2)
        self.assertEqual(strong_orc.attack(), 0)

if __name__ == '__main__':
    unittest.main()
