"""
Driver code for week 11

@author jdeanes0
@version 10/30/23
"""

def main():
    s = "Jonathan Denali Eanes"

    count = 0
    for char in s:
        if count < len(s) - 1:
            print(ord(char), end=":")
        else:
            print(ord(char), end="\n")
        count += 1

if __name__ == "__main__":
    main()
