"""
Python file for Steve's media parent class, which is basically useless
(It does hold a few general variables!)
@author jdeanes0
@version 9/12/23
"""

class Media:
    """Abstract class for P0000"""

    #protected variables
    _title = None
    _release_year = None
    _artist = None

    def __init__(self, title, release_year, artist):
        """Creates a piece of media with information about the title, year of release,
        and the artist."""
        self._title = title
        self._release_year = release_year
        self._artist=artist

    def __str__(self) -> str:
        return f"{self._title} was released in {self._release_year} by {self._artist}."
