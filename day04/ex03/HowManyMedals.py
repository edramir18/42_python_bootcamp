import pandas as pd


def how_many_medals(data, name):
    """
    How many medals by name, year and type
    :param pd.DataFrame data: data to be analysed
    :param str name: Name athlete to evalued
    :return:
    """
    df_medal = (data.query('Name == @name').groupby(['Year', 'Medal'])['Event']
                .count())  # type: pd.Series
    return df_medal


if __name__ == '__main__':
    from FileLoader import FileLoader
    data_csv = FileLoader.load('../resources/athlete_events.csv')
    medals = how_many_medals(data_csv, 'Kjetil Andr Aamodt')
    print(medals)
