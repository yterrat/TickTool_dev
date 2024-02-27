#!/usr/bin/env python3

#

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '40%', 'height': '40%'}, className='center'),
    html.Br(),
    html.Hr(className='orange_line'),
    html.Br(),
    html.B('Are you adapting to ticks ?', style={'text-align' : 'center', 'font-size' : '40px'}, className='center'),
    #html.H1('Are you adapting to ticks ?',style={'text-align' : 'center'}),
    html.Br(),
    html.Br(),
    html.P("Would you like to better understand your risk of tick exposure or learn how to improve \
            your tick bite prevention strategy for yourself and your family?", style={'font-size': '20px'}),
    html.P("The University of Montreal and eTick have developed a questionnaire designed to estimate your exposure \
            profile and to highlight areas where you can improve or modify your prevention measures. \
           A personalised report will be created for you at the end.",  style={'font-size': '20px'}),
    html.P("Your responses are very useful for research purposes, specifically to understand the levels of tick exposure and adoption \
           of preventive behaviours among Canadians. We kindly ask that you consent to sharing your responses with the University of Montreal. All responses are anonymous, \
            and you will not be asked to provide your name or contact information. \
           Data will be stored on a secure University of Montreal web server. ", style={'font-size': '20px'}),
    html.P("If you do not wish to share your responses, you may still complete the questionnaire and you will still receive a personalised report.",  style={'font-size': '20px'}),
    html.P("Do you consent to sharing your responses with the University of Montreal?", style={'font-size': '20px'}),
    dcc.RadioItems(
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            id = 'consent',
            value='',
            labelStyle={'display': 'inline-block', 'margin-right': '20px'}
        ),
    html.Br(),
    dcc.Link('Next page', href='/page-2', style={'font-size': '20px'}),
    html.Br(),
    html.Br(),
    html.Img(src='/assets/UdeM.png', style={'width': '30%', 'height': '30%'}, className='center'),
    html.Br(())
])


@callback(
    Output('record_answers', 'data',  allow_duplicate=True),
    Input('consent', 'value'),
    State('record_answers', 'data'),
    prevent_initial_call=True,
)
def update_dic(Q1, data):
    # Update the dictionary based on the input values
    data = data or {}  # Ensure data is a dictionary
    data['Q1'] = Q1
    return data

#git add
# git commit -am "updated whatever"
#git push

