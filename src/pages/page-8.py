#!/usr/bin/env python3

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/page-8')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '40%', 'height': '40%'}, className='image-gallery'),
    html.Hr(className='orange_line'),
    html.Br(),
    html.P('Thank you for agreeing to share your responses for research purposes.\
            We would be grateful if you could complete the following socio-demographic questions.\
        This information helps us direct Lyme disease educational material to where it is most useful.',
        style={"display":"flex", "gap":"1px", "align-items":"flex-end", 'font-size' : '20px'}),
    html.Br(),
    html.H1('Socio-demographic questions', style={'text-align' : 'center'}),
    ####
    # Q27
    ####
    html.P("What is your gender?", className='question_style2'),
    #Changre into ckeckbox
    html.Div([
        dcc.Checklist(
                options=[
                    {'label': 'Gender-fluid', 'value': 'Gender-fluid'},
                    {'label': "Man", 'value': "Man"},
                    {'label': "NonBinary", 'value': "NonBinary"},
                    {'label': "Trans Man", 'value': "Trans Man"},
                    {'label': "Trans Women", 'value': "Trans Women"},
                    {'label': "Two-spirit", 'value': "Two-spirit"},
                    {'label': "Women", 'value': "Women"},
                    {'label': "I don’t identify with any option provided ", 'value': "I don’t identify with any option provided "},
                    {'label': "I prefer not to answer ", 'value': "I prefer not to answer"}
                ],
                inputStyle={"margin-right": "10px"}
            )],
            style={'font-size': '15px', 'marginLeft' : '30px'}
        ),
    html.Hr(className='grey_blue_line'),
    ######
    # Q28
    ######
    html.P("How old are you? ",  className='question_style2'),
    html.Div([
        dcc.RadioItems(
                options=[
                    {'label': 'I prefer not answer', 'value': 'I prefer not answer'},
                    {'label': "Under 18", 'value': "Under 18"},
                    {'label': "18-24", 'value': "18-24"},
                    {'label': "25-34", 'value': "25-34"},
                    {'label': "35-44", 'value': "35-44"},
                    {'label': "45-54", 'value': "45-54"},
                    {'label': "55-64", 'value': "55-64"},
                    {'label': "65-74 ", 'value': "65-74"},
                    {'label': "75 or older", 'value': "75 or older"}
                ],
                inputStyle={"margin-right": "10px"}
            )],
            style={'font-size': '15px', 'marginLeft' : '30px'}
        ),
    html.Hr(className='grey_blue_line'),
    ######
    # Q29
    ######
    html.P("What is the highest level of formal education that you have completed to date?", className='question_style2'),
    html.Div([
        dcc.RadioItems(
                options=[
                    {'label': 'Elementary school or less', 'value': 'Elementary school or less'},
                    {'label': "Some post-secondary school", 'value': "Some post-secondary school"},
                    {'label': "College, vocational or trade school", 'value': "College, vocational or trade school"},
                    {'label': "Undergraduate university program", 'value': "Undergraduate university program"},
                    {'label': "Graduate or professional university program", 'value': "Graduate or professional university program"},
                    {'label': "I prefer not to answer ", 'value': "I prefer not to answer"}
                ],
                inputStyle={"margin-right": "10px"},
                value=''
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    html.Hr(className='grey_blue_line'),
    ######
    # Q30
    ######
    html.P("Which of the following categories best describes your current employment status? ", className='question_style2'),
    html.Div([
        dcc.RadioItems(
                options=[
                    {'label': 'Working full-time (35 or more hours per week)', 'value': 'Working full-time (35 or more hours per week)'},
                    {'label': "Self-employed", 'value': "Self-employed"},
                    {'label': "Student attending full time school (not working)", 'value': "Student attending full time school (not working)"},
                    {'label': "Unemployed, but looking for work", 'value': "Unemployed, but looking for work"},
                    {'label': "Retired", 'value': "Retired"},
                    {'label': "Unemployed, but looking for work", 'value': "Unemployed, but looking for work"},
                    {'label': "Other", 'value': "Other"},
                    {'label': "I prefer not to answer ", 'value': "I prefer not to answer"}
                ],
                inputStyle={"margin-right": "10px"},
                value=''
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    html.Hr(className='grey_blue_line'),
    ######
    # Q31
    ######
    html.P("Which of the following categories best describes your total household income? That is, the total income of all persons in your household, before taxes?", className='question_style2'),
    html.Div([
        dcc.RadioItems(
                options=[
                    {'label': 'Under $20,000', 'value': 'Under $20,000'},
                    {'label': "$20,000 to just under $40,000", 'value': "$20,000 to just under $40,000"},
                    {'label': "$40,000 to just under $60,000", 'value': "$40,000 to just under $60,000"},
                    {'label': "$60,000 to just under $80,000", 'value': "$60,000 to just under $80,000"},
                    {'label': "$80,000 to just under $100,000", 'value': "$80,000 to just under $100,000"},
                    {'label': "$100,000 to just under $120,000", 'value': "$100,000 to just under $120,000"},
                    {'label': "$120,000 to just under $150,000", 'value': "$120,000 to just under $150,000"},
                    {'label': "$150,000 and above", 'value': "$150,000 and above"},
                    {'label': "I prefer not to answer ", 'value': "I prefer not to answer"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    html.Hr(className='grey_blue_line'),
    ######
    # Q31
    ######
    html.P("What is the primary language spoken in your household?", className='question_style2'),
    html.Div([
        dcc.RadioItems(
                options=[
                    {'label': 'English', 'value': 'English'},
                    {'label': "French", 'value': "French"},
                    {'label': "Other (please specify)", 'value': "Other (please specify)"},
                    {'label': "I prefer not to answer ", 'value': "I prefer not to answer"}
                ],
                inputStyle={"margin-right": "10px"},
                value='',
                #id = 'QXXX'
            ),
        ], style={'font-size': '15px', 'marginLeft' : '30px'}),
    html.Hr(className='grey_blue_line'),
    ######
    # Q31
    ######
    html.P("Please indicate the 6 characters of your postal code. Note that you will not be identified in any way.\
            Postal codes will be used to define areas of greatest interest for Lyme disease programs and education", className='question_style2'),
    dcc.Input(),
    html.Br(),
    ######
    # Q32
    ######
    html.Br(),
    html.P("If you did not answered to the previous question, would you share the first 3 characters of your postal code?  ", className='question_style2'),
    dcc.Input(),
    html.Br(),
    html.Hr(className='grey_blue_line'),
    html.P("You have now completed the questionnaire! Thank you for your interest. If you would like to comment on your experience of completing the questionnaire, or on any of its content, please do so here", className='question_style2'),
    dcc.Textarea(
        id='commentaries',
        value='Any comments ?',
        style={'width': '100%', 'height': 300}
    ),
    html.Br(),
    html.Br(),
    html.P('To access your personalised exposure profile report, please click here.', style={'font-size' : '20px', "font-weight": "bold"}),
    dcc.Link('Submit', href='/page-9'),
    html.Br(),
    html.Br(),
    dbc.Progress(value=100, style={"height": "15px"}, className="mb-3", label = "100% done"),
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