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

data_disclaimer_markdown = dcc.Markdown("No worries, the data you insert will be processed only by the web browser. ")
data_disclaimer2 = dcc.Markdown("No server-side operations or storages are performed, no one will see, touch or copy your data!")
app_markdown = dcc.Markdown("##### A FREE web tool for creating beautiful charts from your data.")

app_title_widget = dbc.Jumbotron(html.Div(children=[html.H1('Welcome to FreeCharts',style={'color':'red'}),
                                                    html.Hr(),
                                                    app_markdown,data_disclaimer_markdown, data_disclaimer2],
                                          style=app_title_style))

upload = dcc.Upload(id='upload-widget',max_size=10000000,children=html.Div(children=["Drag and drop your csv file (10Mb max) here or",
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
                                    {'label': 'Violinplot', 'value': 'Violinplot'},
                                    {'label': 'Lineplot', 'value': 'Lineplot'}]
                                   )

theme_selection_dropdown = dcc.Dropdown(id='theme-selection',
                                        placeholder='Select plot theme',
                                        value='ggplot2',
                                        options=[{'label':'Blue', 'value':'plotly'},
                                                 {'label':'White and Blue', 'value':'plotly_white'},
                                                 {'label':'Dark', 'value':'plotly_dark'},
                                                 {'label':'Grey', 'value':'ggplot2'},
                                                 {'label':'Grey and Blue', 'value':'seaborn'},
                                                 {'label':'Pure white', 'value':'simple_white'},],
                                        )

data_store = dcc.Store(id='data-store', storage_type='memory')

data_table = dash_table.DataTable(id='data-table')

upload_status = html.Div(id='upload-status')

label_for_visualization_library = html.Label("Select visualization library and Chart type")

spinners_widget = dcc.Loading(id="loading-1",
                              fullscreen=True,
                              type="default",
                              children=html.Div(id="loading-output-1"))

# graph control widget

title_of_chart_widget = dbc.FormGroup(html.Div(id='title-html',children=[dbc.Label('Title of the chart'),
                                                                                    dcc.Input(
                                                                                        id='title',
                                                                                        type='text',
                                                                                        placeholder='Chart title',
                                                                                        debounce=False)]))

xaxis_widget =dbc.FormGroup(html.Div(id='xaxis-html',children=[dbc.Label('X axis'),
                                                               dcc.Dropdown(id='x-axis',
                                                                            placeholder='Select Column for X axis',)]))


yaxis_widget = dbc.FormGroup(html.Div(id='yaxis-html',children=[dbc.Label('Y axis'),dcc.Dropdown(id='y-axis',
                                                                                                 placeholder='Select Column for Y axis', )]))

logx_widget = dbc.FormGroup(html.Div(id='logx-html',
                                     children=[dbc.Label('Log X (Optional)'),
                                               dcc.RadioItems(options=[{'label':'True', 'value':"True"},
                                                                       {'label':'False', 'value':'False'}],
                                                              id='logx', value="False")]))

logy_widget = dbc.FormGroup(html.Div(id='logy-html',
                                     children=[dbc.Label('Log Y (Optional)'),
                                               dcc.RadioItems(options=[{'label':'True', 'value':'True'},
                                                                       {'label':'False', 'value':'False'}],
                                                                    id='logy',value='False')]))
size_widget = dbc.FormGroup(html.Div(id='size-html',
                                     children=[dbc.Label('Size (Optional)'),
                                               dcc.Dropdown(id='size',placeholder='Select Column for Size',)]))
color_widget=dbc.FormGroup(html.Div(id='color-html',
                                    children=[dbc.Label('Color (Optional)'),
                                              dcc.Dropdown(id='color',placeholder='Select Column for Color',)]))

text_widget=dbc.FormGroup(html.Div(id='text-html',
                                   children=[dbc.Label('Text (Optional)'),
                                             dcc.Dropdown(id='text',placeholder='Select Column for text',)]))

hover_text_widget = dbc.FormGroup(html.Div(id='hover-html',
                                           children=[dbc.Label('Hover Text (Optional)'),
                                                     dcc.Dropdown(id='hover-text',
                                                                  placeholder='Text on hover', )]))

symbol_widget = dbc.FormGroup(html.Div(id='symbol-html', children=[dbc.Label('Symbol (Optional)'),
                                                                   dcc.Dropdown(id='symbol', placeholder='Symbol', )]))
bins_widget = dbc.FormGroup(html.Div(id='bins-html', children=[dbc.Label('Number of bins'),
                                                               dcc.Input(id='bins', type='number',
                                                                         placeholder='Number of bins',
                                                                         debounce=False)]))

barmode_widget = dbc.FormGroup(html.Div(id='barmode-html', children=[dbc.Label('Barmode'), dcc.Dropdown(
    options=[{'label': 'overlay', 'value': 'overlay'}, {'label': 'relative', 'value': 'relative'},
             {'label': 'group', 'value': 'group'}, ], id='barmodex', placeholder='Bar mode', )]))

boxmode_widget = dbc.FormGroup(html.Div(id='boxmode-html', children=[dbc.Label('Boxmode'), dcc.Dropdown(
    options=[{'label': 'overlay', 'value': 'overlay'}, {'label': 'group', 'value': 'group'}, ], id='boxmode',
    placeholder='Box mode', )]))
violinmode_widget = dbc.FormGroup(html.Div(id='violinmode-html', children=[dbc.Label('Violinmode'), dcc.Dropdown(
    options=[{'label': 'overlay', 'value': 'overlay'}, {'label': 'group', 'value': 'group'}, ], id='violinmode',
    placeholder='Violin mode', )]))
marginalx_widget = dbc.FormGroup(html.Div(id='marginalx-html', children=[dbc.Label('Marginal X (Optional)'),
                                                                         dcc.Dropdown(
                                                                             options=[{'label': 'rug', 'value': 'rug'},
                                                                                      {'label': 'box', 'value': 'box'},
                                                                                      {'label': 'violin',
                                                                                       'value': 'violin'},
                                                                                      {'label': 'histogram',
                                                                                       'value': 'histogram'}],
                                                                             id='marginalx',
                                                                             placeholder='Marginal X', )]))
marginaly_widget = dbc.FormGroup(html.Div(id='marginaly-html', children=[dbc.Label('Marginal Y (Optional)'),
                                                                         dcc.Dropdown(
                                                                             options=[{'label': 'rug', 'value': 'rug'},
                                                                                      {'label': 'box', 'value': 'box'},
                                                                                      {'label': 'violin',
                                                                                       'value': 'violin'},
                                                                                      {'label': 'histogram',
                                                                                       'value': 'histogram'}],
                                                                             id='marginaly',
                                                                             placeholder='Marginal Y', )]))

facetrow_widget = dbc.FormGroup(html.Div(id='facetrow-html', children=[dbc.Label('Facet row (Optional)'),
                                                                       dcc.Dropdown(id='facetrow',
                                                                                    placeholder='Facet row', )]))
facetcol_widget = dbc.FormGroup(html.Div(id='facetcolumn-html', children=[dbc.Label('Facet Column (Optional)'),
                                                                          dcc.Dropdown(id='facetcolumn',
                                                                                       placeholder='Facet column', )]))

linegroup_widget =dbc.FormGroup(html.Div(id='linegroup-html',children=[dbc.Label('Line group'),
                                                               dcc.Dropdown(id='linegroup-axis',
                                                                            placeholder='Select Column for Line group',)]))
