import random
from Hero import Hero
from Orc import Orc


class Fight():

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def attack_first(self):
        return random.randrange(0, 100) < 50

    def simulate_fight(self):
        if self.attack_first():
            print("{} is first!".format(self.hero.known_as()))
            while self.hero.is_alive() and self.orc.is_alive():
                self.orc.take_damage(self.hero.attack())
                self.hero.take_damage(self.orc.attack())
        else:
            print("{} is first!".format(self.orc.name))
            while self.hero.is_alive() and self.orc.is_alive():
                self.hero.take_damage(self.orc.attack())
                self.orc.take_damage(self.hero.attack())
