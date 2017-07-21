#! /usr/bin/env python3
from Jukebox import Jukebox

class User():
    """
    A class defining the user
    Attributes:
    interface: variable to hold the jukebox instance
    Methods:
    chooseSong()
    """
    interface = None

    def __init__(self):
        self.interface = Jukebox()

    def chooseSong(self, songName):
        self.interface.addSongToQueue(songName)

    def removeSong(self, songName):
        self.interface.removeSongFromQueue(songName)

    def playSongNow(self, songName):
        self.interface.playSongNow(songName)
