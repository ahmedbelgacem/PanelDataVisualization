import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn import preprocessing
from collections import defaultdict

class Heatmap():
  def __init__(self, df: pd.DataFrame) -> None:
    d = defaultdict(preprocessing.LabelEncoder)
    df = df.apply(lambda x: d[x.name].fit_transform(x))
    self.corr = df.corr()
    self.fig = go.Figure(
      data = go.Heatmap(
        x = self.corr.index,
        y = self.corr.columns,
        z = self.corr.values,
        type = 'heatmap',
        colorscale = 'blues',
        text = np.round(self.corr.values, 2),
        texttemplate = '%{text}',
        textfont = {'size': 12, 'family': 'montserrat'},
        zmin = 0,
        zmax = 1,
        showscale = False,
        hovertemplate = '%{z}<extra></extra>',
        hoverlabel = dict(
          bgcolor = 'rgba(49, 99, 149, 1.)',
          font_size = 12,
          font_family = 'montserrat'
        )
      ),
    )
    self.fig.update_layout(
      title = 'Correlation Map',
      title_font = {'size': 20, 'family': 'montserrat', 'color': 'black'},
      width = 1000,
      height = 600,
      yaxis = dict(
        tickfont = dict(size = 12, family = 'montserrat'),
        tickangle = 0
      ),
      xaxis = dict(
        tickfont = dict(size = 12, family = 'montserrat'),
      ),
    )
    for i in range(len(self.fig.layout.annotations)):
      self.fig.layout.annotations[i].font.size = 20