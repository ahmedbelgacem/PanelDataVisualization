import panel as pn
from utils.utils import read_csv

pn.extension(sizing_mode = 'stretch_width')
with open('templates/ai.jinja2', 'r') as html:
  template = pn.Template('\n'.join(html.readlines()))
template.add_variable('app_title', 'Machine Learning')

template.servable()