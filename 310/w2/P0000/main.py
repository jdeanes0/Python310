"""
Driver class for P000

1: Reads and stores the information in the spotify.csv
2: Reads and stores the information in interests.csv
3: I don't know right now but I'll figure it out later go go go

@author jdeanes0
@version 9/28/23
"""

import media
import music
import random as r

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
    genres = ["indie", "electronic", "r&b", "pop", "indie rock", "dembow", "experimental", "80's",
              "rock", "rap", "viking metal", "punk", "country", "metal", "g funk", "east coast hip hop", "detroit hip hop", "hip hop"]
    # Contains all known genres, used to match.

    for g in genres:            ###        ###                             ###
        if g in specific_genre: ### STEVE! ### THIS IS WHY PYTHON IS GOOD! ###
            print(g)
            return g            ###        ###                             ###
        
    return "generic" # If a genre can't be matched, return that it's generic.

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

    length_reader.close()
    interests.close()
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

    # Acquire space in memory for 1,994 references
    # NOTE: Genre can be found at index no.4
    songs = []

    for _ in range(songs_len):
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
            case "indie rock":
                current_song = music.IndieRock(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "hip hop": # Just in case that it's spelled differently.
                current_song = music.HipHop(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "rap":
                current_song = music.Rap(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "g funk":
                current_song = music.Rap(line[1], line[4], line[2], line[0], "rap", line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "east coast hip hop":
                current_song = music.Rap(line[1], line[4], line[2], line[0], "rap", line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "detroit hip hop":
                current_song = music.Rap(line[1], line[4], line[2], line[0], "rap", line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "metal":
                current_song = music.Metal(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "punk":
                current_song = music.Punk(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "country":
                current_song = music.Country(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "viking metal":
                current_song = music.VikingMetal(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case "80's":
                current_song = music.Eighties(line[1], line[4], line[2], line[0], genre, line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            case _:
                print("If you get this message, then there is an issue with the data set.")

        songs.append(current_song)

    length_reader.close()
    songs_file.close()
    return songs # There will be a lot above here to work out.

def get_student_song_array(songs, genre, poss_student_songs):
    """Takes an empty array or a partially filled array and fills it with songs that match the genre"""
    for song in songs:
        if song.get_genre() == genre:
            poss_student_songs.append(song) # If we find a song of the correct genre, add it to a list of possible songs

    return poss_student_songs

def set_recommendations(students: list[st], songs):
    """Generates 2 recommended songs for each student."""
    # Iterate through our list of students
    for s in students:
        s_genre = s.get_genre().lower() # Get the student's preferred genre
        # Iterate through the list of songs
        poss_student_songs = []
        poss_student_songs = get_student_song_array(songs, s_genre, poss_student_songs)

        # If a song is not found, then we need to go up in the inheritance tree until an actual song is found.
        if len(poss_student_songs) < 2:
            if s_genre == "viking metal":
                s_genre = "metal"
            if s_genre == "dembow":
                s_genre = "generic"
            if s_genre == "rap":
                s_genre = "hip hop"
            if s_genre == "r&b":
                s_genre = "generic"
            if s_genre == "experimental":
                s_genre = "indie"
            if s_genre == "indie rock":
                s_genre = "indie"
            if s_genre == "80's":
                s_genre = "pop"
            if s_genre == "electronic":
                s_genre = "generic"

            poss_student_songs = get_student_song_array(songs, s_genre, poss_student_songs) # call it again with the new genre

        # With the list of possible songs, we now need to randomly set two for each student.
        # Still iterating through the students, choose two random indicies between 0 and len(poss_student_songs)
        max_index = len(poss_student_songs) - 1
        print(max_index)
        i1 = r.randint(0, max_index)
        i2 = r.randint(0, max_index)

        if i1 == i2: # We will have a problem if they equal each other
            # We will simply increment the second one. However
            if i2 == max_index: # If we are at the end of the list, we need to set it to the beginning.
                i2 = int(0)
            else:
                i2 += 1
        
        song1 = poss_student_songs[i1]
        song2 = poss_student_songs[i2]

        print(song1.play())
        print(song2.play())

        s.set_recommendations(song1, song2) # Sets the two recommendations!

        
def print_recommendations(students):
    """
    Iterates through the list of students and prints out their recommendations.

    Now to a particular file!
    """
    output = open(r"C:\Users\under\OneDrive\Documents\GitHub\Python310\310\w2\P0000\output.txt", "w")

    for s in students:
        output.write(str(s))

    output.close()

def main():
    """Driver function that runs the script to access the data and objects"""
    students = []
    songs = []

    students = load_students()
    songs = load_songs() # I am dreading coding this function

    # Ok. All of the songs and students have been loaded.
    # Now, we need to get the recommendations.
    set_recommendations(students, songs)

    print_recommendations(students)

main()
