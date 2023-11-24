"""
Testing script for P0010

My first time doing this, so you better be happy, Steve.

@author jdeanes0
@version 11/21/23
"""

from structures import linkedlist
from structures import record

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
    run_ll_delete_test()