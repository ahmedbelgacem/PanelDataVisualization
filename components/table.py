import panel as pn
from panel.widgets import Tabulator
import pandas as pd

def Table(data : pd.DataFrame):
  data = data.set_index(pd.Index(['A']*len(data)))
  return Tabulator(data, layout = 'fit_data_stretch', page_size = 10)