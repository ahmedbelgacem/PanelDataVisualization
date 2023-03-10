import panel as pn
from panel.widgets import Tabulator
import pandas as pd
import plotly.graph_objects as go


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

class PlotlyTable():
  def __init__(self, df: pd.DataFrame, header: list = None, **kwargs) -> None:
    header_vals = header if header else list(df.columns)
    header_vals = [f'<b>{col}' for col in header_vals]
    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda v: f'<b>{v}')
    self.fig = go.Figure(
      data = [ go.Table(
        header = dict(
          values = header_vals,
          fill_color='rgba(49, 99, 149, 1.)',
          align = 'left',
          font = dict(color = 'white', size = 12),
        ),
        cells = dict(
          values = [df[col] for col in df.columns],
          align = 'left',
          font = dict(size = 12, color = ['white', 'black'], family = 'montserrat'),
          height = 30,
          fill = dict(color = ['rgba(49, 99, 149, 1.)', 'rgba(49, 99, 149, .2)']),
        )
      )
    ])
    self.fig.update_layout(
      **kwargs,
      title_font = {'size': 20, 'color': 'black', 'family': 'montserrat'},
      paper_bgcolor = 'rgba(0,0,0,0)',
      plot_bgcolor = 'rgba(0,0,0,0)',
    )
    
  def update(self, df):
    self.fig.update_traces(
      header = dict(values = list(df.columns)),
      cells = dict(values = [df[col] for col in df.columns]),
    )