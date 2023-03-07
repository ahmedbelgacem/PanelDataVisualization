import panel as pn
from panel.widgets import Tabulator
import pandas as pd

def Table(data : pd.DataFrame, index: list = None, columns: list = None):
  if index:
    data = data.set_index(pd.Index(index))
  data.insert(0, '', index)

  if columns and len(columns) != len(data.columns) - 1:
    raise ValueError('columns length is {}, while data has {} columns'.format(len(columns), len(data.columns) - 1))
  if columns: columns = [''] + columns

  return Tabulator(
    data, 
    layout = 'fit_data_fill', 
    page_size = 10, 
    show_index = False,
    titles = {data.columns[i]: (columns[i] if columns else data.columns[i]) for i in range(len(data.columns))},
  )