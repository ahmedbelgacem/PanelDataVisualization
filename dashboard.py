import panel as pn
from utils.dataset import read_csv, summarize
from components import PlotlyTable, Heatmap, Indicator, CountPlot, UMAPlot, BoxPlot

pn.extension(sizing_mode = 'stretch_width')
with open('templates/dashboard.jinja2', 'r') as html:
  template = pn.Template('\n'.join(html.readlines()))
template.add_variable('app_title', 'Dashboard')


dataset = read_csv('data/StudentsPerformance.csv')
summary = summarize(dataset)

table = PlotlyTable(dataset.reset_index(names = ''), title = 'Dataset Exploration', width = 1500, height = 600) # Resetting index to display it as a column
# summary_table = PlotlyTable(summary.reset_index(names = ''), title = 'Dataset Summary', width = 800, height = 400) # Resetting index to display it as a column
heatmap = Heatmap(dataset)
indicator = Indicator(dataset, width = 650, height = 400)
genderplot = CountPlot(dataset, height = 600, column = 'Gender', ticktext = ['Female', 'Male'], colors = ['#ef553b', '#636efa'], title = 'Gender Distribution')
umaplot = UMAPlot(dataset, title = 'UMAP Representation', width = 750)
boxplot = BoxPlot(dataset, title = 'Score Distribution Summary')
grouplot = CountPlot(dataset, height = 450, column = 'Race/Ethnicity', ticktext = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E'], title = 'Race/Ethnicity Distribution')

selectors_dict = {
  'Race/Ethnicity': ['All'] + list(sorted(dataset['Race/Ethnicity'].unique().tolist())),
  'Gender': ['All'] + dataset['Gender'].unique().tolist(),
  'Parental level education': ['All'] + dataset['Parental level education'].unique().tolist(),
  'Lunch': ['All'] + dataset['Lunch'].unique().tolist(),
  'Test prep. course': ['All'] + dataset['Test prep. course'].unique().tolist(),
}

selectors = [pn.widgets.Select(name = name, options = options) for name, options in selectors_dict.items()]
sliders = [
  pn.widgets.IntSlider(name = 'Number of neighbors', start = 1, end = 20, step = 1, value = 10, bar_color = '#316395', height = 50),
  pn.widgets.FloatSlider(name = 'Min. distance', start = .01, end = 1, step = 0.01, value = .1, bar_color = '#316395', height = 50)
]
spinner = pn.indicators.LoadingSpinner(value = True, width = 25, height = 25, bgcolor = 'light', color = 'success', visible = False)
button = pn.widgets.Button(name = 'Update', button_type = 'primary')

widgets = [
  *selectors,
  *sliders,
  button,
]

@pn.depends(*selectors, watch = True)
def filter(*selectors):
  subset = dataset.copy()
  subset = subset[subset['Race/Ethnicity'] == selectors[0]] if selectors[0] != 'All' else subset
  subset = subset[subset['Gender'] == selectors[1]] if selectors[1] != 'All' else subset
  subset = subset[subset['Parental level education'] == selectors[2]] if selectors[2] != 'All' else subset
  subset = subset[subset['Lunch'] == selectors[3]] if selectors[3] != 'All' else subset
  subset = subset[subset['Test prep. course'] == selectors[4]] if selectors[4] != 'All' else subset

  summary = summarize(subset)
  
  table.update(subset.reset_index(names = ''))
  # summary_table.update(summary.reset_index(names = ''))
  indicator.update(subset)
  boxplot.update(subset)
  
@pn.depends(button, watch = True)
def filter_umap(button):
  spinner.visible = True
  umaplot.update(dataset, sliders[0].value, sliders[1].value)
  spinner.visible = False

template.add_panel('sidebar', pn.Column(*widgets, css_classes = ''.split()))
template.add_panel('table', table.fig)
# template.add_panel('summary', summary_table.fig)
template.add_panel('indicator', indicator.fig)
template.add_panel('heatmap', heatmap.fig)
template.add_panel('genderplot', genderplot.fig)
template.add_panel('umap', umaplot.fig)
template.add_panel('spinner', spinner)
template.add_panel('summary', boxplot.fig)
template.add_panel('grouplot', grouplot.fig)
template.servable()
