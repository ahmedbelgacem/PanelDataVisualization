import pandas as pd


def data_preprocessing(path):
    df = pd.read_csv(path)
    df['total score (%)'] = round(
        (df['math score'] + df['reading score'] + df['writing score']) / 3, 1)
    return df


def summary(df: pd.DataFrame, index: list):
    summary_df = df.describe().T[['min', 'mean', '75%', 'max']].astype(int)
    return pd.DataFrame(summary_df, index=index)


def filter_data(df: pd.DataFrame, feature, value):
    return df[df[feature] == value]