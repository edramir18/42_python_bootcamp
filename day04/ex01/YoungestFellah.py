import pandas as pd


def youngestFellah(data, year):
    """
    Calculate the youngest woman and men from dataset based on year
    :param pd.DataFrame data:
    :param int year:
    :return:
    """
    a = 1
    return {
        'man': data.query('Sex == "M" and Year == @year').min().Age,
        'woman': data.query('Sex == "F" and Year == @year').min().Age,
    }


if __name__ == '__main__':
    from FileLoader import FileLoader
    data = FileLoader.load('../resources/athlete_events.csv')
    youngests = youngestFellah(data, 2004)
    print(f'Male: {youngests["man"]} Female: {youngests["woman"]}')