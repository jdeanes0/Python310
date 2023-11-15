"""
Driver code for P0010, the one about hash maps.

@author jdeanes0
@version 11/14/23
"""

from structures import hashmap

def info():
    """Prints out a blurb that says how to use the program."""

def load() -> hashmap.HashMap:
    """
    Populates the data set 
    
    :return: A hashmap populated with all of the movie quotes.
    """
    h = hashmap.HashMap()
    return h

def loop(h: hashmap.HashMap):
    """
    Contains the infinite loop for the program where the user will use commands.

    :param h: A hashmap populated with the movie quotes.
    """
    info()

    run_loop = True

    while (run_loop):
        pass

def main():
    """
    Main function in the project, controls the program flow by initializing the data structure
    and beginning the user-driven loop.
    """

if __name__ == "__main__":
    main()
