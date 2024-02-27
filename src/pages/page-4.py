#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/page-4')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '25%', 'height': '15%', 'padding-left' : '5%'}),
    html.H1('How are you protecting yourself ?', style={'text-align' : 'center'}),
    html.Br(),
    # Q12
    html.P("In the last 12 months, have you visited or lived in an area where you knew or suspected you could contract Lyme disease, \
           or another disease spread by ticks? ", style={'font-size': '20px'}),
    html.Div([
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'Yes'},
                    {'label': 'No', 'value': 'No'},
                    {'label': "I don't know", 'value': "I don't know"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'Q28'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    html.Hr(style={'borderWidth': "0.3vh", "width": "100%", "color": "grey"}),
    html.Br(),
    # Q13
    html.P("If you answered yes to the previous question, \
           when visiting or living in these areas, did you look into ways to prevent tick exposure and infection with a tick-borne disease? ", style={'font-size': '20px'}),
    html.Div([
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'Yes'},
                    {'label': 'No', 'value': 'No'},
                    {'label': "I don't remember", 'value': "I don't remember"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'Q29'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    html.Hr(style={'borderWidth': "0.3vh", "width": "100%", "color": "grey"}),
    html.Br(),
    #######
    #######
    # Q14
    html.P("When visiting or living in these areas, how frequently did you adopt the following measures to protect yourself against tick bites and Lyme disease? ", className='question_style2'),
    html.Div([
        html.Div([
            html.B('Wearing long layers of clothing (e.g., pants, long sleeves)'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Tucking in clothes when practicing outdoor activities)'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Applying bug repellent containing DEET or icaridin (also known as picaridin) when outdoors )'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Walking on cleared paths and trails and avoiding tall grass during outdoor activities'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Wearing light-coloured clothing to make it easier to check for ticks during outdoor activities'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Bathing or showering after spending time outdoors'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Examining your body for ticks and removing them immediately after being outdoors'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Examining clothes and items to avoid bringing ticks into home after being outdoors'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.B('Putting clothes in the dryer for 10 minutes to kill any ticks that may be there after being outdoors'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Never', 'value': 'Never'},
                    {'label': "Rarely", 'value': "Rarely"},
                    {'label': "Sometimes", 'value': "Sometimes"},
                    {'label': "Most of the time", 'value': "Most of the time"},
                    {'label': "Always", 'value': "Always"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'QXXXXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    ]),
    ######
    ######
    html.Br(),
    dcc.Link('Next page', href='/page-5'),
    html.Br(),
    html.Br(),
    dbc.Progress(value=50, style={"height": "15px"}, className="mb-3", label = "50% done"),
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
