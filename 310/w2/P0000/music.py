"""
All classes related to music will be in this file. I just can't deal with making an individual 
file for EVERY class.

Because of how python deal with constructors and the inheritance of variables, this file is going to be VERY BIG

I AM DROWNING IN BOILERPLATE STEVE

@author jdeanes0
@version 9/12/23

Classes for categorizing the songs in the spotify file. Anything that is not part of our dataset is considered to 
be "Generic".
"""
import media

class Music(media.Media):
    """Contains the music-specific variables found in spotify-2000.csv"""
    _index = None
    _genre = None
    _bpm = None
    _energy = None
    _danceability = None
    _loudness = None
    """Measured in dB (decibels)"""
    _liveness = None
    _valence = None
    _length = None
    """Measured in seconds"""
    _acousticness = None
    _speechiness = None
    _popularity = None

    def __init__(self, title, release_year, artist, index, genre, bpm, energy, danceability, loudness, liveness, valence, length, acousticness, speechiness, popularity):
        """Constructs a song with every possible field provided by the Spotify-2000 .csv"""
        super().__init__(title, release_year, artist)
        self._index = index
        self._genre = genre
        self._bpm = bpm
        self._energy = energy
        self._danceability = danceability
        self._loudness = loudness
        self._liveness = liveness
        self._valence = valence
        self._length = length
        self._acousticness = acousticness
        self._speechiness = speechiness
        self._popularity = popularity

    # below this point, we have getters but not setters, we will not need to mutate any data from the .csv
    def get_title(self):
        return self._title

    def get_release_year(self):
        return self._release_year

    def get_artist(self):
        return self._artist

    def get_index(self):
        return self._index

    def get_genre(self):
        return self._genre

    def get_bpm(self):
        return self._bpm

    def get_energy(self):
        return self._energy

    def get_danceability(self):
        return self._danceability

    def get_loudness(self):
        return self._loudness

    def get_liveness(self):
        return self._liveness

    def get_valence(self):
        return self._valence

    def get_length(self):
        return self._length

    def get_acousticness(self):
        return self._acousticness

    def get_speechiness(self):
        return self._speechiness

    def get_popularity(self):
        return self._popularity

    # behavior to by polymorphise'm'd
    def play(self):
        """Returns a string about music"""

        return "Where words fall, music speaks, Hans Christian Anderson"

class Indie(Music):
    """For the indie genre, inherits the properties of Music"""

class Electronic(Music):
    """For the electronic genre, inherits the properties of Music"""

class RnB(Music):
    """For the R&B genre, inherits the properties of Music"""

class Pop(Music):
    """For the pop genre, inherits the properties of Music"""

class Rock(Music):
    """For the rock genre, inherits the properties of Music"""

class Dembow(Music):
    """For the dembow genre, inherits the properties of Music"""

class Generic(Music):
    """For music without one of our specified genres, this class also inherits the properties of Music"""

class Experimental(Indie):
    """For the experimental genre, inherits the properties of Indie"""

class IndieRock(Indie):
    """For the indie rock genre, inherits the properties of Indie"""

class HipHop(RnB):
    """For the hip hop genre, inherits the properties of R&B"""

class Rap(HipHop):
    """For the rap genre, inherits the properties of HipHop"""

class Metal(Rock):
    """For the metal genre, inherits the properties of Rock"""

class Punk(Rock):
    """For the punk genre, inherits the properties of Rock"""

class Country(Rock):
    """For the country genre, inherits the properties of Rock"""

class VikingMetal(Metal):
    """For the viking metal genre, inherits the properties of Metal"""
