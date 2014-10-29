import json


class Playlist():

    LOW_BITRATE = 256

    def __init__(self, name):
        self.name = name
        self.songlist = []

    def add_song(self, Song):
        self.songlist.append(Song)

    def remove_song(self, songname):
        for song in self.songlist:
            if song.title == songname:
                self.songlist.remove(song)
                break

    def total_length(self):
        result = 0
        for song in self.songlist:
            result += song.length
        return result

    def remove_disrated(self, goodrating):
        result = []
        for i in range(0, len(self.songlist)):
            if self.songlist[i].rating >= goodrating:
                result.append(self.songlist[i])
        self.songlist = result
        return self.songlist

    def remove_bad_quality(self):
        result = []
        for i in range(0, len(self.songlist)):
            if self.songlist[i].bitrate > Playlist.LOW_BITRATE:
                result.append(self.songlist[i])
        self.songlist = result
        return self.songlist

    def show_artists(self):
        result = []
        for song in self.songlist:
            if song.artist not in result:
                result.append(song.artist)
        return result

    def __str__(self):
        return '\n'.join("{} {} {}:{}".format(
            song.artist, song.title, song.length // 60,
            song.length % 60) for song in self.songlist)

    def save(self, file_name):
        """json_dict = {"name": self.name,
                     "songs": [{"title": song.title,
                                "artist": song.artist,
                                "album": song.album,
                                "rating": song.rating,
                                "length": song.length,
                                "bitrate": song.bitrate}
                               for song in self.songlist]}"""
        f = open(file_name, 'r+')
        f.write(json.dumps(self.__dict__, indent=4, separators=(',', ': ')))
        f.close()
