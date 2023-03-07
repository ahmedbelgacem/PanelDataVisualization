import panel as pn
import numpy as np
import holoviews as hv
import pandas as pd
from components.table import Table
from components.Heatmap import Heatmap
from config import DATA_PATH

pn.extension(sizing_mode = 'stretch_width')
vanilla = pn.template.VanillaTemplate(title = 'Vanilla Template')
pn.widgets.Tabulator.theme = 'materialize'

df_data = pd.read_csv(DATA_PATH)
df_data['total score (%)'] = round((df_data['math score'] + df_data['reading score'] + df_data['writing score']) / 3, 1)
vanilla.main.append(Table(df_data, index = range(len(df_data)), columns = ['Gender', 'Race/Ethnicity', 'Parental level education', 'Lunch', 'Test prep. course', 'Math score (%)', 'Reading score (%)', 'Writing score (%)', 'Total score (%)']))

summary = df_data.describe().T[['min', 'mean', '75%','max']].astype(int)
index = ['math score', 'reading score', 'writing score', 'total score (%)']
summary_df = pd.DataFrame(summary, index = index)
vanilla.main.append(
    pn.Row(
        pn.Column(Table(summary_df, index, columns = ['Min. score', 'Avg. score', 'Q3', 'Max. score'])),
        pn.Column(Table(summary_df, index, columns = ['Min. score', 'Avg. score', 'Q3', 'Max. score']))
    )
)

xs = np.linspace(0, np.pi)
freq = pn.widgets.FloatSlider(name='Frequency', start=0, end=10, value=2)
phase = pn.widgets.FloatSlider(name='Phase', start=0, end=np.pi)

vanilla.main.append(
    pn.Row(
        pn.Card(Heatmap(df_data), title='Feature Correlation'),
    )
)
@pn.depends(freq=freq, phase=phase)
def sine(freq, phase):
    return hv.Curve((xs, np.sin(xs*freq+phase))).opts(
        responsive=True, min_height=400)

@pn.depends(freq=freq, phase=phase)
def cosine(freq, phase):
    return hv.Curve((xs, np.cos(xs*freq+phase))).opts(
        responsive=True, min_height=400)

vanilla.sidebar.append(freq)
vanilla.sidebar.append(phase)
vanilla.main.append(
    pn.Row(
        pn.Card(hv.DynamicMap(sine), title='Sine'),
        pn.Card(hv.DynamicMap(cosine), title='Cosine')
    )
)
vanilla.servable();