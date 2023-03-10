import pandas as pd
import plotly.graph_objects as go

class CountPlot():
  def __init__(self, df: pd.DataFrame, **kwargs) -> None:
    count = df['Gender'].value_counts()
    self.fig = go.Figure(
      data = go.Bar(
        x = count.index,
        y = count.values,
        text = list(count.values),
        hovertemplate = '%{x} - %{y}<extra></extra>',
        marker_color = ['#ff7400', '#316395'],
      )
    )
    self.fig.update_layout(
      **kwargs,
      font_family = 'montserrat',
      title = 'Gender Distribution',
      title_font = {'size': 20},
      paper_bgcolor = 'rgba(0,0,0,0)',
      plot_bgcolor = 'rgba(0,0,0,0)',
      yaxis = dict(
        showticklabels = False
      ),
      xaxis = dict(
        tickmode = 'array',
        tickvals = ['female', 'male'],
        ticktext = ['Female', 'Male'],
        tickfont = dict(size = 15),
      ),
    )
    self.fig.update_traces(textposition = 'outside', textfont_size = 17)