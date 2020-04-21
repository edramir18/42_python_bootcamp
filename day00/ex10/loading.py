import sys


def ft_progress(lst):
    size = len(lst)
    eta = size * 0.01
    size_len = len(str(size))
    for c, i in enumerate(lst):
        progress = f'{"":#>{(c + 1) * 100 // size // 4}}'
        print(f'\rETA {eta:4.2f}s [{progress:25}] {c + 1:{size_len}}/{size:{size_len}}'
              f' | elapsed time {c * 0.01:4.2f}s', end='', flush=True)
        yield i


if __name__ == '__main__':
    import time
    import random

    a = random.randint(1, 100)
    listy = range(a * 100)
    ret = 0
    for element in ft_progress(listy):
        ret += (element + 3) % 5
        time.sleep(0.01)
    print('\n' + str(ret))