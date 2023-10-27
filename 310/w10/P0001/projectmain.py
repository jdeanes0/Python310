"""
Driver class for the P0001 project. Cool and Good.

@author jdeanes0
@version 10/25/23
"""

from avl import AVLTree
from music import Music

def test():
    """Function to test out particular bugs and stuffs."""
    pass

def search(param, tree:AVLTree):
    try:
        print(f"{tree.find(param)}")
    except:
        print("The program couldn't find a song. Please try again with another song title.")

def add(param, tree:AVLTree):
    """
    Get further input about song details from the user.
    Then, create a music object and insert it into the AVL Tree.
    """
    ryear = input("Release Year> ")
    artist = input("Artist> ")
    genre = input("Genre> ")

    song = Music(param, ryear, artist, genre)

    tree.insert(song)
    return tree # The tree has been updated so send it back.

def traverse(flag, tree:AVLTree):
    """Calls a function to do a traversal of the tree."""
    match flag:
        case 0:
            print(tree.inorder())
        case 1:
            print(tree.preorder())
        case 2:
            print(tree.postorder())

def info():
    print("--")
    print("--")
    print("--")
    print("--")
    print("Hello, my name is Jonathan Eanes! I am a COSC 310 student at Frostburg State University in October 2023.")
    print("If you happen to actually need to use this program for anything professional, I pity you.")
    print()
    print("This program is a CLI for an AVL tree. Simple as, really.")
    print()
    print("There are 7 commands:")
    print("search <name>: Searches for a song in the AVL tree and returns a matching song.")
    print("add <name>: Adds the name of a song to the tree and will prompt you for additional info about the song.")
    print("inorder: Prints an inorder traversal of the tree.")
    print("preorder: Prints a preorder traversal of the tree.")
    print("postorder: Prints a postorder traversal of the tree.")
    print("info: Re-Prints the information shown in this block to the console.")
    print("exit, x, q: Ends the program.")

def loop(tree:AVLTree): # Type safety! No? Kinda!
    """
    Runs the program's while loop for continuous operation.
    Takes an AVL tree as a parameter to be updated by the add command.
    """
    info() # Print all information once before starting the program

    while True:
        line = input("aReallyCoolGuy@aReallyCoolPlace ~$ ").split(" ") # Split input on the command line

        command = ""
        param = ""

        # Interpret the input to the command line so that there is a single parameter that stays together.
        tokenc = 0
        for token in line:
            if tokenc == 0:
                command += token
            else:
                param += token + " "
            tokenc += 1

        param = param.strip() # Remove the trailing whitespace from the parameter.

        match command:
            case "search":
                if not param:
                    print("You didn't give input, try again with syntax \"search <name>\"")
                else:
                    print("Attempting to find", param)
                    search(param, tree)
            case "add":
                if not param:
                    print("You didn't give input, try again with syntax \"add <name>\"")
                else:
                    print("Attempting to add", param)
                    tree = add(param, tree)
            case "inorder":
                # traverse(0, tree)
                tree.printTree()
            case "preorder":
                traverse(1, tree)
            case "postorder":
                traverse(2, tree)
            case "info":
                info()
            case "exit" | "q" | "x":
                print("Thank you for using my program. Goodbye.")
                break
            case default:
                print("Not a command. Please try again, or type \"info\" for more info.")

def load_data() -> AVLTree:
    """Grab the data from the .csv file and place it in the tree."""
    tree = AVLTree()
    file = open(r"310\w10\P0001\Spotify-2000_b-1.csv", "r", encoding="UTF8")

    file.readline() # skip header line of the .csv
    contents = file.readlines() # Read the entire file

    count = 0
    for line in contents: # For every line in the file, make an object and add it to the tree
        linearr = line.split(",")
        temp = Music(linearr[1], linearr[4], linearr[2], linearr[3])
        tree.insert(temp) # Insert the object into the tree
        if count == 501:
            tree.insert(temp)
        count += 1

    return tree

def main():
    """
    Driver function to call sub-functions in the path of the program.
    Because we have been asked to create "commands," it seems fitting to give each command its own function. 
    Also, there will be a loop function just to keep it out of main.
    """
    tree = load_data()
    loop(tree)

if __name__ == "__main__":
    test()
    main()
