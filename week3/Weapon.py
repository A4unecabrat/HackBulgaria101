import random


class Weapon():

    def __init__(self, typewep, damage, critical_stricke_persent):
        self.typewep = typewep
        self.damage = damage
        if critical_stricke_persent >= 0 and critical_stricke_persent <= 1:
            self.critical_stricke_persent = critical_stricke_persent
        else:
            raise ValueError
