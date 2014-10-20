import unittest
from Weapon import Weapon


class TestWeapon(unittest.TestCase):

    def test_weapon(self):
        hammer = Weapon("hammer_of_ivo", 0, 0)
        self.assertEqual(hammer.typewep, "hammer_of_ivo")
        self.assertEqual(hammer.damage, 0)
        self.assertEqual(hammer.critical_stricke_persent, 0)

    def test_wepon_error(self):
        with self.assertRaises(ValueError):
            randomwep = Weapon("random", 45, 3)

    def test_critical_hit(self):
        pass
if __name__ == '__main__':
    unittest.main()
