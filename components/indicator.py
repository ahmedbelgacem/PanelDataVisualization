import plotly.graph_objects as go
import pandas as pd

class Indicator():
  def __init__(self, df: pd.DataFrame, **kwargs) -> None:
    values = [int(df['Total score (%)'].between(70, 100).sum()*100/len(df)), int(df['Total score (%)'].between(50, 70).sum()*100/len(df)), int(df['Total score (%)'].between(0, 50).sum()*100/len(df))]
    self.fig = go.Figure()
    self.fig.add_trace(
      go.Indicator(
        name = 'excellence',
        mode = 'number',
        value = values[0],
        domain = {'row': 0, 'column': 0},
        title = {'text': 'Excellence', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
        number = {'font_color' : '#3d9970', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
      )
      
    )
    self.fig.add_trace(
      go.Indicator(
        name = 'mediocrity',
        mode = 'number',
        value = values[1],
        domain = {'row': 0, 'column': 1},
        title = {'text': 'Mediocrity', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
        number = {'font_color' : '#ff7400', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
      )
      
    )
    self.fig.add_trace(
      go.Indicator(
        name = 'failure',
        mode = 'number',
        value = values[2],
        domain = {'row': 0, 'column': 2},
        title = {'text': 'Failure', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
        number = {'font_color' : '#ff4136', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
      )
      
    )
    self.fig.update_layout(
      **kwargs,
      grid = {'rows': 1, 'columns': 3, 'pattern': 'independent'},
      paper_bgcolor = 'rgba(0,0,0,0)',
      plot_bgcolor = 'rgba(0,0,0,0)',
    )
    
  def update(self, df):
    values = [int(df['Total score (%)'].between(70, 100).sum()*100/len(df)), int(df['Total score (%)'].between(50, 70).sum()*100/len(df)), int(df['Total score (%)'].between(0, 50).sum()*100/len(df))]
    self.fig.update_traces(value = values[0], selector = dict(name = 'excellence'))
    self.fig.update_traces(value = values[1], selector = dict(name = 'mediocrity'))
    self.fig.update_traces(value = values[2], selector = dict(name = 'failure'))