#! /usr/bin/env python3

class Song():
    """
    A class representing a song.
    Attributes:
    Name: name of the song
    Artist: name of the artist of the song
    Genre: genre of the song,
    isPlaying: Boolean to determine if song is playing
    """

    def __init__(self, name, artist, genre, isPlaying = False):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.isPlaying = isPlaying

    def getSongName(self):
        return self.name

    def getSongArtist(self):
        return self.artist

    def getSongGenre(self):
        return self.genre

    def changePlayStatus(self):
        self.isPlaying = not self.isPlaying
