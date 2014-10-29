import unittest
from Playlist import Playlist
from Song import Song


class Playlisttest(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist("random")
        song1 = Song(
            "We Are!", "Hiroshi Kitadani", "One Piece OST", 5, 240, 512)
        song2 = Song(
            "We Are!", "Hiroshi Kitadani", "One Piece OST", 5, 240, 512)
        self.playlist.add_song(song1)
        self.playlist.add_song(song2)

    def test_save(self):
        #self.playlist.save("jason.txt")
        print(self.playlist.__dict__)
if __name__ == '__main__':
    unittest.main()
