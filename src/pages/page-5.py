#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/page-5')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '25%', 'height': '15%', 'padding-left' : '5%'}),
    ######
    ######
    # Q15
    ######
    ######
    html.H1('Do you have a tick story?', style={'text-align' : 'center'}),
    html.Hr(className='grey_line'),
    html.P("In the last 12 months, how frequently did you find ticks in the following contexts \
           when living in your principal residence?? ", className='question_style2'),
    html.Br(),
    html.Div([
        html.Div([
            html.B('Attached to your skin)'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Daily', 'value': 'Daily'},
                    {'label': "Weekly", 'value': "Weekly"},
                    {'label': "Monthly", 'value': "Monthly"},
                    {'label': "Less than once a month", 'value': "Less than once a month"},
                    {'label': "Once or twicw a season", 'value': "Once or twicw a season"},
                    {'label': "Never", 'value': "Never"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
            html.Br(),
            html.B('Freely moving on your skin or clothing'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Daily', 'value': 'Daily'},
                    {'label': "Weekly", 'value': "Weekly"},
                    {'label': "Monthly", 'value': "Monthly"},
                    {'label': "Less than once a month", 'value': "Less than once a month"},
                    {'label': "Once or twicw a season", 'value': "Once or twicw a season"},
                    {'label': "Never", 'value': "Never"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
            html.Br(),
            html.B('On a pet'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Daily', 'value': 'Daily'},
                    {'label': "Weekly", 'value': "Weekly"},
                    {'label': "Monthly", 'value': "Monthly"},
                    {'label': "Less than once a month", 'value': "Less than once a month"},
                    {'label': "Once or twicw a season", 'value': "Once or twicw a season"},
                    {'label': "Never", 'value': "Never"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
            html.Br(),
            html.B('In the environment'),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Daily', 'value': 'Daily'},
                    {'label': "Weekly", 'value': "Weekly"},
                    {'label': "Monthly", 'value': "Monthly"},
                    {'label': "Less than once a month", 'value': "Less than once a month"},
                    {'label': "Once or twicw a season", 'value': "Once or twicw a season"},
                    {'label': "Never", 'value': "Never"},
                    {'label': "Not applicable", 'value': "Not applicable"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Br(),
    ]),
    ######
    ######
    html.Br(),
    ######
    ######
    # Q16
    ######
    ######
    html.Hr(className='grey_line'),
    html.P('When living in your principal residence, approximately how many ticks did you find in the following contexts last year, \
           between the months of April and November?', className='question_style2'),
    html.Div([
            html.B('Embedded in your skin'),
            html.Br(),
            html.Br(),
            dcc.Slider(0, 5,
            step=1,
            marks={
                0: "I don't remmber",
                1: 'Not applicable',
                2: '0',
                3: '1-25',
                4: '25-50',
                5: '51-75',
                6: '76-100 '
            },
            value=0,
            className='slider1'
            ),
            html.Br(),
            html.B('Freely moving on your skin or cloth'),
            html.Br(),
            html.Br(),
            dcc.Slider(0, 5,
            step=1,
            marks={
                0: "I don't remmber",
                1: 'Not applicable',
                2: '0',
                3: '1-25',
                4: '25-50',
                5: '51-75',
                6: '76-100 '
            },
            value=0,
            className='slider1'
            ),
            html.Br(),
            html.B('On a pet'),
            html.Br(),
            html.Br(),
            dcc.Slider(0, 5,
            step=1,
            marks={
                0: "I don't remmber",
                1: 'Not applicable',
                2: '0',
                3: '1-25',
                4: '25-50',
                5: '51-75',
                6: '76-100 '
            },
            value=0,
            className='slider1'
            ),
            html.Br(),
            html.B('In the environment (e.g., yard, house or park)'),
            html.Br(),
            html.Br(),
            dcc.Slider(0, 5,
            step=1,
            marks={
                0: "I don't remmber",
                1: 'Not applicable',
                2: '0',
                3: '1-25',
                4: '25-50',
                5: '51-75',
                6: '76-100 '
            },
            value=0,
            className='slider1')
    ], style={'font-size': '15px', 'marginLeft' : '30px', 'marginRight' : '30px'}),
    html.Br(),
    html.Br(),
    dcc.Link('Next page', href='/page-6'),
    html.Br(),
    html.Br(),
    dbc.Progress(value=63, style={"height": "15px"}, className="mb-3", label = "63% done"),
], style={'border': '4px solid black', 'padding': '20px', 'border-radius' : '15px'})


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



### dcc.slider pour ;a patie nombre de ticks