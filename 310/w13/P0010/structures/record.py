"""
Class to package movie quote data.

@author jdeanes0
@version 11/14/23
"""

class Record:
    """
    Simple class for holding and accessing movie data.

    Getters are needed to read data, Setters should not be needed.
    """

    """ Fields """

    __quote = ""
    __movie = ""
    __type_of_media = ""
    __year = -1

    """ Constructor """

    def __init__(self, quote: str, movie: str, tom: str, year: int):
        """Store the values of a movie quote in a record object."""
        self.__quote = quote
        self.__movie = movie
        self.__type_of_media = tom
        self.__year = year

    """ Getters """

    def get_quote(self) -> str:
        return self.__quote

    def get_movie(self) -> str:
        return self.__movie

    def get_type(self) -> str:
        return self.__type_of_media

    def get_year(self) -> int:
        return self.__year
    
    def __str__(self) -> str:
        """Provide a nice string to be printed out about the movie."""
        return f"{self.__quote} is from the {self.__type_of_media} {self.__movie}, which was released in {self.__year}."
    
