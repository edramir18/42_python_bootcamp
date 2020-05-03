import pandas as pd


class SpatioTemporalData:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def where(self, year: int):
        return (self.df.query('Year == @year')['City'].drop_duplicates()
                .to_list())

    def when(self, city: str):
        return (self.df.query('City == @city')['Year'].drop_duplicates()
                .to_list())


if __name__ == '__main__':
    from FileLoader import FileLoader
    data_csv = FileLoader.load('../resources/athlete_events.csv')
    sp = SpatioTemporalData(data_csv)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
