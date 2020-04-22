def ft_progress(lst):
    size = len(lst)
    eta = size * 0.01
    for k, v in enumerate(lst, start=1):
        pct = (k * 20) // size
        progress = f'{"":#>{pct}}'
        print(f'\rETA {eta:4.2f}s [{progress:20}] {k:5}/{size:<5}'
              f'| elapsed time {k * 0.01:4.2f}s', end='', flush=True)
        yield v


if __name__ == '__main__':
    import time
    import random

    a = random.randint(500, 1000)
    listy = range(a)
    ret = 0
    for element in ft_progress(listy):
        ret += (element + 3) % 5
        time.sleep(0.01)
    print('\n' + str(ret))