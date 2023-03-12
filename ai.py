import panel as pn
from utils.dataset import read_csv
from components import ClusterPlot

pn.extension(sizing_mode = 'stretch_width')
with open('templates/ai.jinja2', 'r') as html:
  template = pn.Template('\n'.join(html.readlines()))
template.add_variable('app_title', 'Machine Learning')

dataset = read_csv('data/StudentsPerformance.csv')

clusterplot = ClusterPlot(dataset, title = 'KMeans Clustering')

sliders = [
  pn.widgets.IntSlider(name = 'Number of neighbors', start = 1, end = 20, step = 1, value = 10, bar_color = '#316395', height = 50),
  pn.widgets.FloatSlider(name = 'Min. distance', start = .01, end = 1, step = 0.01, value = .1, bar_color = '#316395', height = 50),
  pn.widgets.IntSlider(name = 'Number of clusters', start = 1, end = 10, step = 1, value = 2, bar_color = '#316395', height = 50),
]
spinner = pn.indicators.LoadingSpinner(value = True, width = 25, height = 25, bgcolor = 'light', color = 'success', visible = False)
button = pn.widgets.Button(name = 'Update', button_type = 'primary')

widgets = [
  *sliders,
  button,
]

@pn.depends(button, watch = True)
def filter_umap(button):
  spinner.visible = True
  clusterplot.update(dataset, n_neighbors = sliders[0].value, min_dist = sliders[1].value, n_clusters = sliders[2].value)
  spinner.visible = False

template.add_panel('sidebar', pn.Column(*widgets))
template.add_panel('clusterplot', clusterplot.fig)
template.add_panel('spinner', spinner)

template.servable()