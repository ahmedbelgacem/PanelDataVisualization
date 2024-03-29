import panel as pn
from utils.dataset import read_csv
from components import ClusterPlot, Regression

pn.extension(sizing_mode = 'stretch_width')
with open('templates/ai.jinja2', 'r') as html:
  template = pn.Template('\n'.join(html.readlines()))
template.add_variable('app_title', 'Machine Learning')

dataset = read_csv('data/StudentsPerformance.csv')

clusterplot = ClusterPlot(dataset, title = 'KMeans Clustering')
regression = Regression(dataset)
sliders = [
  pn.widgets.IntSlider(name = 'Number of neighbors', start = 1, end = 20, step = 1, value = 10, bar_color = '#316395', height = 50),
  pn.widgets.FloatSlider(name = 'Min. distance', start = .01, end = 1, step = 0.01, value = .1, bar_color = '#316395', height = 50),
  pn.widgets.IntSlider(name = 'Number of clusters', start = 1, end = 10, step = 1, value = 2, bar_color = '#316395', height = 50),
]
spinner = pn.indicators.LoadingSpinner(value = True, width = 25, height = 25, bgcolor = 'light', color = 'success', visible = False)
button = pn.widgets.Button(name = 'Update', button_type = 'primary')
regression_sliders = [
  pn.widgets.Select(name = 'Gender', options = dataset['Gender'].unique().tolist()),
  pn.widgets.Select(name = 'Lunch', options = dataset['Lunch'].unique().tolist()),
  pn.widgets.Select(name = 'Test prep. course', options = dataset['Test prep. course'].unique().tolist()),
  pn.widgets.Select(name = 'Race/Ethnicity', options = dataset['Race/Ethnicity'].unique().tolist()),
  pn.widgets.Select(name = 'Parental level education', options = dataset['Parental level education'].unique().tolist()),
]
predict_scores= pn.widgets.Button(name = 'Predict', button_type = 'primary')
widgets = [
  *sliders,
  button,
  *regression_sliders,
  predict_scores,
]

@pn.depends(button, watch = True)
def filter_umap(button):
  spinner.visible = True
  clusterplot.update(dataset, n_neighbors = sliders[0].value, min_dist = sliders[1].value, n_clusters = sliders[2].value)
  spinner.visible = False

@pn.depends(predict_scores, watch = True)
def predict(predict_scores):
  spinner.visible = True
  regression.update(gender = regression_sliders[0].value, lunch = regression_sliders[1].value, test_prep = regression_sliders[2].value, race = regression_sliders[3].value, parental_education = regression_sliders[4].value)
  spinner.visible = False

template.add_panel('sidebar', pn.Column(*widgets))
template.add_panel('clusterplot', clusterplot.fig)
template.add_panel('regression', regression.fig)
template.add_panel('spinner', spinner)

template.servable()