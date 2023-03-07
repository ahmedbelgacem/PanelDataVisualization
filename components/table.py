import panel as pn
from panel.widgets import Tabulator
import pandas as pd


class Table():
    def __init__(self, data: pd.DataFrame, index: list = None, columns: list = None):
        self.data = data
        self.index = index
        self.columns = columns
        # if self.index is not None:
        #     self.data = self.data.set_index(pd.Index(self.index))
        # self.data.insert(0, '', index)
        #
        # if self.columns is not None and len(columns) != len(data.columns) - 1:
        #     raise ValueError(
        #         'columns length is {}, while data has {} columns'.format(len(columns), len(data.columns) - 1))
        # if self.columns: columns = [''] + columns

        self.figure = Tabulator(
            data,
            layout='fit_data_fill',
            page_size=10,
            show_index=False,
            #titles={data.columns[i]: (columns[i] if columns else data.columns[i]) for i in range(len(data.columns))},
        )

    def update(self, df):
        self.figure.value = df
