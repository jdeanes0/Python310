"""
Class that contains information for Students in the interests.csv file

@author jdeanes0
@version 9/18/23
"""

class Student310:
    """Student constructed by the interests.csv file"""

    __name = None
    __dogs_cats = None
    __anime = None
    __preferred_genre = ""
    __recommendation_1 = None
    __recommendation_2 = None

    def __init__(self, name, dogs_cats, anime, preferred_genre):
        self.__name = name
        self.__dogs_cats = dogs_cats
        self.__anime = anime
        self.__preferred_genre = preferred_genre

    def set_recommendations(self, recommendation1, recommendation2): # Can I see this?
        """Set the recommendations for the Student310 object"""
        self.__recommendation_1 = recommendation1
        self.__recommendation_2 = recommendation2

    def get_recommendation1(self):
        return self.__recommendation_1

    def get_recommendation2(self):
        return self.__recommendation_2

    def get_name(self):
        return self.__name

    def get_animal(self):
        return self.__dogs_cats

    def get_anime(self):
        return self.__anime

    def get_genre(self) -> str:
        return self.__preferred_genre

    def __str__(self):
        return f"Name: {self.__name} Animal: {self.__dogs_cats} Likes Anime?: {self.__anime} Preferred Genre: {self.__preferred_genre}"
