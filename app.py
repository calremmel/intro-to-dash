# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

usa_last_five = pd.read_csv('data/processed/usa_last_five.csv')
summer_medals_counts = pd.read_csv('data/processed/summer_medals_counts.csv')

trace1 = go.Bar(x=usa_last_five.Year, y=usa_last_five.Gold, name='Gold', marker=dict(color='rgb(255,215,0)'))
trace2 = go.Bar(x=usa_last_five.Year, y=usa_last_five.Silver, name='Silver', marker=dict(color='rgb(192,192,192)'))
trace3 = go.Bar(x=usa_last_five.Year, y=usa_last_five.Bronze, name='Bronze', marker=dict(color='rgb(205,133,63)'))

teams = sorted(list(summer_medals_counts.Team.unique()))

options = [{'label': team, 'value': team} for team in teams]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Summer Olympic Medals by Country'),

    html.Div(children='''
        An example dashboard made using Dash.
    '''),

    dcc.Dropdown(
        id='country-dropdown',
        options=options,
        value="United States"
    ),

    dcc.Graph(
        id='medals-bar',
        figure={
            'data': [
                trace1,
                trace2,
                trace3
            ],
            'layout': go.Layout(
                barmode='stack', 
                title="Summer Olympic Medals - USA", 
                xaxis=dict(
                    type='category',
                    title=dict(text='Year')
                    ),
                yaxis=dict(
                    title=dict(text='Count')
                    )
            )
        }
    )
])

@app.callback(
    Output(component_id='medals-bar', component_property='figure'),
    [Input(component_id='country-dropdown', component_property='value')]
)
def fig_data(country):
    counts = summer_medals_counts[summer_medals_counts['Team'] == country].copy()
    
    trace1 = go.Bar(x=counts.Year, y=counts.Gold, name='Gold', marker=dict(color='rgb(255,215,0)'))
    trace2 = go.Bar(x=counts.Year, y=counts.Silver, name='Silver', marker=dict(color='rgb(192,192,192)'))
    trace3 = go.Bar(x=counts.Year, y=counts.Bronze, name='Bronze', marker=dict(color='rgb(205,133,63)'))

    data = [trace1, trace2, trace3]
    
    layout = go.Layout(
        barmode='stack', 
        title="Summer Olympic Medals - " + country, 
        xaxis=dict(
            type='category',
            title=dict(text='Year')
        ),
        yaxis=dict(
            title=dict(text='Count')
        )
    )
    
    figure = {'data': data, 'layout': layout}

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)