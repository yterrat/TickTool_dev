#!/usr/bin/env python3

# Import packages
import dash
from dash import dcc, html, Input, Output, callback, State
import dash_daq as daq
import datetime
import csv
import dash_bootstrap_components as dbc
from flask import request

# Register the page
dash.register_page(__name__, path='/page-9')

layout = html.Div([
    html.Img(src='/assets/logo-white.png', style={'width': '10%', 'height': '10%'}), 
    html.H1('your personalized report', style={'text-align' : 'center', 'font-size' : '40px', "font-weight": "bold"}),
    html.Br(),
    html.P('Potential for BLT in environment', style={'font-size' : '20px', "font-weight": "bold"}),
    daq.Gauge(
    color={"gradient":True,"ranges":{"green":[0,1],"yellow":[1,2],"red":[2,3]}},
    max=3,
    min=0,
    label = '',
    showCurrentValue = False,
    value = 1,
    units = '',
    id='gauge1'
    ),
    html.Hr(className='grey_line'),
    html.Br(),
    html.P('Risk of exposure', style={'font-size' : '20px', "font-weight": "bold"}),
    daq.Gauge(
    color={"gradient":True,"ranges":{"green":[0,1],"yellow":[1,2],"red":[2,3]}},
    max=3,
    min=0,
    label = '',
    value = 2,
    showCurrentValue = False,
    units = '',
    id='gauge2'
    ),
    html.Hr(className='grey_line'),
    html.Br(),
    html.P('Level of preventive behaviours', style={'font-size' : '20px', "font-weight": "bold"}),
    daq.Gauge(
    color={"gradient":True,"ranges":{"green":[0,1],"yellow":[1,2],"red":[2,3]}},
    max=3,
    min=0,
    label = '',
    value = 3,
    showCurrentValue = False,
    units = '',
    id='gauge3'
    )
])

# @callback([Output(component_id='gauge1', component_property='value'),
#           Output(component_id='gauge2', component_property='value'),
#           Output(component_id='gauge3', component_property='value')],
#           Input(component_id='record_answers', component_property='data')
#           )

# def calculat_score_and_record_answers(data):
#     now = datetime.datetime.now()
#     ip_address = request.remote_addr
#     #myline  = now.strftime('%Y-%m-%d %H:%M:%S')
#     myline = str(ip_address) + '\t' + now.strftime('%Y-%m-%d %H:%M:%S') 
#     for v in data.values():
#         myline += '\t' + str(v)
#     myline += '\n'
#     filename = 'survey_results_' + now.strftime('%Y-%m-%d') + '.tsv'
#     with open(filename, 'a') as tsvfile:
#         tsvfile.write(myline)
#     ######
#     score1 = int(data['Q1']) + int(data['Q2']) 
#     score2 = int(data['Q3']) + int(data['Q4']) 
#     score3 = int(data['Q5']) + int(data['Q6']) 
#     return score1, score2, score3



# Update the global store with answers from current page

