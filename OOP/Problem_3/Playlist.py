#! /usr/bin/env python3
from Song import Song
import pdb

class Playlist():
    """
    A class that will hold the playlist
    Attributes:
    songList: List of all songs
    songQueue: Current song queue
    """

    songListInitial = [
        { "name": "Someone Like You", "artist": "Adele", "genre": "pop" },
        { "name": "Hometown Glory", "artist": "Adele", "genre": "pop" },
        { "name": "Run Tis Town", "artist": "Jay-Z", "genre": "hip-hop" },
        { "name": "Lose Yourself", "artist": "Eminem", "genre": "hip-hop" }
    ]

    def __init__(self):
        self.songList = [] #variable to hold the list of songs here
        self.queue = [] #variable to hold the song queue
        self.loadSongList()

    def loadSongList(self):
        for song in self.songListInitial:
            # pdb.set_trace()
            self.songList.append(Song(song['name'], song['artist'], song['genre']))
        return True

    def getSongQueue(self):
        return self.queue

    def lookUpSong(self, songName):
        #method to look up song by name
        songLookUp = [song for song in self.songList if song.name == songName]
        if len(songLookUp) is not 1:
            return ValueError("Sorry something went wrong")
        else:
            return songLookUp[0]

    def addSongToQueue(self, songName): #song has to be song name
        try:
            song = self.lookUpSong(songName)
            self.queue.append(song)
            self.playSong()
        except ValueError:
            print("Sorry, could not find song")
            print("Please pick another song")

    def removeSongFromQueue(self, songName): #song should be song name
        try:
            song = self.lookUpSong(songName)
            self.queue.remove(song)
        except ValueError:
            print("Sorry, could not find song in queue")

    def getCurrentSongDetails(self):
        print("Name: ", self.queue[0].name)
        print("Artist: ", self.queue[0].artist)
        print("Genre: ", self.queue[0].genre)
        return self.queue[0]

    def playSong(self):
        #method to play first song in queue
        self.getCurrentSongDetails()
        if self.queue[0].isPlaying is False:
            self.queue[0].changePlayStatus()

    def playNextSong(self):
        #method to switch to the next song
        self.removeSongFromQueue(self.queue[0].name)
        self.playSong()

    def playSongNow(self, songName):
        #method to move song to front of queue
        try:
            song = self.lookUpSong(songName)
            self.queue.insert(0, songName)
        except (ValueError, IndexError) as e:
            print("Sorry, something went wrong")

    def skipCurrentSong(self):
        try:
            del skip.queue[0]
            self.playSong()
        except ValueError:
            print("Sorry, could not skip song")

    def replayCurrentSong(self):
        self.playSong()
