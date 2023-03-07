import panel as pn

def index():
  return pn.Column('root')

page = index()
page.servable()