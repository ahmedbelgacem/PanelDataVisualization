import panel as pn
from panel.widgets import Tabulator
import pandas as pd


def Table(data: pd.DataFrame, index: list = None):
    if index is not None:
        data = data.set_index(pd.Index(index))
    return Tabulator(data, layout='fit_data_stretch', page_size=10)
