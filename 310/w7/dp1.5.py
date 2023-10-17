"""We are going to do this in O(n) time for the challenge"""

gnums = [2,2,1,1,1,2,2]

def high_val_in_dict(dict: dict):
    highest = 0
    highestkey = None

    for kv in dict:
        if dict.get(kv) is not None:
            if dict.get(kv,0) > highest: # literally ignored with type cleansing
                highest = dict.get(kv)
                highestkey = kv

    return highestkey

def run(nums):
    # Begin a for loop over the entire list
    # dictionary to hold nums
    mydict = {}
    for i in range(len(nums)):
        # I'm thinking a dictionary for this
        if nums[i] not in mydict:
            mydict[nums[i]] = 1 # begin count with first object
        if nums[i] in mydict:
            mydict[nums[i]] += 1 # increment once in the dictionary
    
    highest = high_val_in_dict(mydict)
    print(highest)

run(gnums)
