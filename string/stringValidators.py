"""
Python has built-in string validation methods for basic data.
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).
"""
if __name__ == '__main__':
    s = raw_input()
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for c in s:
        if c.isalnum():
            alnum=True
        if c.isalpha():
            alpha=True
        if c.isdigit():
            digit = True
        if c.islower():
            lower = True
        if c.isupper():
            upper = True
    print alnum
    print alpha
    print digit
    print lower
    print upper
