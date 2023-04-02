"""
Author: Drew Marschner
Date: 2023-04-02

Recurse Center Prompt: Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number.
If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop.
You can use any language.
"""

def crackle_pop():
    """ Return a list of numbers 1-100 with Crackle, Pop, and CracklePop replacing
     numbers divisible by 3, 5, and 3 and 5 respectively. """
    data = [i for i in range(1,101)]
    data[2:101:3] = ["Crackle"]*33
    data[4:101:5] = ["Pop"]*20
    data[14:101:15] = ["CracklePop"]*6
    return data

if __name__ == "__main__":
    print("\n".join(str(i) for i in crackle_pop()))