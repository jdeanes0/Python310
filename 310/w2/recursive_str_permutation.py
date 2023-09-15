"""
This file aims to create a recursive method for creating all possible permutations of a word.
This will also be used to mess with input and output configurations.

@author jdeanes0
"""

with open("310/w2/in.txt", "r") as file:
    STR1 = file.read()
with open("310/w2/out.txt", "w") as file3:
    file3.write("")

def to_string(list1):
    """Turns a list into a readable string."""
    return ''.join(list1)

def permute(word, start_i, end_i):
    """Prints all possible permutations of a string."""
    if start_i == end_i:
        with open("310/w2/out.txt", "a") as file2:
            file2.write(to_string(word) + "\n")
        # print(to_string(word))
    else:
        for i in range(start_i, end_i):
            word[start_i], word[i] = word[i], word[start_i]
            permute(word, start_i + 1, end_i)
            word[start_i], word[i] = word[i], word[start_i]

permute(list(STR1), 0, len(STR1))
