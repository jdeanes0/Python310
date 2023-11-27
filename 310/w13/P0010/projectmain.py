"""
Driver code for P0010, the one about hash maps.

@author jdeanes0
@version 11/26/23

11/25/23: Today I will be making the program loop
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
    print("add: Add a new quote into the hashtable.")
    print("delete <movie>: Remove all quotes from a movie from the hash table.")
    print("find <movie>: Print out all entries under a movie's name.")
    print("printHT: Prints the hashtable.")
    print("load: Prints the current and max load factors.")
    print("count: Prints the number of items in the table")
    print("buckets: Prints the number of occupied buckets in the hashtable.")
    print("who: Prints the user's name.")
    print("help | ?: Prints information about the program.")
    print("exit: Quits the program")

def add(h: hashmap.HashMap):
    """Gets additional information from the user to place a new quote into the hash table."""
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
    truth = h.delete(param)
    if truth:
        print("Delete operation successful.")
    else:
        print("Could not find movie to delete.")
    
    return h

def find(h: hashmap.HashMap, param):
    """Finds an entry in the hash table."""
    
    h.find(param)

# print is easy to do, will not be it's own function.

def get_ht_load(h: hashmap.HashMap):
    """Prints the current load on the hashtable."""
    print(h.return_load())

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
    uname = input("\n\n\nBut first, who are you?\n")

    print("Hello " + str(uname))

    while (run_loop):
        line = input(str(uname) + "@hashprogram ~$ ").split(" ") # Split input on the command line

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
                find(h, param)
            case "printHT":
                print(h)
            case "load":
                get_ht_load(h)
            case "count":
                print(h.count)
            case "buckets":
                print(h.buckets)
            case "help" | "?":
                info()
            case "who":
                # print's the user's name
                print(uname)
            case "exit":
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
