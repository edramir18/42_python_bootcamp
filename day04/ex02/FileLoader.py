import numpy as np
import pandas as pd


class FileLoader:
    @staticmethod
    def load(filename):
        """

        :param string filename:
        :return: pd.DataFrame
        """
        df = None
        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(filename)
            if filename.endswith('.json'):
                df = pd.read_json(filename)
        except FileNotFoundError:
            print(f'File {filename} not found.')
            raise FileNotFoundError
        rows, columns = df.shape
        print(f'Loading dataset of dimensions {rows} x {columns}')
        return df

    @staticmethod
    def display(dataframe, n):
        """

        :param pd.DataFrame dataframe:
        :return:
        """
        if n < 0:
            print(str(dataframe.tail(n)))
        else:
            print(str(dataframe.head(n)))


if __name__ == '__main__':
    fl = FileLoader()
    data = fl.load('../resources/athlete_events.csv')
    fl.display(data, 10)
    fl.display(data, -10)
