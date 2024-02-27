#!/usr/bin/env python3

#

# Import packages
import dash
from dash import Dash, dcc, html, Input, Output, callback, State
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Img(src='/assets/TickTOOL_logo.png', style={'width': '46%', 'height': '60%'}, className='image-gallery'),
    html.Br(),
    html.Hr(className='orange_line'),
    html.Br(),
    html.H1('Are you adapting to ticks ?', style={'textAlign' : 'center'}),
    #html.H1('Are you adapting to ticks ?',style={'text-align' : 'center'}),
    html.Br(),
    html.Br(),
    html.P("Would you like to better understand your risk of tick exposure or learn how to improve \
            your tick bite prevention strategy for yourself and your family? \
           The University of Montreal and eTick have developed a questionnaire designed to estimate your exposure \
            profile and to highlight areas where you can improve or modify your prevention measures. \
           A personalised report will be created for you at the end.", 
           style={"display":"flex", "gap":"1px", "align-items":"flex-end", 'font-size' : '20px'}),
    html.Br(),
    html.P("Your responses are very useful for research purposes, specifically to understand the levels of tick exposure and adoption \
           of preventive behaviours among Canadians. We kindly ask that you consent to sharing your responses with the University of Montreal. All responses are anonymous, \
            and you will not be asked to provide your name or contact information. \
           Data will be stored on a secure University of Montreal web server. \
           If you do not wish to share your responses, you may still complete the questionnaire and you will still receive a personalised report.",
           style={"display":"flex", "gap":"1px", "align-items":"flex-end", 'font-size' : '20px'}),
    html.Br(),
    html.B("Do you consent to sharing your responses with the University of Montreal?", style={'font-size': '20px'}),
    html.Br(),
    html.Br(),
    dcc.RadioItems(
            options=[
                {'label': 'Yes', 'value': 'yes'},
                {'label': 'No', 'value': 'no'}
            ],
            id = 'consent',
            value='',
            inputStyle={"margin-right": "10px"},
            labelStyle={'display': 'inline-block', 'margin-right': '15px'}
        ),
    html.Br(),
    dcc.Link('Next page', href='/page-2', style={'font-size': '20px'}),
    html.Br(),
    html.Br(),
    html.Img(src='/assets/UdeM.png', style={'width': '30%', 'height': '30%'}, className='image-gallery'),
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

