class Song():
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title, artist, album, rating, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.bitrate = bitrate
        if rating > Song.MAX_RATING or rating < Song.MIN_RATING:
            raise ValueError("IVO E PEDAL")
        else:
            self.rating = rating

    def rate(self, rating):
        if rating > Song.MAX_RATING or rating < Song.MIN_RATING:
            raise ValueError("IVO E PEDAL")
        else:
            self.rating = rating

    def __repr__(self):
        return str(self.__dict__)
