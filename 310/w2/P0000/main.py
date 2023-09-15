"""
Driver class for P000

1: Reads and stores the information in the spotify.csv
2: Reads and stores the information in interests.csv
3: I don't know right now but I'll figure it out later go go go

@author jdeanes0
@version 9/13/23
"""

import media
import music
from student import Student310 as st

john_lennon_fortnite = media.Media("Fortnite", 2017, "John Lennon")

print(john_lennon_fortnite)

free_bird = music.Rock("Lynyrd Skynrd", 1973, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

print(free_bird.play())
print(free_bird.get_valence())

def loadStudents():
    """
    Function that puts each line of interests.csv into its own Student310 object.
    Not too bad yet!
    """

    length_reader = open("310/w2/P0000/interests.csv", "r", encoding="utf8")
    interests_len = len(length_reader.readlines()) - 1 # This gets the total length of the file

    interests = open("310/w2/P0000/interests.csv", "r", encoding="utf8")
    interests.readline() # Skip the first line of the file with the headers

    students = [st(None, None, None, None)]*25 # List of 25 empty student310 objects to be overwritten
    for x in range(interests_len): # Begin iterating through the entire file
        line = interests.readline().split(",")

        # Set anime to false by default, and set it to true if the character is a +
        is_anime_liker = False
        if line[2] == '+':
            is_anime_liker = True

        students[x] = st(line[0], line[1], is_anime_liker, line[3]) # Construct a student and insert them into the list
    
    return students

def loadSongs():
    """
    Function that opens Spotify-2000.csv and assigns each song a class to be put in a giant list.
    This will be expensive.
    """

def main():
    """Driver function that runs the script to access the data and objects"""
    students = loadStudents()
    songs = loadSongs() # I am dreading coding this function

main()
