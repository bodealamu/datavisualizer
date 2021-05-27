import dash_core_components as dcc
import dash_html_components as html
import dash_table
from styles import upload_button_style, app_title_style
import dash_bootstrap_components as dbc

app_title_widget = dbc.Jumbotron(html.Div(children=[html.H1('Open Source Data Visualizer',)],
                     style=app_title_style))

upload = dcc.Upload(id='upload-widget',children=html.Div(children=["Drag and drop file here or",
                                                html.A('Select files')],
                                      style=upload_button_style,
                                      ))

visualization_library_dropdown = dcc.Dropdown(id="visualization-library-dropdown",
                                              options=[{'label':'plotly','value':'plotly'}],
                                              value='plotly')

label_for_dropdown = html.Label('Select the plotting library')

chart_type_dropdown = dcc.Dropdown(id='chart-type-dropdown',
                                   placeholder="Data Visualization Chart type",
                                   value='Scatterplot')

data_store = dcc.Store(id='data-store', storage_type='memory')

data_table = dash_table.DataTable(id='data-table')

upload_status = html.Div(id='upload-status')

label_for_visualization_library = html.Label("Select visualization library and Chart type")

