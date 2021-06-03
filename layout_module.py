import dash_core_components as dcc
import dash_html_components as html
from widgets import (app_title_widget, upload, theme_selection_dropdown,
                     chart_type_dropdown,data_store, data_table,
                     label_for_visualization_library,xaxis_widget,yaxis_widget,
                     spinners_widget,title_of_chart_widget,
                     upload_status)
import dash_bootstrap_components as dbc

main_layout = html.Div(children=[dbc.Card([app_title_widget,data_store,label_for_visualization_library,
                                           spinners_widget,
                                 dbc.Row(
                                    [
                                        dbc.Col(theme_selection_dropdown),
                                        dbc.Col(chart_type_dropdown)
                                    ]
                                ),
                                dbc.Container([upload,
                                               upload_status])], body=True),
                                 html.Br(),
                                dbc.Container(data_table),
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col(dbc.Card(body=True,
                                                         id='graph-controls-card',
                                                         children=[title_of_chart_widget,
                                                                   xaxis_widget,yaxis_widget,

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

                                                                   dbc.FormGroup(html.Div(id='barmode-html',
                                                                                          children=[dbc.Label('Barmode'),
                                                                                                    dcc.Dropdown(
                                                                                                        options=[{'label':'overlay','value':'overlay'},
                                                                                                                 {'label':'relative','value':'relative'},
                                                                                                                 {'label':'group','value':'group'},
                                                                                                                 ],
                                                                                                        id='barmodex',
                                                                                                        placeholder='Bar mode', )])),
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
                                        dbc.Col(dbc.Card(dcc.Graph(id='graph-area'), body=True), width=9),
                                    ]
                                ),
                                # html.Div(dcc.Graph(id='graph-scatter'),style={'display': 'none'} )
                                ],
                      )