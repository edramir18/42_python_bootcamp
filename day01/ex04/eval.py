from functools import reduce


class Evaluator:
    def __init__(self):
        pass

    def validate(coefs, words):
        if type(coefs) != list or type(words) != list:
            raise TypeError("Invalid argument")
        elif not reduce(lambda r, x: r and type(x) in [int, float],
                        coefs, True):
            raise ValueError("Coefs list has invalid values")
        elif not reduce(lambda r, x: r and type(x) == str, words, True):
            raise ValueError("Words list has invalid values")

    def zip_evaluate(coefs, words):
        Evaluator.validate(coefs, words)
        if len(coefs) != len(words):
            return -1
        return reduce(lambda r, t: r + len(t[0]) * t[1], zip(words, coefs), 0)

    def enumerate_evaluate(coefs, words):
        Evaluator.validate(coefs, words)
        if len(coefs) != len(words):
            return -1
        return reduce(lambda r, v: r + len(v[1]) * coefs[v[0]],
                      enumerate(words), 0)
