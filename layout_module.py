import plotly.express as px
import dash_core_components as dcc
import base64
import dash_html_components as html
import dash
import datetime
import dash_table
import io
from styles import upload_button_style, app_title_style
from graph_controls import (create_formgroup)
from widgets import create_dropdown
import pandas as pd
from widgets import (app_title_widget, upload, visualization_library_dropdown,
                     chart_type_dropdown,data_store, data_table,
                     label_for_visualization_library,label_for_dropdown,
                     upload_status)
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

main_layout = html.Div(children=[app_title_widget,
                                 data_store,
                                label_for_visualization_library,
                                dbc.Row(
                                    [
                                        dbc.Col(visualization_library_dropdown),
                                        dbc.Col(chart_type_dropdown)
                                    ]
                                ),
                                dbc.Container([upload,
                                               upload_status]),
                                dbc.Container(data_table),
                                html.Hr(),
                                dbc.Row(
                                    [
                                        dbc.Col(dbc.Card(body=True,
                                                         id='graph-controls-card',
                                                         children=[dbc.FormGroup(html.Div(id='xaxis-html',
                                                                                          children=[dbc.Label('X axis'),
                                                                                                    dcc.Dropdown(id='x-axis',
                                                                                                                 placeholder='Select Column for text',)])),
                                                                   dbc.FormGroup(html.Div(id='yaxis-html',
                                                                                          children=[dbc.Label('Y axis'),
                                                                                                    dcc.Dropdown(
                                                                                                        id='y-axis',
                                                                                                        placeholder='Select Column for text', )])),
                                                                   dbc.FormGroup(html.Div(id='size-html',
                                                                                          children=[dbc.Label('Size'),
                                                                                                    dcc.Dropdown(id='size',
                                                                                                                 placeholder='Select Column for text',)])),
                                                                   dbc.FormGroup(html.Div(id='color-html',
                                                                                          children=[dbc.Label('Color'),
                                                                                                    dcc.Dropdown(id='color',
                                                                                                                 placeholder='Select Column for text',)])),
                                                                   dbc.FormGroup(html.Div(id='text-html',
                                                                                          children=[dbc.Label('Text'),
                                                                                                    dcc.Dropdown(id='text',
                                                                                                                 placeholder='Select Column for text',)])),
                                                                   dbc.FormGroup(html.Div(id='hover-html',
                                                                                          children=[dbc.Label('Hover Text'),
                                                                                                    dcc.Dropdown(
                                                                                                        id='hover-text',
                                                                                                        placeholder='X axis', )])),
                                                                   dbc.FormGroup(html.Div(id='symbol-html',
                                                                                          children=[dbc.Label('Symbol'),
                                                                                                    dcc.Dropdown(
                                                                                                        id='symbol',
                                                                                                        placeholder='X axis', )])),
                                                                   dbc.FormGroup(html.Div(id='bins-html',
                                                                                          children=[dbc.Label('Number of bins'),
                                                                                                    dcc.Input(
                                                                                                        id='bins',
                                                                                                        type='number',
                                                                                                        placeholder='Number of bins',
                                                                                                        debounce=False)])),
                                                                   dbc.FormGroup(html.Div(id='title-html',
                                                                                          children=[dbc.Label(
                                                                                              'Title of the chart'),
                                                                                                    dcc.Input(
                                                                                                        id='title',
                                                                                                        type='text',
                                                                                                        placeholder='Chart title',
                                                                                                        debounce=False)])),
                                                                   ]
                                                         ),
                                                width=3),
                                        dbc.Col(dcc.Graph(id='graph-area'), width=8),
                                    ]
                                ),
                                # html.Div(dcc.Graph(id='graph-scatter'),style={'display': 'none'} )
                                ],
                      )