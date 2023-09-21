"""
Driver class for P000

1: Reads and stores the information in the spotify.csv
2: Reads and stores the information in interests.csv
3: I don't know right now but I'll figure it out later go go go

@author jdeanes0
@version 9/18/23
"""

import media
import music
from student import Student310 as st

john_lennon_fortnite = media.Media("Fortnite", 2017, "John Lennon")

print(john_lennon_fortnite)

free_bird = music.Rock("Lynyrd Skynrd", 1973, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

print(free_bird.play())
print(free_bird.get_valence())

def determine_genre(specific_genre: str):
    """
    Honestly a quite messy method that determines the genre that a particular song belongs to.
    Returns string out of a set of possible strings.
    """

    specific_genre = specific_genre.lower()
    genres = ["indie", "electronic", "r&b", "pop", "indie rock", "dembow", "experimental", "rock", "hiphop", "rap", "viking metal", "punk", "country", "metal"]
    """Contains all known genres, used to match."""

    for g in genres:            ###        ###                             ###
        if g in specific_genre: ### STEVE! ### THIS IS WHY PYTHON IS GOOD! ###
            print(g)
            return g            ###        ###                             ###
        
    return "generic" # If a genre can't be matched, go and return that it's generic.

def load_students():
    """
    Function that puts each line of interests.csv into its own Student310 object.
    Not too bad yet!
    """

    length_reader = open("310/w2/P0000/interests.csv", "r", encoding="utf8")
    interests_len = len(length_reader.readlines()) - 1 # This gets the total length of the file

    interests = open("310/w2/P0000/interests.csv", "r", encoding="utf8")
    interests.readline() # Skip the first line of the file with the headers

    students = [st(None, None, None, None)]*25 # List of 25 empty student310 objects to be overwritten
    for i in range(interests_len): # Begin iterating through the entire file
        line = interests.readline().split(",") # Place each line of the file into its own list upon splitting it at commas

        # Set anime to false by default, and set it to true if the character is a +
        is_anime_liker = False
        if line[2] == '+':
            is_anime_liker = True

        students[i] = st(line[0], line[1], is_anime_liker, line[3]) # Construct a student and insert them into the list
    
    return students

def load_songs() -> list[music.Music]:
    """
    Function that opens Spotify-2000.csv and assigns each song a class to be put in a giant list.
    This will be expensive.
    """
    length_reader = open("310/w2/P0000/Spotify-2000.csv", "r", encoding="utf8")
    songs_len = len(length_reader.readlines()) - 1 # This gets the total length of the file

    songs_file = open("310/w2/P0000/Spotify-2000.csv", "r", encoding="utf8")
    songs_file.readline() # Skip the header line

    # Acquire space in memory for 1,994 Music objects
    # NOTE: Genre can be found at index no.4
    songs = [music.Music(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)]*1994

    for i in range(songs_len):
        line = songs_file.readline().split(",") # Place each line of the file into its own list upon splitting it at commas

        # Large if statement to determine genre based on line[4]
        genre = determine_genre(str(line[3])) # Kidding! It's been encapsulated/abstracted/whatever.

        current_song = None # initialize variable

        match genre:
            case "generic":
                # title:1, release year:4, artist:2, index:0, genre:3, continues normally from here
                current_song = music.Generic(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "indie":
                current_song = music.Indie(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "electronic":
                current_song = music.Electronic(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "r&b":
                current_song = music.RnB(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "pop":
                current_song = music.Pop(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "rock":
                current_song = music.Rock(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "dembow":
                current_song = music.Dembow(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "experimental":
                current_song = music.Experimental(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])



    return songs # There will be a lot above here to work out.

def main():
    """Driver function that runs the script to access the data and objects"""
    students = []
    songs = []

    students = load_students()
    songs = load_songs() # I am dreading coding this function

main()
