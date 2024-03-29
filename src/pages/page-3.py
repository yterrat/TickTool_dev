#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/page-3')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '40%', 'height': '40%'}, className='image-gallery'),
    html.Hr(className='orange_line'),
    html.Br(),
    html.H1('Are you outdoorsy ?', style={'text-align' : 'center'}),
    html.Br(),
    html.Br(),
    html.P("As part of your primary occupation (including work or studies), \
           on average how much time do you spend daily in wooded or grassy areas between the months of April and November? ", style={'font-size': '20px'}),
    html.Div([
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Less than one hour per day', 'value': 'Less than one hour per day'},
                    {'label': 'One hour to less than five hours per day', 'value': 'One hour to less than five hours per day'},
                    {'label': 'Five hours or more per day', 'value': 'Five hours or more per day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'Q21'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    html.Br(),
    #######
    #######
    html.Hr(className='grey_blue_line'),
    html.Br(),
    html.P("How often do you engage in the following outdoor activities between the months of April and November? ", style={'font-size': '20px'}),
    html.Div([
        html.Div([
            html.Label('Hiking or dog walking',  style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Once or twice a season', 'value': 'Once or twice a season'},
                    {'label': 'Less than once a month', 'value': 'Less than once a month'},
                    {'label': 'Every week', 'value': 'Every week'},
                    {'label': 'Every day', 'value': 'Every day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'Q21'
            )
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Camping',  style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Once or twice a season', 'value': 'Once or twice a season'},
                    {'label': 'Less than once a month', 'value': 'Less than once a month'},
                    {'label': 'Every week', 'value': 'Every week'},
                    {'label': 'Every day', 'value': 'Every day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'Q21'
            )
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Hunting',  style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Once or twice a season', 'value': 'Once or twice a season'},
                    {'label': 'Less than once a month', 'value': 'Less than once a month'},
                    {'label': 'Every week', 'value': 'Every week'},
                    {'label': 'Every day', 'value': 'Every day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'Q21'
            )
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Gardening/yard work on your property',  style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Once or twice a season', 'value': 'Once or twice a season'},
                    {'label': 'Less than once a month', 'value': 'Less than once a month'},
                    {'label': 'Every week', 'value': 'Every week'},
                    {'label': 'Every day', 'value': 'Every day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'Q21'
            )
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Recreational sports and outdoor activities',  style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Once or twice a season', 'value': 'Once or twice a season'},
                    {'label': 'Less than once a month', 'value': 'Less than once a month'},
                    {'label': 'Every week', 'value': 'Every week'},
                    {'label': 'Every day', 'value': 'Every day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'Q21'
            )
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Woodcutting',  style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Once or twice a season', 'value': 'Once or twice a season'},
                    {'label': 'Less than once a month', 'value': 'Less than once a month'},
                    {'label': 'Every week', 'value': 'Every week'},
                    {'label': 'Every day', 'value': 'Every day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'Q21'
            )
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Other outdoor activities',  style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': 'Once or twice a season', 'value': 'Once or twice a season'},
                    {'label': 'Less than once a month', 'value': 'Less than once a month'},
                    {'label': 'Every week', 'value': 'Every week'},
                    {'label': 'Every day', 'value': 'Every day'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'Q21'
            )
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
    ]),
    dcc.Link('Next page', href='/page-4', style={'font-size': '20px'}),
    html.Br(),
    html.Br(),
    dbc.Progress(value=33, style={"height": "15px"}, className="mb-3", label = "33% done"),
])


# @callback(
#     Output('record_answers', 'data',  allow_duplicate=True),
#     Input('Q21', 'value'),
#     Input('Q22', 'value'),
#     Input('Q23', 'value'),
#     Input('Q24', 'value'),
#     Input('Q25', 'value'),
#     Input('Q26', 'value'),
#     Input('Q27', 'value'),
#     State('record_answers', 'data'),
#     prevent_initial_call=True,
# )
# def update_dic(Q21,Q22,Q23,Q24,Q25,Q26,Q27,data):
#     data = data or {}  # Ensure data is a dictionary
#     data['Q21'] = Q21
#     data['Q22'] = Q22
#     data['Q23'] = Q23
#     data['Q24'] = Q24
#     data['Q25'] = Q25
#     data['Q26'] = Q26
#     data['Q27'] = Q27
#     return data
