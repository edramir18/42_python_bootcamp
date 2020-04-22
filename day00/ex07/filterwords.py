import sys
from string import punctuation


def main():
    if len(sys.argv) != 3:
        print("\033[1;38;5;3mError\033[m")
        return
    words = str(sys.argv[1])
    size = int(sys.argv[2])
    a = [x for x in (a.strip(punctuation) for a in words.split())
         if len(x) > size]
    print(a)


if __name__ == '__main__':
    main()
