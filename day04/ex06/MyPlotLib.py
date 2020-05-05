import pandas as pd
import matplotlib.pyplot as plt


class MyPlotLib:
    @staticmethod
    def histogram(data: pd.DataFrame, features: list):
        data.hist(column=['Height', 'Weight'])
        plt.show()

    @staticmethod
    def density(data: pd.DataFrame, features: list):
        ...

    @staticmethod
    def pait_plot(data: pd.DataFrame, features: list):
        ...

    @staticmethod
    def box_plot(data: pd.DataFrame, features: list):
        ...


if __name__ == '__main__':
    from FileLoader import FileLoader
    data_csv = FileLoader.load('../resources/athlete_events.csv')
    MyPlotLib.histogram(data_csv, ['Height', 'Weight'])
