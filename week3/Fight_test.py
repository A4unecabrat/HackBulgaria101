import unittest
from Fight import Fight
from Hero import Hero
from Orc import Orc
from Weapon import Weapon


class TestFight(unittest.TestCase):

    def test_fight_init(self):
        hero = Hero("Natsu", 10000, "DragonSlayer")
        orc = Orc("BadOrc", 100, 2)
        fight = Fight(hero, orc)
        self.assertEqual(fight.hero, hero)
        self.assertEqual(fight.orc, orc)

    def test_fight_simulation(self):
        hero = Hero("Natsu", 10000, "DragonSlayer")
        orc = Orc("BadOrc", 100, 2)
        fight = Fight(hero, orc)
        dragonpower = Weapon("Dragonpower", 200, 0.8)
        axe = Weapon("Axe", 120, 0.4)
        fight.hero.weapon = dragonpower
        fight.orc.weapon = axe
        fight.simulate_fight()
        self.assertEqual(fight.orc.battlehp, 0)
        self.assertTrue(fight.hero.battlehp > 0)


if __name__ == '__main__':
    unittest.main()
