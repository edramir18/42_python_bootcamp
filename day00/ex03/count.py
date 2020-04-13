#! /usr/bin/env python

import fileinput
import string


def text_analyzer(text=None):
    """
    Function to count the number of uppercase, lowercase, punctuation and spaces characters on a text.

    :param text: String to be analyzed
    :return: print the count of each type of character to the standard output
    """
    lower = 0
    upper = 0
    space = 0
    punctuation = 0
    if text is None:
        text = input("What is the text to analyse?\n")
    for k in list(text):
        if k.islower():
            lower += 1
        elif k.isupper():
            upper += 1
        elif k in string.punctuation:
            punctuation += 1
        elif k.isspace():
            space += 1
    print(f'The text contains {len(text)} characters:\n')
    print(f'- {upper} upper letters\n')
    print(f'- {lower} lower letters\n')
    print(f'- {punctuation} punctuation marks\n')
    print(f'- {space} spaces')
