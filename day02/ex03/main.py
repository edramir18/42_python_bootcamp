#! /usr/bin/env python3

from csvreader import CsvReader


def test_good_csv():
    with CsvReader('../resources/good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(header)
        for d in data:
            print(d)


def test_bad_csv():
    with CsvReader('../resources/bad.csv') as file:
        if file is None:
            print('File is corrupted')


def test_file_not_found():
    with CsvReader('bad.csv') as file:
        if file is None:
            print('File is corrupted')


if __name__ == '__main__':
    test_good_csv()
    test_bad_csv()
    test_file_not_found()