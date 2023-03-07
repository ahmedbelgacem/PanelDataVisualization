import seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from collections import defaultdict


def Heatmap(df: pd.DataFrame):
    d = defaultdict(preprocessing.LabelEncoder)
    df = df.apply(lambda x: d[x.name].fit_transform(x))
    fig = plt.Figure(figsize=(22, 10))
    ax = fig.add_subplot(111)
    corr = pd.DataFrame(df.corr())
    seaborn.heatmap(corr, ax=ax)
    return fig
