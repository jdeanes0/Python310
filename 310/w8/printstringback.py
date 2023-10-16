"""
Recursive method to print a string backwards
Yeah. I coded it already.

@author jdeanes0
@version 10/16/23
"""

def __sback(word, i):
    if i == 0:
        return word[0]
    
    # print("got here:", i)
    return word[i] + __sback(word, i-1)


def sback(word):
    i = len(word) - 1
    return __sback(list(word), i)

print(sback("Is this function a good example of printing out a string backwards?"))
