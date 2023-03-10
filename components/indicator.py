import plotly.graph_objects as go

class Indicator():
  def __init__(self, percentages: list, **kwargs) -> None:
    self.fig = go.Figure()
    self.fig.add_trace(
      go.Indicator(
        mode = 'number',
        value = percentages[0],
        domain = {'row': 0, 'column': 0},
        title = {'text': 'Excellence', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
        number = {'font_color' : '#3d9970', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
      )
      
    )
    self.fig.add_trace(
      go.Indicator(
        mode = 'number',
        value = percentages[1],
        domain = {'row': 0, 'column': 1},
        title = {'text': 'Mediocre', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
        number = {'font_color' : '#ff7400', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
      )
      
    )
    self.fig.add_trace(
      go.Indicator(
        mode = 'number',
        value = percentages[2],
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