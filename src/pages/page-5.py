#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/page-5')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '40%', 'height': '40%'}, className='image-gallery'),
    html.Hr(className='orange_line'),
    html.Br(),
    ######
    ######
    # Q15
    ######
    ######
    html.H1('Do you have a tick story?', style={'text-align' : 'center'}),
    html.Br(),
    html.Br(),
    html.P("In the last 12 months, how frequently did you find ticks in the following contexts \
           when living in your principal residence? ", className='question_style2'),
    html.Br(),
    html.Div([
        html.Div([
            html.Label('Attached to your skin', style={'font-size' : '20px'}),
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
            html.Label('Freely moving on your skin or clothing', style={'font-size' : '20px'}),
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
            html.Label('On a pet', style={'font-size' : '20px'}),
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
            html.Label('In the environment', style={'font-size' : '20px'}),
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
        ], style={'font-size': '15px', 'marginLeft' : '30px'})
    ]),
    ######
    ######
    ######
    ######
    # Q16
    ######
    ######
    html.Hr(className='grey_blue_line'),
    html.P('When living in your principal residence, approximately how many ticks did you find in the following contexts last year, \
           between the months of April and November?', className='question_style2'),
    html.Div([
            html.Label('Embedded in your skin', style={'font-size' : '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': "I don't remember", 'value': "I don't remmber"},
                    {'label': "0", 'value': "0"},
                    {'label': "1-25", 'value': "1-25"},
                    {'label': "26-50", 'value': "26-50"},
                    {'label': "51-75", 'value': "51-75"},
                    {'label': "76-100", 'value': "76-100"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
            html.Br(),
            html.Label('Freely moving on your skin or cloth', style={'font-size' : '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': "I don't remember", 'value': "I don't remmber"},
                    {'label': "0", 'value': "0"},
                    {'label': "1-25", 'value': "1-25"},
                    {'label': "26-50", 'value': "26-50"},
                    {'label': "51-75", 'value': "51-75"},
                    {'label': "76-100", 'value': "76-100"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
            html.Br(),
            html.Label('On a pet', style={'font-size' : '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': "I don't remember", 'value': "I don't remmber"},
                    {'label': "0", 'value': "0"},
                    {'label': "1-25", 'value': "1-25"},
                    {'label': "26-50", 'value': "26-50"},
                    {'label': "51-75", 'value': "51-75"},
                    {'label': "76-100", 'value': "76-100"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
            html.Br(),
            html.Label('In the environment (e.g., yard, house or park)', style={'font-size' : '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': "I don't remember", 'value': "I don't remmber"},
                    {'label': "0", 'value': "0"},
                    {'label': "1-25", 'value': "1-25"},
                    {'label': "26-50", 'value': "26-50"},
                    {'label': "51-75", 'value': "51-75"},
                    {'label': "76-100", 'value': "76-100"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
    ], style={'font-size': '15px', 'marginLeft' : '30px', 'marginRight' : '30px'}),
    html.Br(),
    dcc.Link('Next page', href='/page-6', style={'font-size': '20px'}),
    html.Br(),
    html.Br(),
    dbc.Progress(value=63, style={"height": "15px"}, className="mb-3", label = "63% done"),
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



### dcc.slider pour ;a patie nombre de ticks