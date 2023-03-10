import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn import preprocessing
from collections import defaultdict


class Heatmap:
    def __init__(self, df: pd.DataFrame) -> None:
        d = defaultdict(preprocessing.LabelEncoder)
        df = df.apply(lambda x: d[x.name].fit_transform(x))
        self.corr = df.corr()
        self.fig = go.Figure(
            data=go.Heatmap(
                x=self.corr.index,
                y=self.corr.columns,
                z=self.corr.values,
                type='heatmap',
                colorscale='greens',
                text=np.round(self.corr.values, 2),
                texttemplate='%{text}',
                textfont={'size': 15},
                zmin=0,
                zmax=1,
                showscale=False,
                hovertemplate='%{z}<extra></extra>',
                hoverlabel=dict(
                    bgcolor='green',
                    font_size=20
                )
            ),
        )
        self.fig.update_layout(
            title='Correlation Map',
            title_font={'size': 30},
            width=1400,
            height=800,
            yaxis=dict(
                tickfont=dict(size=20),
                tickangle=0
            ),
            xaxis=dict(
                tickfont=dict(size=20),
            ),
        )
        for i in range(len(self.fig.layout.annotations)):
            self.fig.layout.annotations[i].font.size = 20
