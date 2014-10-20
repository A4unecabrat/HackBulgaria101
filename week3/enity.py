class Enity():

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.battlehp = health

    def get_health(self):
        return self.battlehp

    def is_alive(self):
        return self.battlehp != 0

    def take_damage(self, damage):
        if self.battlehp - damage < 0:
            self.battlehp = 0
        else:
            self.battlehp -= damage

    def take_healing(self, healing):
        if not self.is_alive():
            return False
        elif self.battlehp == self.health:
            return True
        elif self.battlehp + healing > self.health:
            self.battlehp = self.health
            return True
        else:
            self.battlehp += healing
            return True
