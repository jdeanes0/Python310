"""
Driver code for P0010, the one about hash maps.

@author jdeanes0
@version 11/14/23

11/25/23: Today I will be making the gameplay loop
"""

from structures import hashmap
from structures import record

def info():
    """Prints out a blurb that says how to use the program."""
    print("Welcome to the Jonathan Eanes's hashtable program!")
    print("-")
    print("-")
    print("-")
    print("-")
    print("There are 10 commands:")
    print("add: Add a new entry into the hashtable.")
    print("delete <quote>: Remove an entry.")
    print("find <movie>: Print out all entries under a movie's name.")
    print("printHT: Prints the hashtable.")
    print("load: Prints the current and max load factors.")
    print("count: Prints the number of items in the table")
    print("buckets: Prints the number of occupied buckets in the hashtable.")
    print("who: Prints the user's name.")
    print("help | ?: Prints information about the program.")
    print("exist: Quits the program")

def add(h: hashmap.HashMap):
    quote = input("quote> ")
    title = input("title> ")
    tom = input("type of media> ")
    try:
        year = int(input("year> "))
    except:
        year = -1
        print("Entered value was not an integer, year set to -1.")

    h.add(record.Record(quote, title, tom, year))

    return h

def delete(h: hashmap.HashMap, param):
    """Deletes an entry in the hash table based on the value in :param:."""
    h.delete(param)
    
    return h

def find(h: hashmap.HashMap, param):
    """Finds an entry in the hash table."""
    
    print(h.find("param"))

# print is easy to do

def get_ht_load():
    pass

def who():
    pass

def load() -> hashmap.HashMap:
    """
    Populates the data set 
    
    :return: A hashmap populated with all of the movie quotes.
    """
    h = hashmap.HashMap()
    csv = open(r"310/w13/P0010/movie_quotes.csv", "r", encoding="UTF8")

    csv.readline() # skip the header
    contents = csv.readlines()

    for line in contents:
        linearr = line.split(",")
        h.add(record.Record(linearr[0], linearr[1], linearr[2], int(linearr[3])))
    # And I think that's it?

    return h

def loop(h: hashmap.HashMap):
    """
    Contains the infinite loop for the program where the user will use commands.

    :param h: A hashmap populated with the movie quotes.
    """
    info()
    # print(h)

    run_loop = True

    while (run_loop):
        line = input("aReallyCoolGuy@hashprogram ~$ ").split(" ") # Split input on the command line

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
            case "add":
                h = add(h)
                print("Added entry.")
            case "delete":
                h = delete(h, param)
            case "find":
                h = find(h, param)
            case "help" | "?":
                info()
            case "quit":
                print("Goodbye!")
                break
            case default:
                print("Command not recognized. Type \"info\" for more information.")

def main():
    """
    Main function in the project, controls the program flow by initializing the data structure
    and beginning the user-driven loop.
    """
    h = load()
    loop(h)

if __name__ == "__main__":
    main()
