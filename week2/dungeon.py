
class Dungeon():

    def __int__(self, dungeonmap):
        f = open('dungeonmap', 'r')
        self.mapp = f.read()
        f.close

asd = Dungeon("maps.txt")
