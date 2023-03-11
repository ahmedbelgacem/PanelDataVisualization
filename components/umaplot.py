import pandas as pd
import umap
from sklearn.preprocessing import LabelEncoder
import plotly.graph_objects as go
import plotly.express as px
  
class UMAPlot():
  def __init__(self, df: pd.DataFrame, **kwargs) -> None:
    le = LabelEncoder()
    df_enc = df.copy()
    df_enc['Gender'] = le.fit_transform(df_enc['Gender'])
    df_enc['Lunch'] = le.fit_transform(df_enc['Lunch'])
    df_enc['Test prep. course'] = le.fit_transform(df_enc['Test prep. course'])
    
    df_enc = pd.get_dummies(df_enc, columns = ['Race/Ethnicity', 'Parental level education'])
    
    reducer = umap.UMAP(n_neighbors = 10, min_dist = 0.1, metric = 'euclidean')
    X_proj = reducer.fit_transform(df_enc.values)
    
    self.fig = go.Figure(
      data = go.Scatter(
        x = X_proj[:, 0],
        y = X_proj[:, 1],
        customdata = df.values,
        hovertemplate = 'Gender = <b>%{customdata[0]}</b><br>' +
                        'Race/Ethnicity = <b>%{customdata[1]}</b><br>' + 
                        'Parental level education = <b>%{customdata[2]}</b><br>' + 
                        'Lunch = <b>%{customdata[3]}</b><br>' + 
                        'Test prep. course = <b>%{customdata[4]}</b><br>' + 
                        'Math score (%) = <b>%{customdata[5]}</b><br>' + 
                        'Reading score (%) = <b>%{customdata[6]}</b><br>' + 
                        'Writing score (%) = <b>%{customdata[7]}</b><br>' + 
                        'Total score (%) = <b>%{customdata[8]}</b><br>' + 
                        '<extra></extra>',
        hoverlabel = dict(
          font_size = 12,
          font_family = 'montserrat'
        ),
        marker = dict(
          color = df_enc['Total score (%)'],
          size = 10,
          colorscale = 'greens',
          showscale = True,
        ),
        mode = 'markers'
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