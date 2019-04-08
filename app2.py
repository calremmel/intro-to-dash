# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

usa_last_five = pd.read_csv('data/processed/usa_last_five.csv')

trace1 = go.Bar(x=usa_last_five.Year, y=usa_last_five.Gold, name='Gold', marker=dict(color='rgb(255,215,0)'))
trace2 = go.Bar(x=usa_last_five.Year, y=usa_last_five.Silver, name='Silver', marker=dict(color='rgb(192,192,192)'))
trace3 = go.Bar(x=usa_last_five.Year, y=usa_last_five.Bronze, name='Bronze', marker=dict(color='rgb(205,133,63)'))

data = [trace1, trace2, trace3]

layout = go.Layout(
    barmode='stack',
    title="Summer Olympic Medals - USA",
    xaxis=dict(
        type='category'
    )
)


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Chris is the Best'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': data,
            'layout': layout
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)