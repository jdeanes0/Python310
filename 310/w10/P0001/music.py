"""
Modified version of the music class file used in the previous project, but simplified such that it holds much less information.

@author jdeanes0
@version 10/24/23

Other classes that exist for the purpose of polymorphism in P0000 can be ignored.
"""
import media

class Music(media.Media):
    """Contains the music-specific variables found in spotify-2000.csv"""
    _genre = None

    def __init__(self, title, release_year, artist, genre):
        """Constructs a song with every possible field provided by the Spotify-2000 .csv"""
        super().__init__(title, release_year, artist)
        self._genre = genre

    # below this point, we have getters but not setters, we will not need to mutate any data from the .csv
    def get_title(self) -> str:
        return self._title

    def get_release_year(self):
        return self._release_year

    def get_artist(self):
        return self._artist

    def get_genre(self):
        return self._genre

    def get_song_info(self):
        return f"{self._title} by {self._artist}"
    
    def __str__(self):
        return f"{self._title} by {self._artist}"

    # behavior to be polymorphise'm'd
    def play(self):
        """Returns a string about music"""

        return "Where words fall, music speaks, Hans Christian Anderson"

class Indie(Music):
    """For the indie genre, inherits the properties of Music"""

    def play(self):
        return "Music comes from the heart, not a big studio -Me"

class Electronic(Music):
    """For the electronic genre, inherits the properties of Music"""

    def play(self):
        return "Harder, better, faster, stronger. -Daft Punk"

class RnB(Music):
    """For the R&B genre, inherits the properties of Music"""

class Pop(Music):
    """For the pop genre, inherits the properties of Music"""

    def play(self):
        return "*POP* Noice. -That guy from that one meme"

class Rock(Music):
    """For the rock genre, inherits the properties of Music"""

    def play(self):
        return "I love rock and roll! -Joan Jett"

class Dembow(Music):
    """For the dembow genre, inherits the properties of Music"""

    def play(self):
        return "Unfortunately, this statement will never be seen with the original data set :("

class Generic(Music):
    """For music without one of our specified genres, this class also inherits the properties of Music"""

class Experimental(Indie):
    """For the experimental genre, inherits the properties of Indie"""

    def play(self):
        return "Science!"

class IndieRock(Indie):
    """For the indie rock genre, inherits the properties of Indie"""

class HipHop(RnB):
    """For the hip hop genre, inherits the properties of R&B"""

class Rap(HipHop):
    """For the rap genre, inherits the properties of HipHop"""

    def play(self):
        return "Life without knowledge is death in disguise, Kalib Kweli"

class Metal(Rock):
    """For the metal genre, inherits the properties of Rock"""

    def play(self):
        return "I'M PULLING YOUR STRINGS -Metallica"

class Punk(Rock):
    """For the punk genre, inherits the properties of Rock"""

    def play(self):
        return "Punk is musical freedom, Kurt Cobain"

class Country(Rock):
    """For the country genre, inherits the properties of Rock"""

    def play(self):
        return "I walk the line, Johnny Cash"

class VikingMetal(Metal):
    """For the viking metal genre, inherits the properties of Metal"""

    def play(self):
        return "Skål!"

class Eighties(Pop):
    """For the 80's genre that snuck by me, inherits the properties of pop"""
