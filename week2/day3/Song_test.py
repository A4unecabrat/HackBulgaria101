import unittest
from Song import Song


class SongTests(unittest.TestCase):

    def test_init(self):
        song = Song(
            "We Are!", "Hiroshi Kitadani", "One Piece OST", 5, 240, 512)
        self.assertEqual(song.title, "We Are!")
        self.assertEqual(song.artist, "Hiroshi Kitadani")
        self.assertEqual(song.album, "One Piece OST")
        self.assertEqual(song.length, 240)
        self.assertEqual(song.bitrate, 512)

    def test_rate(self):
        song = Song(
            "We Are!", "Hiroshi Kitadani", "One Piece OST", 5, 240, 512)
        song.rate(5)
        self.assertEqual(song.rating, 5)

    def test_rate_out_of_scope(self):
        with self.assertRaises(ValueError):
            song = Song(
                "We Are!", "Hiroshi Kitadani", "One Piece OST", 5, 240, 512)
            song.rate(7)

if __name__ == '__main__':
    unittest.main()
