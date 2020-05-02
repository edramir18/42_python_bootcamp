import pandas as pd


def proportion_by_sport(data, year, sport, gender):
    """
    Return the proportion of participants who played given sport by genere
    :param pd.DataFrame data:
    :param int year:
    :param string sport:
    :param string gender:
    :return:
    """
    played = (data.query('Year == @year and Sex == @gender')
              .drop_duplicates(['Name']))
    total = len(played.index)
    return len(played.query('Sport == @sport').index) / total


if __name__ == '__main__':
    from FileLoader import FileLoader
    data_csv = FileLoader.load('../resources/athlete_events.csv')
    percent = proportion_by_sport(data_csv, 2004, 'Tennis', 'F')
    print(percent)
    percent = proportion_by_sport(data_csv, 2004, 'Tennis', 'M')
    print(percent)
