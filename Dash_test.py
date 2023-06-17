# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:01:07 2023

@author: noco_
"""
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Load the CSV data
url = 'https://raw.githubusercontent.com/plotly/datasets/master/diabetes-vid.csv'
df = pd.read_csv(url)

# Create the scatter plot using Plotly Express
fig = px.scatter(df, x='BMI', y='BloodPressure', color='Age', title='Diabetes Dataset')

# Create the Dash app
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html.H1('Diabetes Dataset Scatter Plot'),
    
    dcc.Graph(id='scatter-plot', figure=fig),
    
    html.Div([
        html.Label('Filter by Outcome:'),
        dcc.Dropdown(
            id='outcome-filter',
            options=[{'label': i, 'value': i} for i in df['Outcome'].unique()],
            value=None,
            clearable=True
        )
    ]),
    
    dcc.Link(
        'Click here to view the dashboard',
        href='/dash',
        className='dashboard-link'
    )
])

# Define the callback to update the scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    Input('outcome-filter', 'value')
)
def update_scatter_plot(outcome):
    filtered_df = df if outcome is None else df[df['Outcome'] == outcome]
    updated_fig = px.scatter(filtered_df, x='BMI', y='BloodPressure', color='Age', title='Diabetes Dataset')
    return updated_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False, port=8051)