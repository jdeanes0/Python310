"""Testing to see how a bucket sort impacts time taken to complete the sort"""

import time

# with open("310\w2\sorting_test\dataset.txt", "r") as file:
#     dataset_words = list(file.read().split())

# start = time.time()

# sorts according to the first letter
def letter_sort(e):
    """Sorting key for .sort by first letter, just an example of how to use sorting keys."""
    return e[0]

CON1 = ["b", "o", "a", "c"]
CON2 = ["z", "o", "p", "d"]

def bucketize(arr):
    """
    Takes a given array and makes many small arrays out of it based on a characteristic.
    For the purposes of this program, it will bucketize based on first letter.
    There will be 4 buckets in total: A-F, G-M, N-S, T-Z.
    
    @param arr: list of the raw data
    @return: list containing 4 lists
    """

    # First, find out how to get the ascii values for different chars in python which will make the logic easier
    # ord("str") works to get the ascii values
    arrAF, arrGM, arrNS, arrTZ = [], [], [], []

    for i in range(len(arr)):
        if ord(arr[i][0]) < 103:
            arrAF.append(arr[i])
        elif ord(arr[i][0]) >= 103 & ord(arr[i][0]) < 110:
            arrGM.append(arr[i])
        elif ord(arr[i][0]) >= 110 & ord(arr[i][0]) < 116:
            arrNS.append(arr[i])
        else: # sloppy but I do not care (Mike Tomlin: "We do not care.")
            arrTZ.append(arr[i])

    arr_of_arrs = [arrAF, arrGM, arrNS, arrTZ] # array of arrays to return
    return arr_of_arrs

def drive_it():
    """
    When called, will start everything and handle everything.

    Intended to be called from another file.
    """
    with open("310/w2/sorting_test/dataset.txt", "r", encoding="UTF8") as file:
        raw = list(file.read().split())
    
    start = time.time()

    r_of_rs = bucketize(raw)

    # for every list in the list, bubble sort it
    for arr in r_of_rs:
        bubble_sort(arr)
    
    # collate based on groups of two
    # easy to hard code, difficult to make bendable
    # going to hard code for now
    # TODO: make recursive function to do what has been done below
    collated = collate(collate(r_of_rs[0], r_of_rs[1]), collate(r_of_rs[2], r_of_rs[3]))

    delta_time = time.time() - start
    print(f"The process took {delta_time} seconds to complete.")

    with open("310\w2\sorting_test\dataset out.txt", "w") as file:
        for i_2 in collated:
            file.write(i_2 + "\n")

def bubble_sort(lis):
    """
    Default bubble sort function without anything fancy
    
    @param lis: unsorted list
    @return: sorted list via bubble sort
    """

    # TODO: make this function deep sort the strings, recursive?
    for i in range(len(lis) - 1):
        for j in range(len(lis) - i - 1):
            if lis[j][0] > lis[j+1][0]:
                temp = lis[j]
                lis[j] = lis[j+1]
                lis[j + 1] = temp

    return lis

def collate(list1, list2):
    """
    Function that collates two lists
    
    @param list1: SORTED list
    @param list2: additional SORTED list
    @return: collated combination of the two input lists
    """
    
    total_len = len(list1) + len(list2)
    current_val1, current_val2 = 0,0 # first foray into double assignment, they both equal zero

    final = [] # will be equal to len(list1) + len(list2)
    for i in range(total_len - 1):
        # Check if a list has been fully incremented through and if so, break the loop and dump the contents of that list
        if current_val1 == len(list1) or current_val2 == len(list2):
            if current_val1 == len(list1): # If 1 is empty, empty 2
                for i in range(current_val2, len(list2)):
                    final.append(list2[i])
            else: # otherwise, empty the contents of list1 into the final list
                for i in range(current_val1, len(list1)):
                    final.append(list1[i])
            break # After either condition is true, break the loop and go to return
        # compare the two values, equals shouldnt really matter
        # place the lowest in the final list
        # increment one from the list where the lowest value was found
        if list1[current_val1] > list2[current_val2]:
            final.append(list2[current_val2])
            current_val2 += 1
        else:
            final.append(list1[current_val1])
            current_val1 += 1
        # This needs a second function to happen before the if statement that will populate the final 
        # list with the remaining elements if one composite list is entirely empty.

    return final

# bubble_sort(CON1)
# bubble_sort(CON2)

# collated = collate(CON1, CON2)
# dataset_words.sort(key=letter_sort)

# delta_time = time.time() - start

# with open("310\w2\sorting_test\dataset out.txt", "w") as file:
#     for i_2 in collated:
#         file.write(i_2 + "\n")

# print(f"The process took {delta_time} seconds to complete.")
