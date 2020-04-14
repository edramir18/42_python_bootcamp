import random


def generator(text, sep=" ", option=None):
    """Option is an optional arg, sep is mandatory"""
    if type(text) != str or type(sep) != str:
        raise TypeError
    elif len(sep) == 0:
        raise ValueError("empty separator")
    text_list = str(text).split(sep)
    if type(option) == str:
        if option == 'shuffle':
            random.shuffle(text_list)
        elif option == 'ordered':
            text_list.sort()
        elif option == 'unique':
            text_list = set(text_list)
    for word in text_list:
        yield word
