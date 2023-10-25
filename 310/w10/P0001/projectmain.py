"""
Driver class for the P0001 project. Cool and Good.

@author jdeanes0
@version 10/24/23
"""

import kvpair
from avl import AVLTree
from music import Music

def test():
    """Testing function, TODO: Delete later."""
    asong = Music("Hey, Soul Sister", 2010, "Train", "neo mellow")
    sample = kvpair.KVPair(asong)
    print(sample)

    if "a" < "b": print("yes1")
    # from this statement we can gather that values at the front end of the alphabet are in fact lesser than those at the end
    if "aaaaaaaaaaab" < "aaaaaaaaaaac": print("does it go that far in?")
    # from this statement we can gather that < & > can be used to sort entire words. That's a good sign.

def search(param, tree:AVLTree):
    try:
        print(tree.find(param))
    except:
        print("The program couldn't find a song. Please try again with another song title.")

def add(param, tree:AVLTree):
    # TODO: Create a music object here.
    tree.insert(param)

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
    Takes an AVL tree as a parameter.
    """
    info() # Print all information once before starting the program

    while True:
        line = input("aReallyCoolGuy@aReallyCoolPlace ~$ ")
        tmp = line.split(" ") # split input tokens on the command line

        command = tmp[0]
        try:
            param = tmp[1] # Python loves its index out of range errors. I know its out of range! I only need this sometimes!
        except IndexError:
            param = None

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
                    add(param, tree)
            case "inorder":
                traverse(0, tree)
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
