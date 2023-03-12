import pandas as pd
import plotly.graph_objects as go 

class BoxPlot():
  def __init__(self, df: pd.DataFrame, **kwargs) -> None:
    self.fig = go.Figure()
    self.fig.add_trace(
      go.Box(
        name = 'Math score (%)',
        x = df['Math score (%)'],
        text = ['hello']*5,
        hoverinfo = 'none'
      )
    )
    self.fig.add_trace(
      go.Box(
        name = 'Writing score (%)',
        x = df['Writing score (%)'],
        hoverinfo = 'none'
      )
    )
    self.fig.add_trace(
      go.Box(
        name = 'Reading score (%)',
        x = df['Reading score (%)'],
        hoverinfo = 'none'
      )
    )
    self.fig.update_layout(
      **kwargs,
      font_family = 'montserrat',
      title_font = {'size': 20},
      paper_bgcolor = 'rgba(0,0,0,0)',
      plot_bgcolor = 'rgba(0,0,0,0)',
      yaxis = dict(
        showticklabels = False
      ),
      xaxis = dict(
        showticklabels = False
      ),
    )

    for i, col in enumerate(['Math score (%)', 'Writing score (%)', 'Reading score (%)']):
      for q in [0, .25, .5, .75, 1]:
        self.fig.add_annotation(
          name = '{} - {}'.format(col, q),
          x = df[col].quantile(q), 
          y = i + .4,
          text = '{}'.format(df[col].quantile(q)),
          showarrow = False,
          font = dict(
            color = (i == 0)*'#636efa' + (i == 1)*'#ef553b' + (i == 2)*'#00cc96',
            size = 12
          ),
        )
  def update(self, df: pd.DataFrame):
    self.fig.update_traces(
      x = df['Math score (%)'],
      selector = dict(name = 'Math score (%)')
    )
    self.fig.update_traces(
      x = df['Writing score (%)'],
      selector = dict(name = 'Writing score (%)')
    )
    self.fig.update_traces(
      x = df['Reading score (%)'],
      selector = dict(name = 'Reading score (%)')
    )
    for i, col in enumerate(['Math score (%)', 'Writing score (%)', 'Reading score (%)']):
      for q in [0, .25, .5, .75, 1]:
        self.fig.update_annotations(
          selector = dict(name = '{} - {}'.format(col, q)),
          x = df[col].quantile(q), 
          y = i + .4,
          text = '{}'.format(df[col].quantile(q)),
        )