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
                                                                                          children=[dbc.Label('Size (Optional)'),
                                                                                                    dcc.Dropdown(id='size',
                                                                                                                 placeholder='Select Column for text',)])),
                                                                   dbc.FormGroup(html.Div(id='color-html',
                                                                                          children=[dbc.Label('Color (Optional)'),
                                                                                                    dcc.Dropdown(id='color',
                                                                                                                 placeholder='Select Column for text',)])),
                                                                   dbc.FormGroup(html.Div(id='text-html',
                                                                                          children=[dbc.Label('Text (Optional)'),
                                                                                                    dcc.Dropdown(id='text',
                                                                                                                 placeholder='Select Column for text',)])),
                                                                   dbc.FormGroup(html.Div(id='hover-html',
                                                                                          children=[dbc.Label('Hover Text (Optional)'),
                                                                                                    dcc.Dropdown(
                                                                                                        id='hover-text',
                                                                                                        placeholder='X axis', )])),
                                                                   dbc.FormGroup(html.Div(id='symbol-html',
                                                                                          children=[dbc.Label('Symbol (Optional)'),
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
                                                                                              'Title of the chart (Optional)'),
                                                                                                    dcc.Input(
                                                                                                        id='title',
                                                                                                        type='text',
                                                                                                        placeholder='Chart title',
                                                                                                        debounce=False)])),
                                                                   dbc.FormGroup(html.Div(id='marginalx-html',
                                                                                          children=[dbc.Label('Marginal X (Optional)'),
                                                                                                    dcc.Dropdown(
                                                                                                        options=[{'label':'rug','value':'rug'},
                                                                                                                 {'label':'box','value':'box'},
                                                                                                                 {'label':'violin','value':'violin'},
                                                                                                                 {'label':'histogram','value':'histogram'}],
                                                                                                        id='marginalx',
                                                                                                        placeholder='Marginal X', )])),
                                                                   dbc.FormGroup(html.Div(id='marginaly-html',
                                                                                          children=[dbc.Label('Marginal Y (Optional)'),
                                                                                                    dcc.Dropdown(
                                                                                                        options=[{'label':'rug','value':'rug'},
                                                                                                                 {'label':'box','value':'box'},
                                                                                                                 {'label':'violin','value':'violin'},
                                                                                                                 {'label':'histogram','value':'histogram'}],
                                                                                                        id='marginaly',
                                                                                                        placeholder='Marginal Y', )])),
                                                                   dbc.FormGroup(html.Div(id='logx-html',
                                                                                          children=[dbc.Label('Log X (Optional)'),
                                                                                                    dcc.RadioItems(
                                                                                                        options=[{'label':'True', 'value':"True"},
                                                                                                                {'label':'False', 'value':'False'}],
                                                                                                        id='logx',
                                                                                                        value="False"
                                                                                                         )])),
                                                                   dbc.FormGroup(html.Div(id='logy-html',
                                                                                          children=[dbc.Label('Log Y (Optional)'),
                                                                                                    dcc.RadioItems(
                                                                                                        options=[{'label':'True', 'value':'True'},
                                                                                                                {'label':'False', 'value':'False'}],
                                                                                                        id='logy',
                                                                                                        value='False'
                                                                                                    )])),
                                                                   dbc.FormGroup(html.Div(id='facetrow-html',
                                                                                          children=[dbc.Label('Facet row (Optional)'),
                                                                                                    dcc.Dropdown(
                                                                                                        id='facetrow',
                                                                                                        placeholder='Facet row', )])),
                                                                   dbc.FormGroup(html.Div(id='facetcolumn-html',
                                                                                          children=[dbc.Label('Facet Column (Optional)'),
                                                                                                    dcc.Dropdown(
                                                                                                        id='facetcolumn',
                                                                                                        placeholder='Facet column', )])),
                                                                   ]
                                                         ),
                                                width=3),
                                        dbc.Col(dbc.Card(dcc.Graph(id='graph-area'), body=True), width=8),
                                    ]
                                ),
                                # html.Div(dcc.Graph(id='graph-scatter'),style={'display': 'none'} )
                                ],
                      )