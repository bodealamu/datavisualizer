import dash_core_components as dcc
import dash_html_components as html
import dash_table
from styles import upload_button_style, app_title_style

app_title_widget = html.Div(children=[html.H1('Data Visualizer',className='jumbotron')],
                     style=app_title_style)

upload = dcc.Upload(id='upload-widget',children=html.Div(children=["Drag and drop file here or",
                                                html.A('Select files')],
                                      style=upload_button_style,
                                      ))

visualization_library_dropdown = dcc.Dropdown(id="visualization-library-dropdown",
                                              options=[{'label':'plotly','value':'plotly'}],
                                              value='plotly')

chart_type_dropdown = dcc.Dropdown(id='chart-type-dropdown',)

data_store = dcc.Store(id='data-store', storage_type='memory')

data_table = dash_table.DataTable(id='data-table')

