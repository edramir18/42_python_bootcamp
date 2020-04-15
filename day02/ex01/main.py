#! /usr/bin/env python3
def what_are_the_vars(*args, **kwargs):
    """Your code"""
    if args is None and kwargs is None:
        return None
    c = ObjectC()
    for i, k in enumerate(args):
        setattr(c, f'var_{i}', k)
    for k, v in kwargs.items():
        if getattr(c, k, None) is not None:
            return None
        setattr(c, k, v)
    return c


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(objt):
    if objt is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(objt):
        if attr[0] != '_':
            value = getattr(objt, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)