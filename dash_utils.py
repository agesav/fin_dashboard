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