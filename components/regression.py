import plotly.graph_objects as go
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression


class Regression():
    def __init__(self, df: pd.DataFrame, **kwargs) -> None:
        df_enc = df.copy()
        self.le_gender = LabelEncoder().fit(df_enc['Gender'])
        self.le_lunch = LabelEncoder().fit(df_enc['Lunch'])
        self.le_test_prep = LabelEncoder().fit(df_enc['Test prep. course'])
        df_enc['Gender'] = self.le_gender.transform(df_enc['Gender'])
        df_enc['Lunch'] = self.le_lunch.transform(df_enc['Lunch'])
        df_enc['Test prep. course'] = self.le_test_prep.transform(df_enc['Test prep. course'])
        df_enc = pd.get_dummies(df_enc, columns=['Race/Ethnicity', 'Parental level education'])
        self.X = df_enc.loc[:, ~df_enc.columns.isin(['Math score (%)', 'Reading score (%)', 'Writing score (%)', 'Total score (%)'])]
        self.math = LinearRegression().fit(self.X, df_enc['Math score (%)'])
        self.reading = LinearRegression().fit(self.X, df_enc['Reading score (%)'])
        self.writing = LinearRegression().fit(self.X, df_enc['Writing score (%)'])

        values = [self.math.predict(np.array([[0, 0,0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]))[0], self.reading.predict(np.array([[0, 0,0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]))[0],
                  self.writing.predict(np.array([[0, 0,0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]))[0]]
        self.fig = go.Figure()
        self.fig.add_trace(
            go.Indicator(
                name='Math score',
                mode='number',
                value=values[0],
                domain={'row': 0, 'column': 0},
                title={'text': 'Math Score', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
                number={'font_color': 'black', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
            )

        )
        self.fig.add_trace(
            go.Indicator(
                name='Reading Score',
                mode='number',
                value=values[1],
                domain={'row': 0, 'column': 2},
                title={'text': 'Reading Score', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
                number={'font_color': 'black', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
            )

        )
        self.fig.add_trace(
            go.Indicator(
                name='Writing Score',
                mode='number',
                value=values[2],
                domain={'row': 1, 'column': 3},
                title={'text': 'Writing Score', 'font_family': 'montserrat', 'font_color': 'black', 'font_size': 20},
                number={'font_color': 'black', 'font_size': 60, 'suffix': '%', 'font_family': 'montserrat'},
            )

        )
        self.fig.update_layout(
            **kwargs,
            title='Linear Regression',
            font_family='montserrat',
            title_font={'size': 20},
            grid={'rows': 2, 'columns': 3, 'pattern': 'independent'},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )

    def update(self, gender, lunch, test_prep, race, parental_education):
        X_new = pd.get_dummies(pd.DataFrame({'Gender':[self.le_gender.transform([gender])[0]],'Lunch':[self.le_lunch.transform([lunch])[0]],'Test prep. course':[self.le_test_prep.transform([test_prep])[0]],'Race/Ethnicity':[race],'Parental level education':[parental_education]}))
        X_new = X_new.reindex(columns=self.X.columns, fill_value=0)
        values = [self.math.predict(X_new)[0], self.reading.predict(X_new)[0], self.writing.predict(X_new)[0]]
        self.fig.update_traces(value=values[0], selector=dict(name='Math score'))
        self.fig.update_traces(value=values[1], selector=dict(name='Reading Score'))
        self.fig.update_traces(value=values[2], selector=dict(name='Writing Score'))
