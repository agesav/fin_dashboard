# dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table 
from dash.exceptions import PreventUpdate

# plotly
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# other
import flask
import yfinance as yf
import numpy as np
import sqlite3
import pandas as pd

# native
import dateutil.relativedelta
from datetime import date
import datetime


def ticker_inputs(inputID, pickerID, MONTH_CUTTOFF):
    #calculate the current date
    currentDate = date.today()    #calculate past date for the max allowed date
    pastDate = currentDate - dateutil.relativedelta.relativedelta(months=MONTH_CUTTOFF)
    
    #return the layout components
    return html.Div([
            dcc.Input(id = inputID, type="text", placeholder="MSFT"),
            html.P(" "),
            dcc.DatePickerRange(
                id = pickerID,
                min_date_allowed=pastDate,
                start_date = pastDate,
                #end_date = currentDate
            )
            ])

# combine Dash Bootstrap components Card and Alert. 
# Bootstrap’s cards provide a flexible content container and allow a 
# fair amount of customization. 
# Alert is used to easily add color and more style if desired.
def make_card(alert_message, color, cardbody, style_dict = None):
    
    return dbc.Card(
        [dbc.Alert(alert_message, color=color), dbc.CardBody(cardbody)],
        style = style_dict
        )

# used to build the price chart Accordion
def make_item(button, cardbody, i):
    # This function makes the accordion items 
    return dbc.Card([
        dbc.CardHeader(
            html.H2(
                dbc.Button(
                    button,
                    color="link",
                    id=f"group-{i}-toggle"))),
        dbc.Collapse(
            dbc.CardBody(cardbody),
            id=f"collapse-{i}")])

def make_table(id, dataframe, lineHeight = '17px', page_size = 5):
    return   dash_table.DataTable(
        id=id,
        css=[{'selector': '.row', 'rule': 'margin: 0'}],
        columns=[
            {"name": i, "id": i} for i in dataframe.columns
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'},
            style_cell={'textAlign': 'left'},
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
                'lineHeight': lineHeight
            },
        
        style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ],
        style_cell_conditional=[
            {'if': {'column_id': 'title'},
            'width': '130px'},
            {'if': {'column_id': 'post'},
            'width': '500px'},
            {'if': {'column_id': 'datetime'},
            'width': '130px'},
            {'if': {'column_id': 'text'},
            'width': '500px'}],
        page_current=0,
        page_size=page_size,
        page_action='custom',filter_action='custom',
        filter_query='',sort_action='custom',
        sort_mode='multi',
        sort_by=[]
        )#end table

