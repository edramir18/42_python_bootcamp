#! /usr/bin/env python


def main():
    t = (0, 4, 132.42222, 10000, 12345.67)
    print(f'day_{t[0]:02,}, ex_{t[1]:02} : {t[2]:.2f}, {t[3]:.2e}, {t[4]:.2e}')
    return


if __name__ == '__main__':
    main()
