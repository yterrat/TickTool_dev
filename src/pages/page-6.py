#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/page-6')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '40%', 'height': '40%'}, className='image-gallery'),
    html.Hr(className='orange_line'),
    html.Br(),
    ######
    ######
    # Q17
    ######
    ######
    html.H1('Secondary residence questions', style={'text-align' : 'center'}),
    html.Br(),
    html.Hr(className='grey_blue_line'),
    html.P("If you previously indicated that you have a secondary residence. \
           Are you willing to answer questions about tick exposure and preventive practices at your secondary residence?"
           , className='question_style2'),
    html.Br(),
    html.Div([
        dcc.RadioItems(
            options=[
                {'label': 'Yes', 'value': 'Yes'},
                {'label': "No", 'value': "No"}
            ],
            inputStyle={"margin-right": "10px"},
            value='No',
            id = 'Q777'
        )
    ], style={'font-size': '15px', 'marginLeft' : '30px', 'marginRight' : '30px'}),
    html.Hr(className='grey_blue_line'),
    # La suite va être affichée si Yes à cette réponse
    html.Div(
        id='garden',
        children=[
            ######
            ######
            # Q18
            ######
            ######
            html.P("Please answer the following questions about your secondary residence", className='question_style2'),
            html.Div([
                html.Div([
                    html.Label('Do you live in close proximity (within 500 feet or 150 meters) to a wooded area?)', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': "No", 'value': "No"}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value='',
                        id= 'Q1234'
                    ),
                    html.Br(),
                    html.Label('Do you have a courtyard, a garden, or a wooded area?', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': "No", 'value': "No"}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value='',
                        id= 'Q12345'
                    ),
                    html.Br(),
                    html.Label('Are you aware of, or do you suspect, the presence of deer or rodents on your property?', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': "No", 'value': "No"}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value='',
                        #id = 'QXXX'
                    ),
                    html.Br(),
                ], style={'font-size': '15px', 'marginLeft' : '30px', 'marginRight' : '30px'}),
            ]),
            html.Hr(className='grey_blue_line'),
            ######
            ######
            # Q19
            ######
            ######
            html.P('if you have a a courtyard, a garden, or a wooded area at your secondary residence, are there any of the following on your property?',
                className='question_style2'
            ),
            html.Div([
                html.Div([
                    html.Label('Herbaceous or forested areas/edges', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': "No", 'value': "No"},
                            {'label': "I don't know", 'value': "I don't know"}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('Children’s play equipment or activity structures', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': "No", 'value': "No"},
                            {'label': "I don't know", 'value': "I don't know"}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('Fenced in area(s) for recreational use', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': "No", 'value': "No"},
                            {'label': "I don't know", 'value': "I don't know"}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('A corridor/border of wood chips or gravel between the yard and surrounding woods and brush', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'Yes'},
                            {'label': "No", 'value': "No"},
                            {'label': "I don't know", 'value': "I don't know"}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
            ]),
            ######
            ######
            # Q20
            ######
            ######
            html.Hr(className='grey_blue_line'),
            html.P('How frequently do you implement the following practices on the property of your secondary residence?',
                className='question_style2'
            ),
            html.Div([
                html.Div([
                    html.Label('Regular lawn maintenance including mowing', style={'font-size' : '20px'}),
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
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('Removing fallen leaves ', style={'font-size' : '20px'}),
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
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('Clearing herbaceous brush and trimming branches', style={'font-size' : '20px'}),
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
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
            ]),
            ######
            ######
            # Q21
            ######
            ######
            html.Hr(className='grey_blue_line'),
            html.P('In the last 12 months, how frequently did you find ticks in the following contexts when living in your secondary residence?',
                className='question_style2'
            ),
            html.Div([
                html.Div([
                    html.Label('Attached to your skin', style={'font-size' : '20px'}),
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
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('Freely moving on your skin or clothing', style={'font-size' : '20px'}),
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
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('On a pet', style={'font-size' : '20px'}),
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
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('In the environment', style={'font-size' : '20px'}),
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
                        value=''
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'})
            ]),
            html.Hr(className='grey_blue_line'),
            html.P('When living in your secondary residence, approximately how many ticks did you find \
                    in the following contexts last year, between the months of April and November?', className='question_style2'),
            html.Div([
                    html.Label('Attached your skin', style={'font-size' : '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': "I don't remmber", 'value': "I don't remmber"},
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
                            {'label': "I don't remmber", 'value': "I don't remmber"},
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
                            {'label': "I don't remmber", 'value': "I don't remmber"},
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
                            {'label': "I don't remmber", 'value': "I don't remmber"},
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
                    ######
                    #replace by 1-4, 5-9, 10 or more categories, remove not applicable
                    ######
                ], style={'font-size': '15px', 'marginLeft' : '30px'}
            )
        ],
        style= {'display': 'block'}
    ),    
    html.Br(),
    html.Br(), 
    html.Label(id= 'data_display', children = ''),
    html.Br(),
    html.Br(),
    dcc.Link('Next page', href='/page-7'),
    html.Br(),
    html.Br(),
    dbc.Progress(value=77, style={"height": "15px"}, className="mb-3", label = "66% done")
])


@callback(
    Output(component_id='garden', component_property='hidden'),
    [Input(component_id='Q777', component_property='value')])

def show_hide_element(Q777):
    if Q777 == 'Yes':
        return False
    if Q777 == 'No':
        return True
    

@callback(
    Output('record_answers', 'data',  allow_duplicate=True),
    Input('Q777', 'value'),
    Input('Q1234', 'value'),
    Input('Q12345', 'value'),
    State('record_answers', 'data'),
    prevent_initial_call=True,
)
def update_dic(Q777,Q1234,Q12345,data):
    data = data or {}  # Ensure data is a dictionary
    data['Q777'] = Q777
    data['Q1234'] = Q1234
    data['Q12345'] = Q12345
    return data

# @callback(
#     Output('data_display', 'children'),
#     Input('record_answers', 'data')
# )
# def show_dic(data):
#     return str(data)


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