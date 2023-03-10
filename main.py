import panel as pn
from utils.utils import read_csv, summarize
from components import PlotlyTable, Heatmap, Indicator

pn.extension(sizing_mode = 'stretch_width')
with open('templates/dashboard.jinja2', 'r') as html:
  template = pn.Template('\n'.join(html.readlines()))
template.add_variable('app_title', 'Dashboard')


dataset = read_csv('data/StudentsPerformance.csv')
summary = summarize(dataset)

table = PlotlyTable(dataset.reset_index(names = ''), title = 'Dataset Exploration', width = 1500, height = 600) # Resetting index to display it as a column
summary_table = PlotlyTable(summary.reset_index(names = ''), title = 'Dataset Summary', width = 800, height = 400) # Resetting index to display it as a column
heatmap = Heatmap(dataset)
indicator = Indicator(dataset, width = 650, height = 300)

selectors_dict = {
  'Race/Ethnicity': ['All'] + dataset['Race/Ethnicity'].unique().tolist(),
  'Gender': ['All'] + dataset['Gender'].unique().tolist(),
  'Parental level education': ['All'] + dataset['Parental level education'].unique().tolist(),
  'Lunch': ['All'] + dataset['Lunch'].unique().tolist(),
  'Test prep. course': ['All'] + dataset['Test prep. course'].unique().tolist(),
}
selectors = [pn.widgets.Select(name = name, options = options) for name, options in selectors_dict.items()]

# panels = [
#   pn.Row(table.fig),
#   pn.Row(summary_table.fig),
#   pn.Row(heatmap.fig)
# ]
widgets = [
  *selectors,
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
  summary_table.update(summary.reset_index(names = ''))
  indicator.update(subset)

template.add_panel('sidebar', pn.Column(*widgets, css_classes = ''.split()))
template.add_panel('table', table.fig)
template.add_panel('summary', summary_table.fig)
template.add_panel('indicator', indicator.fig)
template.add_panel('heatmap', heatmap.fig)
# template.add_panel('main', pn.Column(*panels, css_classes = '!bg-white'.split()))
template.servable()
