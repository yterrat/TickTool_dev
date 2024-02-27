#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/page-7')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '40%', 'height': '40%'}, className='image-gallery'),
    html.Hr(className='orange_line'),
    html.Br(),
    html.H1('Tell us about your self confidence',style={'text-align' : 'center'}),
    ######
    ######
    # Q23
    ######
    ######
    html.Br(),
    html.P("How confident are you that you can prevent a tick bite?", className='question_style2'),
    html.Div([
        dcc.RadioItems(
            options=[
                {'label': 'Not at all', 'value': 'Not at all'},
                {'label': "Slightly", 'value': "Slightly"},
                {'label': "Somewhat", 'value': "Somewath"},
                {'label': "Very", 'value': "Very"},
                {'label': "Extremely", 'value': "Extremely"}
            ],
            inputStyle={"margin-right": "10px"},
            value='',
            #id = 'QXXX'
        )
    ], style={'font-size': '15px',  'marginLeft' : '30px'}),
    html.Hr(className='grey_blue_line'),
    ######
    ######
    # Q24
    ######
    ######
    html.P("How confident are you that you could find a young tick (nymph, pictured) on your clothes or skin?",className='question_style2'),
    html.Img(src='/assets/tick1.jpg', style={'width': '100vw', 'height': 'auto'}),
    html.Br(),
    html.Div([
        dcc.RadioItems(
            options=[
                {'label': 'Not at all', 'value': 'Not at all'},
                {'label': "Slightly", 'value': "Slightly"},
                {'label': "Somewhat", 'value': "Somewath"},
                {'label': "Very", 'value': "Very"},
                {'label': "Extremely", 'value': "Extremely"}
            ],
            inputStyle={"margin-right": "10px"},
            value='',
            #id = 'QXXX'
        )
    ], style={'font-size': '15px',  'marginLeft' : '30px'}),
    html.Hr(className='grey_blue_line'),
    ######
    ######
    # Q25
    ######
    ######
    html.P("How confident are you that you could find a young tick (nymph, pictured) on your clothes or skin?"
           , className= 'question_style2'),
    html.Img(src='/assets/tick2.jpg', style={'width': '100vw', 'height': 'auto'}),
    html.Br(),
    html.Div([
        dcc.RadioItems(
            options=[
                {'label': 'Not at all', 'value': 'Not at all'},
                {'label': "Slightly", 'value': "Slightly"},
                {'label': "Somewhat", 'value': "Somewath"},
                {'label': "Very", 'value': "Very"},
                {'label': "Extremely", 'value': "Extremely"}
            ],
            inputStyle={"margin-right": "10px"},
            value='',
            #id = 'QXXX'
        )
    ], style={'font-size': '15px',  'marginLeft' : '30px'}),
    html.Hr(className='grey_blue_line'),
    ######
    ######
    # Q26
    ######
    ######
    html.P("How confident are you that you could safely and effectively remove a tick which had embedded into the skin?"
           , className= 'question_style2'),
    html.Div([
        dcc.RadioItems(
            options=[
                {'label': 'Not at all', 'value': 'Not at all'},
                {'label': "Slightly", 'value': "Slightly"},
                {'label': "Somewhat", 'value': "Somewath"},
                {'label': "Very", 'value': "Very"},
                {'label': "Extremely", 'value': "Extremely"}
            ],
            inputStyle={"margin-right": "10px"},
            value='',
            #id = 'QXXX'
        )
    ], style={'font-size': '15px',  'marginLeft' : '30px'}),
    html.Br(),
    dcc.Link('Next page', href='/page-8', style={'font-size': '20px'}),
    html.Br(),
    html.Br(),
    dbc.Progress(value=90, style={"height": "15px"}, className="mb-3", label = "90% done"),
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

# ######
#     ######
#     # Q19
#     ######
#     ######
#     html.P('if you have a a courtyard, a garden, or a wooded area at your secondary residence, are there any of the following on your property?',
#         className='question_style2'
#     ),
#     html.Div([
#         html.Div([
#             html.B('Herbaceous or forested areas/edges'),
#             html.Br(),
#             html.Br(),
#             dcc.RadioItems(
#                 options=[
#                     {'label': 'Yes', 'value': 'Yes'},
#                     {'label': "No", 'value': "No"},
#                     {'label': "I don't know", 'value': "I don't know"}
#                 ],
#                 inputStyle={"margin-right": "10px"},
#                 value=''
#             ),
#         ], style={'font-size': '15px', 'marginLeft' : '30px'}),
#         html.Br(),
#     ]),