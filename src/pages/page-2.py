#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/page-2')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '40%', 'height': '40%'}, className='image-gallery'),
    html.Hr(className='orange_line'),
    html.Br(),
    html.H1('Tell us more about your house', style={'textAlign' : 'center'}),
    html.Br(),
    html.Br(),
    #Question 1
    html.P("Where is your primary residence? ", style={'font-size': '20px'}),
    dcc.Dropdown(
        options=[
            {'label': 'Alberta', 'value': 'Alberta'},
            {'label': 'British Columbia', 'value': 'British Columbia'},
            {'label': 'New Brunswick', 'value': 'New Brunswick'},
            {'label': 'Newfoundland and Labrador', 'value': 'Newfoundland and Labrador'},
            {'label': 'Northwest Territories', 'value': 'Northwest Territories'},
            {'label': 'Nova Scotia', 'value': 'Nova Scotia'},
            {'label': 'Nunavut', 'value': 'Nunavut'},
            {'label': 'Ontario', 'value': 'Ontario'},
            {'label': 'Prince Edward Island', 'value': 'Prince Edward Island'},
            {'label': 'Quebec', 'value': 'Quebec'},
            {'label': 'Saskatchewan', 'value': 'Saskatchewan'},
            {'label': 'Yukon', 'value': 'Yukon'}
        ],
        placeholder='Select province',
        id = 'Q1'
    ),
    html.Br(),
    html.P("If applicable, where is your secondary residence (for example, cottage)? ", style={'font-size': '20px'}),
    dcc.Dropdown(
        options=[
            {'label': 'Not applicable to my situation' , 'value': 'Not applicable to my situation'},
            {'label': 'I prefer not to say ', 'value': 'I prefer not to say '},
            {'label': 'Alberta', 'value': 'Alberta'},
            {'label': 'British Columbia', 'value': 'British Columbia'},
            {'label': 'New Brunswick', 'value': 'New Brunswick'},
            {'label': 'Newfoundland and Labrador', 'value': 'Newfoundland and Labrador'},
            {'label': 'Northwest Territories', 'value': 'Northwest Territories'},
            {'label': 'Nova Scotia', 'value': 'Nova Scotia'},
            {'label': 'Nunavut', 'value': 'Nunavut'},
            {'label': 'Ontario', 'value': 'Ontario'},
            {'label': 'Prince Edward Island', 'value': 'Prince Edward Island'},
            {'label': 'Quebec', 'value': 'Quebec'},
            {'label': 'Saskatchewan', 'value': 'Saskatchewan'},
            {'label': 'Yukon', 'value': 'Yukon'},
        ],
        placeholder='Select province',
        id = 'Q2'
    ),
    html.Hr(className='grey_blue_line'),
    html.P('Please indicate whether the following statements are true for your household, most of the time.', style={'font-size': '20px'}),
    html.Div([
        html.Div([
            html.Label('I live alone', style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'},
                    {'label': 'I prefer not to say', 'value': 'prefer_not_to_say'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'Q3'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('I live with at least one person over 18 years of age', style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'},
                    {'label': 'I prefer not to say', 'value': 'prefer_not_to_say'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'Q4'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('I live with at least one child between the ages of 0 and 4 years', style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'},
                    {'label': 'I prefer not to say', 'value': 'prefer_not_to_say'}
                ],
                value='',
                inputStyle={"margin-right": "10px"},
                id = 'Q5'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'})
    ]),
    html.Hr(className='grey_blue_line'),
    html.P('Do you have, or regularly take care of, at least one of the following animals?', style={'font-size': '20px'}),
    html.Div(
        dcc.Checklist(
            options=[
                {'label': 'Dogs', 'value': 'Dogs'},
                {'label': 'Cats which go outdoors at least some of the time', 'value': 'Outdoor_cats'},
                {'label': 'Horses', 'value': 'Horses'}
            ],
            inputStyle={"margin-right": "10px"},
            value=[],
            id = 'Q6'
        ),style={'font-size': '15px', 'marginLeft' : '30px'}
    ),
    #######
    html.Div(
        id='dogs',
        children=[
            html.Hr(className='grey_blue_line'),
            html.P("Have you used either of the following for your dog(s) in the last 12 months?",
                style={'font-size': '20px'}
                ),
            html.Div([
                html.Div([
                    html.Label('Anti-tick products, as recommended by your veterinarian', style={'font-size': '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'yes'},
                            {'label': 'No', 'value': 'no'},
                            {'label': "I don't know", 'value': "I don't know"},
                            {'label': 'I prefer not to say', 'value': 'prefer_not_to_say'}
                        ],
                        inputStyle={"margin-right": "10px"},
                        value='',
                        id = 'Q7'
                    ),
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Br(),
                html.Div([
                    html.Label('Lyme disease vaccine', style={'font-size': '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Yes', 'value': 'yes'},
                            {'label': 'No', 'value': 'no'},
                            {'label': "I don't know", 'value': "I don't know"},
                            {'label': 'I prefer not to say', 'value': 'prefer_not_to_say'}
                        ],
                        value='',
                        inputStyle={"margin-right": "10px"},
                        id = 'Q8'
                    ),
                ], 
                style={'font-size': '15px', 'marginLeft' : '30px'})
            ]),
        ], style={'display' : 'block'}
    ),
    ######
    html.Div(
        id='cats',
        children=[
        html.Hr(className='grey_blue_line'),
        html.P("Have you used anti-tick products, as recommended by your veterinarian, for your cat(s) in the last 12 months? ",
            style={'font-size': '20px'}
            ),
        dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'},
                    {'label': "I don't know", 'value': "I don't know"},
                    {'label': 'I prefer not to say', 'value': 'prefer_not_to_say'}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                style={'font-size': '15px', 'marginLeft' : '30px'},
                id = 'Q9'
            ), 
        ], style={'display':'block'}
    ),
    #######
    #######
    html.Hr(className='grey_blue_line'),
    html.P("Please answer the following questions about your principal residence:", style={'font-size': '20px'}),
    html.Div([
        html.Div([
            html.Label('Do you live in close proximity (within 500 feet or 150 meters) to a wooded area?', style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'},
                    {'label': "I don't know", 'value': "I don't know"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'Q10'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Do you have a courtyard, a garden, or a wooded area?', style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'},
                    {'label': "I don't know", 'value': "I don't know"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                id = 'Q11'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
        html.Br(),
        html.Div([
            html.Label('Are you aware of, or do you suspect, the presence of deer or rodents on your property?', style={'font-size': '20px'}),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                options=[
                    {'label': 'Yes', 'value': 'yes'},
                    {'label': 'No', 'value': 'no'},
                    {'label': "I don't know", 'value': "I don't know"}
                ],
                value='',
                inputStyle={"margin-right": "10px"},
                id = 'Q12'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    ]),
    html.Hr(className='grey_blue_line'),
    ######
    ######
    html.Div(
        id='courtyard',
        children=[
            html.P("Are there any of the following on your principal residencey", style={'font-size': '20px'}),
            html.Div([
                html.Label('Herbaceous or forested areas/edges', style={'font-size': '20px'}),
                html.Br(),
                html.Br(),
                dcc.RadioItems(
                    options=[
                        {'label': 'Yes', 'value': 'yes'},
                        {'label': 'No', 'value': 'no'},
                        {'label': "I don't know", 'value': "I don't know"}
                    ],
                    inputStyle={"margin-right": "10px"},
                    value='',
                    id = 'Q13'
                ),
            ], style={'font-size': '15px', 'marginLeft' : '30px'}),
            html.Br(),
            html.Div([
                html.Label('Children’s play equipment or activity structures?', style={'font-size': '20px'}),
                html.Br(),
                html.Br(),
                dcc.RadioItems(
                    options=[
                        {'label': 'Yes', 'value': 'yes'},
                        {'label': 'No', 'value': 'no'},
                        {'label': "I don't know", 'value': "I don't know"}
                    ],
                    inputStyle={"margin-right": "10px"},
                    value='',
                    id = 'Q14'
                ),
            ], style={'font-size': '15px', 'marginLeft' : '30px'}),
            html.Br(),
            html.Div([
                html.Label('Fenced in area(s) for recreational use?', style={'font-size': '20px'}),
                html.Br(),
                html.Br(),
                dcc.RadioItems(
                    options=[
                        {'label': 'Yes', 'value': 'yes'},
                        {'label': 'No', 'value': 'no'},
                        {'label': "I don't know", 'value': "I don't know"}
                    ],
                    value='',
                    inputStyle={"margin-right": "10px"},
                    id = 'Q15'
                ),
            ], style={'font-size': '15px', 'marginLeft' : '30px'}),
            html.Br(),
            html.Div([
                html.Label('Barriers to exclude deer on your property?', style={'font-size': '20px'}),
                html.Br(),
                html.Br(),
                dcc.RadioItems(
                    options=[
                        {'label': 'Yes', 'value': 'yes'},
                        {'label': 'No', 'value': 'no'},
                        {'label': "I don't know", 'value': "I don't know"}
                    ],
                    value='',
                    inputStyle={"margin-right": "10px"},
                    id = 'Q16'
                ),
            ], style={'font-size': '15px', 'marginLeft' : '30px'}),
            html.Br(),
            html.Div([
                html.Label('A corridor/border of wood chips or gravel between the yard and surrounding woods and brush?', style={'font-size': '20px'}),
                html.Br(),
                html.Br(),
                dcc.RadioItems(
                    options=[
                        {'label': 'Yes', 'value': 'yes'},
                        {'label': 'No', 'value': 'no'},
                        {'label': "I don't know", 'value': "I don't know"}
                    ],
                    value='',
                    inputStyle={"margin-right": "10px"},
                    id = 'Q17'
                ),
            ], style={'font-size': '15px', 'marginLeft' : '30px'}),  
            ######
            ######
            html.Hr(className='grey_blue_line'),
            #######
            html.P("How frequently do you implement the following practices on the property of your principal residence?", style={'font-size': '20px'}),
            html.Div([
                html.Div([
                    html.Label('Regular lawn maintenance including mowing', style={'font-size': '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Never', 'value': 'Never'},
                            {'label': 'rarely', 'value': 'Rarely'},
                            {'label': "Sometimes", 'value': "Sometimes"},
                            {'label': 'Most of the time', 'value': 'Most of the time'},
                            {'label': "Always", 'value': "Always"}
                        ],
                        value='',
                        inputStyle={"margin-right": "10px"},
                        id = 'Q17'
                    ),
                    html.Br()
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Div([
                    html.Label('Removing fallen leaves', style={'font-size': '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Never', 'value': 'Never'},
                            {'label': 'rarely', 'value': 'Rarely'},
                            {'label': "Sometimes", 'value': "Sometimes"},
                            {'label': 'Most of the time', 'value': 'Most of the time'},
                            {'label': "Always", 'value': "Always"}
                        ],
                        value='',
                        inputStyle={"margin-right": "10px"},
                        id = 'Q18'
                    ),
                    html.Br()
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
                html.Div([
                    html.Label('Clearing herbaceous brush and trimming branches', style={'font-size': '20px'}),
                    html.Br(),
                    html.Br(),
                    dcc.RadioItems(
                        options=[
                            {'label': 'Never', 'value': 'Never'},
                            {'label': 'rarely', 'value': 'Rarely'},
                            {'label': "Sometimes", 'value': "Sometimes"},
                            {'label': 'Most of the time', 'value': 'Most of the time'},
                            {'label': "Always", 'value': "Always"}
                        ],
                        value='',
                        inputStyle={"margin-right": "10px"},
                        id = 'Q19'
                    ),
                    html.Br()
                ], style={'font-size': '15px', 'marginLeft' : '30px'}),
            ]),
        ], style={'display':'block'}
    ),
    #######
    #######
    dcc.Link('Next page', href='/page-3', style={'font-size': '20px'}),
    html.Br(),
    html.Br(),
    dbc.Progress(value=17, style={"height": "15px"}, className="mb-3", label = "17% done"),
])


@callback(
    Output(component_id='dogs', component_property='hidden'),
    [Input(component_id='Q6', component_property='value')])

def show_hide_element(Q6):
    if 'Dogs' in Q6:
        return False
    else:
        return True
    
@callback(
    Output(component_id='cats', component_property='hidden'),
    [Input(component_id='Q6', component_property='value')])

def show_hide_element(Q6):
    if 'Outdoor_cats' in Q6:
        return False
    else:
        return True

@callback(
    Output(component_id='courtyard', component_property='hidden'),
    [Input(component_id='Q11', component_property='value')])

def show_hide_element(Q11):
    if Q11 == 'yes':
        return False
    else:
        return True

# myquestions = []
# for i in range(1,21):
#     quest = 'Q' + str(i)
#     myquestions.append(quest)

# @callback(
#     Output('record_answers', 'data',  allow_duplicate=True),
#     Input('Q1', 'value'),
#     Input('Q2', 'value'),
#     Input('Q3', 'value'),
#     Input('Q4', 'value'),
#     Input('Q5', 'value'),
#     Input('Q6', 'value'),
#     Input('Q7', 'value'),
#     Input('Q8', 'value'),
#     Input('Q9', 'value'),
#     Input('Q10', 'value'),
#     Input('Q11', 'value'),
#     Input('Q12', 'value'),
#     Input('Q13', 'value'),
#     Input('Q14', 'value'),
#     Input('Q15', 'value'),
#     Input('Q16', 'value'),
#     Input('Q17', 'value'),
#     Input('Q18', 'value'),
#     Input('Q19', 'value'),
#     Input('Q20', 'value'),
#     State('record_answers', 'data'),
#     prevent_initial_call=True,
# )
# def update_dic(Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16,Q17,Q18,Q19,Q20,data):
#     data = data or {}  # Ensure data is a dictionary
#     data['Q1'] = Q1
#     data['Q2'] = Q2
#     data['Q3'] = Q3
#     data['Q4'] = Q4
#     data['Q5'] = Q5
#     data['Q6'] = Q6
#     data['Q7'] = Q7
#     data['Q8'] = Q8
#     data['Q9'] = Q9
#     data['Q10'] = Q10
#     data['Q11'] = Q11
#     data['Q12'] = Q12
#     data['Q13'] = Q13
#     data['Q14'] = Q14
#     data['Q15'] = Q15
#     data['Q16'] = Q16
#     data['Q17'] = Q17
#     data['Q18'] = Q18
#     data['Q19'] = Q19
#     data['Q20'] = Q20
#     return data


# dcc.RadioItems(
#                 options=[
#                     {'label': 'Never', 'value': 'Never'},
#                     {'label': 'Rarely', 'value': 'Rarely'},
#                     {'label': "Sometimes", 'value': "Sometimes"},
#                     {'label': "Most of the time", 'value': "Most of the time"},
#                     {'label': "Always", 'value': "Always"},
#                     {'label': "Not applicable to my situation", 'value': "Not applicable to my situation"},

#                 ],
#                 inputStyle={"margin-right": "10px"},
#                 value='',
#                 id = 'Q19'
#             ),