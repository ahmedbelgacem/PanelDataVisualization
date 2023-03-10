import pandas as pd


def read_csv(path):
    df = pd.read_csv(path)
    df['total score (%)'] = df.iloc[:, -3:].mean(axis = 1).round(1)
    columns = ['Gender', 'Race/Ethnicity', 'Parental level education', 'Lunch', 'Test prep. course', 'Math score (%)', 'Reading score (%)', 'Writing score (%)', 'Total score (%)']
    df = df.rename(columns = {df.columns[i]: columns[i] for i in range(len(df.columns))})
    return df


def summarize(df: pd.DataFrame):
    summary = df.describe().T[['min', 'mean', '75%', 'max']].astype(int)
    index = ['Math score', 'Reading score', 'Writing score', 'Total score (%)']
    columns = ['Min.', 'Mean', '75%', 'Max.']
    summary = summary.rename(columns = {summary.columns[i]: columns[i] for i in range(len(summary.columns))})
    summary = summary.set_index(pd.Index(index))
    return pd.DataFrame(summary)


def filter_data(df: pd.DataFrame, feature, value):
    return df[df[feature] == value]