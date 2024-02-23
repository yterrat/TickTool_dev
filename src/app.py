#!/usr/bin/env python3

# Import packages
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.prevent_initial_callbacks='initial_duplicate'

app.suppress_callback_exceptions=True

app.layout = html.Div([
    dbc.Container(
    [dash.page_container],
    fluid=True
    ),
    dcc.Store(id='record_answers', data= {}, storage_type='memory')
])

if __name__ == "__main__":
    app.run_server(debug=True)