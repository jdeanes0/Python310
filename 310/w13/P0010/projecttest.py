"""
Testing script for P0010

My first time doing this, so you better be happy, Steve.

@author jdeanes0
@version 11/21/23
"""

from structures import linkedlist
from structures import record
from structures import hashmap

def run_hashmap_test():
    hm = hashmap.HashMap()

    hm.add(record.Record("Do or do not, there is no try.","SW 5","movie", 1971))
    hm.add(record.Record("Do or do not, there is no tru.","SW 4","movie", 1971))
    hm.add(record.Record("Do or do not, there is no trip.","SW 5","movie", 1971))

    hm.find("SW 5")
    hm.find("SW 6")

    print(hm)


def get_first_words(title:str) -> str | None:
    """
    Returns the first two words of a string.

    If this fails, return nothing.
    """

    tokens = title.split(" ")
    if len(tokens) < 3:
        return title
    else: # If there are 3 or more tokens, return the first two tokens concatenated.
        returnable = ""
        count = 0
        for token in tokens:
            count += 1

            returnable += token + " "
            if count == 2:
                return returnable
        
        return
    
def run_words_test():
    zero = ""
    one = "Airplane!"
    two = "Good Burger"
    three = "An Unexpected Journey"
    four = "Return of the King"

    print(get_first_words(zero))
    print(get_first_words(one))
    print(get_first_words(two))
    print(get_first_words(three))
    print(get_first_words(four))

def run_ll_delete_test():
    """
    I'm still not sure if I'm doing this right but it's the thought that counts, right?
    """
    ll = linkedlist.LL()

    ll.add(record.Record("Do or do not, there is no try.","SW 5","movie", 1971))
    ll.add(record.Record("Do or do not, there is no tru.","SW 5","movie", 1971))
    ll.add(record.Record("Do or do not, there is no trip.","SW 5","movie", 1971))

    print(ll)

    ll.delete("Do or do not, there is no trip.")

    print(ll)

if __name__ == "__main__":
    # run_ll_delete_test()
    # run_words_test()
    run_hashmap_test()