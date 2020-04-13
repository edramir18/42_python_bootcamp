#! /usr/bin/env python


def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
    }
    for k, v in languages.items():
        print(f'{k} was created by {v}')


if __name__ == '__main__':
    main()
