"""
Data class for P0001.

Contains in it a key and a value
Key: Name of the song
Value: Music object containing the song info

@author jdeanes0
@version 10/24/23
"""

from music import Music

class KVPair:
    """Class of data nodes in P0001's AVL project."""

    __key:str = ""
    __value:Music = Music(None, None, None, None)

    def __init__(self, song:Music):
        """Constructor object, takes a song as input to construct an appropriate key-value pairing."""
        self.__key = song.get_title()
        self.__value = song

    def get_key(self):
        return self.__key
    
    def get_value(self):
        return self.__value

    def __str__(self):
        """Returns a simple printout of all the pair's characteristics."""
        return f"\"{self.__key}\" is a song by {self.__value.get_artist()}. It is a {self.__value.get_genre()} song that was popular in {self.__value.get_release_year()}."