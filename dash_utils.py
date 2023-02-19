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
