import panel as pn
from panel.widgets import Tabulator
import pandas as pd


class Table():
  def __init__(self, df: pd.DataFrame, index: list = None, columns: list = None, **kwargs):
    # Check params
    if len(df.columns) != len(columns):
      raise ValueError('The number of DataFrame columns is {}, while the size of the columns parameter is {}'.format(len(df.columns), len(columns)))
    # Customise index
    if not index: index = list(range(len(df)))
    df = df.set_index(pd.Index(index))
    # Prettify column titles
    col_map = {df.columns[i]: columns[i] for i in range(len(df.columns))}
    col_map['index'] = ''
    # Construct widget
    self.widget = Tabulator(
      df,
      layout='fit_data_fill',
      titles = col_map,
      **kwargs
    )
    
  def update(self, df: pd.DataFrame):
    self.widget.value = df
# class Table():
#     def __init__(self, data: pd.DataFrame, index: list = None, columns: list = None):
#         self.data = data
#         self.index = index
#         self.columns = columns
#         if self.index is not None:
#             self.data = self.data.set_index(pd.Index(self.index))
#         self.data.insert(0, '', index)

#         if self.columns is not None and len(self.columns) != (len(self.data.columns) - 1):
#             raise ValueError('columns length is {}, while data has {} columns'.format(len(columns), len(data.columns) - 1))
#         if self.columns: self.columns = [''] + self.columns

#         print(len(self.data.columns), len(self.columns))
#         # print({self.data.columns[i]: (self.columns[i] if self.columns else self.data.columns[i]) for i in range(len(self.data.columns))})
#         self.figure = Tabulator(
#             data,
#             layout='fit_data_fill',
#             page_size=10,
#             show_index=False,
#             titles={self.data.columns[i]: (self.columns[i] if self.columns else self.data.columns[i]) for i in range(len(self.data.columns))},
#         )

#     def update(self, df):
#         self.figure.value = df


