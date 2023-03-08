import panel as pn
import numpy as np
import holoviews as hv
import pandas as pd
from components.table import Table
from components.Heatmap import Heatmap
from config import DATA_PATH

pn.extension(sizing_mode='stretch_width')
vanilla = pn.template.VanillaTemplate(title='Student Performance in Exams - Explanatory Data Analysis')
pn.widgets.Tabulator.theme = 'materialize'
# Preparing the data table
df_data = pd.read_csv(DATA_PATH)
df_data['total score (%)'] = round((df_data['math score'] + df_data['reading score'] + df_data['writing score']) / 3, 1)
columns = ['Gender', 'Race/Ethnicity', 'Parental level education', 'Lunch', 'Test prep. course',
           'Math score (%)', 'Reading score (%)', 'Writing score (%)', 'Total score (%)']
summary_index = ['math score', 'reading score', 'writing score', 'total score (%)']
data_table = Table(df_data, index=list(range(len(df_data))),
                   columns=columns, page_size = 10)
# This selector is used to filter on race/ethnicity and gender
race_select = pn.widgets.Select(name="race/ethnicity", options=['All', 'A', 'B', 'C', 'D', 'E'])
gender_select = pn.widgets.Select(name="gender", options=['All', 'male', 'female'])
education_select = pn.widgets.Select(name="education",
                                     options=['All', "bachelor's degree", 'some college', "master's degree",
                                              "associate's degree", 'high school', 'some high school'])
lunch_select = pn.widgets.Select(name="lunch", options=['All', 'standard', 'free/reduced'])
preparation_select = pn.widgets.Select(name="preparation", options=['All', 'none', 'completed'])

# Preparing the summary table
summary = df_data.describe().T[['min', 'mean', '75%', 'max']].astype(int)
summary_df = pd.DataFrame(summary, index=summary_index)
summary_table = Table(summary_df, summary_index, columns=['Min. score', 'Avg. score', 'Q3', 'Max. score'])


@pn.depends(race=race_select, gender=gender_select, education=education_select, lunch=lunch_select,
            preparation=preparation_select, watch=True)
def filtering(race, gender, education, lunch, preparation):
    df_new = df_data
    if race != 'All':
        df_new = df_new[df_data['race/ethnicity'] == f"group {race}"]
    if gender != 'All':
        df_new = df_new[df_data['gender'] == f"{gender}"]
    if education != 'All':
        df_new = df_new[df_data['parental level of education'] == f"{education}"]
    if lunch != 'All':
        df_new = df_new[df_data['lunch'] == f"{lunch}"]
    if preparation != 'All':
        df_new = df_new[df_data['test preparation course'] == f"{preparation}"]
    new_summary = df_new.describe().T[['min', 'mean', '75%', 'max']].astype(int)
    new_summary_df = pd.DataFrame(new_summary, index=summary_index)
    data_table.update(df_new)
    summary_table.update(new_summary_df)


heatmap = pn.Row(
    pn.Card(Heatmap(df_data), title='Feature Correlation'),
)

xs = np.linspace(0, np.pi)
freq = pn.widgets.FloatSlider(name='Frequency', start=0, end=10, value=2)
phase = pn.widgets.FloatSlider(name='Phase', start=0, end=np.pi)


@pn.depends(freq=freq, phase=phase)
def sine(freq, phase):
    return hv.Curve((xs, np.sin(xs * freq + phase))).opts(
        responsive=True, min_height=400)


@pn.depends(freq=freq, phase=phase)
def cosine(freq, phase):
    return hv.Curve((xs, np.cos(xs * freq + phase))).opts(
        responsive=True, min_height=400)


sin_cosine = pn.Row(
    pn.Card(hv.DynamicMap(sine), title='Sine'),
    pn.Card(hv.DynamicMap(cosine), title='Cosine')
)

panels = [
    data_table.widget,
    summary_table.widget,
    heatmap,
    sin_cosine
]
widgets = [
    freq,
    phase,
    race_select,
    gender_select,
    education_select,
    lunch_select,
    preparation_select
]

vanilla.sidebar.append(pn.Column(*widgets))
vanilla.main.append(pn.Column(*panels))
vanilla.servable()
