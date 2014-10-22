import random


class Weapon():

    def __init__(self, typewep="", damage=0, critical_stricke_persent=0):
        self.typewep = typewep
        self.damage = damage
        if critical_stricke_persent >= 0 and critical_stricke_persent <= 1:
            self.critical_stricke_persent = critical_stricke_persent
        else:
            raise ValueError

    def critical_hit(self):
        return random.random() <= self.critical_stricke_persent
