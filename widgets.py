import dash_core_components as dcc
import dash_html_components as html
import dash_table
from styles import upload_button_style, app_title_style
import dash_bootstrap_components as dbc


def create_dropdown(dropdown_id, placeholder_text, options=None, value=None):
    dropdown = dcc.Dropdown(id=dropdown_id,
                            placeholder=placeholder_text,
                            options=options,
                            value=value
                         )
    return dropdown


def create_input_component(input_id, type_of_input, placeholder, debounce=False):
    return dcc.Input(id=input_id,
                     type=type_of_input,
                     placeholder=placeholder,
                     debounce=debounce)

app_markdown = dcc.Markdown("##### A FREE web tool for creating beautiful charts from your data.")

app_title_widget = dbc.Jumbotron(html.Div(children=[html.H1('Welcome to FreeCharts',),
                                                    html.Hr(),
                                                    app_markdown],
                                          style=app_title_style))

upload = dcc.Upload(id='upload-widget',children=html.Div(children=["Drag and drop file here or",
                                                html.A('Select files')],
                                      style=upload_button_style,
                                      ))

visualization_library_dropdown = create_dropdown(dropdown_id="visualization-library-dropdown",
                                                 options=[{'label':'plotly','value':'plotly'}],
                                                 value='plotly',
                                                 placeholder_text='Select Visualization Library of your choice')

label_for_dropdown = html.Label('Select the plotting library')

chart_type_dropdown = dcc.Dropdown(id='chart-type-dropdown',
                                   placeholder="Data Visualization Chart type",
                                   value='Scatterplot',
                                   options=[{'label': 'Scatterplot', 'value': 'Scatterplot'},
                                    {'label': 'Bar Charts', 'value': 'Bar Charts'},
                                    {'label': 'Boxplot', 'value': 'Boxplot'},
                                    {'label': 'Density Contour Charts', 'value': 'Density Contour Charts'},
                                    {'label': 'Density Heatmap', 'value': 'Density Heatmap'},
                                    {'label': 'Histogram', 'value': 'Histogram'},
                                    {'label': 'Violinplot', 'value': 'Violinplot'}]
                                   )

theme_selection_dropdown = dcc.Dropdown(id='theme-selection',
                                        placeholder='Select plot theme',
                                        value='plotly',
                                        options=[{'label':'Blue', 'value':'plotly'},
                                                 {'label':'White and Blue', 'value':'plotly_white'},
                                                 {'label':'Dark', 'value':'plotly_dark'},
                                                 {'label':'Grey', 'value':'ggplot2'},
                                                 {'label':'Seaborn', 'value':'seaborn'},
                                                 {'label':'Pure white', 'value':'simple_white'},])

data_store = dcc.Store(id='data-store', storage_type='memory')

data_table = dash_table.DataTable(id='data-table')

upload_status = html.Div(id='upload-status')

label_for_visualization_library = html.Label("Select visualization library and Chart type")

