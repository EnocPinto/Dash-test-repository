# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:01:07 2023

@author: noco_
"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
from dash.dependencies import Input, Output, State

# Load the CSV data
data_url = "https://raw.githubusercontent.com/EnocPinto/Raw_data/main/Data.csv"
df = pd.read_csv(data_url, sep=';')

vars_TOAS = [var for var in df.columns if var.startswith('TOAS')]
vars_OPRE = [var for var in df.columns if var.startswith('OPRE')]
vars_EMPL = [var for var in df.columns if var.startswith('EMPL')]


app = dash.Dash(__name__)
server = app.server

sidebar = html.Div(
    [
        dbc.Row(
            [
                html.H5('Settings',
                        style={'margin-top': '12px', 'margin-left': '24px'})
            ],
            style={"height": "5vh"},
            className='bg-primary text-white font-italic'
        ),
        dbc.Row(
            [
                html.Div(
                    [
                        html.P(
                            'Categorical Variable',
                            style={'margin-top': '8px', 'margin-bottom': '4px'},
                            className='font-weight-bold'
                        ),
                        dcc.Dropdown(
                            id='my-cat-picker',
                            multi=False,
                            value='cat0',
                            options=[{'label': x, 'value': x} for x in vars_TOAS],
                            style={'width': '320px'}
                        ),
                        html.P(
                            'Continuous Variable',
                            style={'margin-top': '16px', 'margin-bottom': '4px'},
                            className='font-weight-bold'
                        ),
                        dcc.Dropdown(
                            id='my-cont-picker',
                            multi=False,
                            value='cont0',
                            options=[{'label': x, 'value': x} for x in vars_OPRE],
                            style={'width': '320px'}
                        ),
                        html.P(
                            'Continuous Variables for Correlation Matrix',
                            style={'margin-top': '16px', 'margin-bottom': '4px'},
                            className='font-weight-bold'
                        ),
                        dcc.Dropdown(
                            id='my-corr-picker',
                            multi=True,
                            options=[{'label': x, 'value': x} for x in vars_EMPL],
                            style={'width': '320px'}
                        ),
                        html.Button(
                            id='my-button',
                            n_clicks=0,
                            children='apply',
                            style={'margin-top': '16px'},
                            className='bg-dark text-white'
                        ),
                        html.Hr()
                    ]
                )
            ],
            style={'height': '50vh', 'margin': '8px'}
        ),
        dbc.Row(
            [
                html.P('Target Variables', className='font-weight-bold')
            ],
            style={"height": "45vh", 'margin': '8px'}
        )
    ]
)

content = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('Distribution based on Industry')
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        html.P('Distribution based on World region')
                                    ]
                                )
                            ],
                            style={"height": "50vh"}
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('Raw data')
                                    ]
                                )
                            ],
                            style={"height": "50vh"}
                        )
                    ],
                    label="TOAS",
                ),
                dbc.Tab(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('Distribution based on Industry')
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        html.P('Distribution based on World region')
                                    ]
                                )
                            ],
                            style={"height": "50vh"}
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('Raw data')
                                    ]
                                )
                            ],
                            style={"height": "50vh"}
                        )
                    ],
                    label="EMPL",
                ),
                dbc.Tab(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('Distribution based on Industry')
                                    ]
                                ),
                                dbc.Col(
                                    [
                                        html.P('Distribution based on World region')
                                    ]
                                )
                            ],
                            style={"height": "50vh"}
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P('Raw data')
                                    ]
                                )
                            ],
                            style={"height": "50vh"}
                        )
                    ],
                    label="OPRE",
                )
            ]
        )
    ]
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3, className='bg-light'),
                dbc.Col(content, width=9)
            ]
        )
    ],
    fluid=True
)


if __name__ == "__main__":
    app.run_server(debug=False, port=8050)
