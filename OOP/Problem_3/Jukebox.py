#! /usr/bin/env python3
from Playlist import Playlist

class Jukebox():
    """
    Main jukebox class that will be the brain of the operations
    Attributes:
    currentSong: Current song playing
    songQueue: Queue of songs
    addSong: add song to queue
    removeSong: remove song from queue
    skipSong: skip current song
    playSongNow: play inserted song immediately
    """

    playlist = None #variable to hold the playlist class instance

    def __init__(self):
        self.playlist = Playlist()

    def currentSong(self):
        return self.playlist.getCurrentSong()

    def songQueue(self):
        return self.playlist.getSongQueue()

    def loadPlaylist(self):
        return self.playlist.loadSongList()

    def addSongToQueue(self, name): #add song by name
        self.playlist.addSongToQueue(name)

    def removeSongFromQueue(self, name):
        self.playlist.removeSong(name)

    def skipCurrentSong(self): #skip current song and play next
        self.playlist.skipSong()

    def playSongNow(self, name): #skip remaining songs and play now
        self.playlist.playNow(name)
