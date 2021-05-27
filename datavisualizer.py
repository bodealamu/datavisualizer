import plotly.express as px
import dash_core_components as dcc
import base64
import dash_html_components as html
import dash
import datetime
import dash_table
import io
from styles import upload_button_style, app_title_style
from graph_controls import (create_dropdown,create_formgroup)
import pandas as pd
from widgets import (app_title_widget, upload, visualization_library_dropdown,
                     chart_type_dropdown,data_store, data_table,
                     label_for_visualization_library,label_for_dropdown,
                     upload_status)
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


app = dash.Dash(external_stylesheets=[dbc.themes.LITERA],suppress_callback_exceptions=True)

server = app.server

# handle callback from dynamically generated callbacks



# callbacks
@app.callback(
    Output(component_id='chart-type-dropdown', component_property='options'),
    Input(component_id="visualization-library-dropdown",component_property='value')
)
def create_dropdown(value):

    options = list()
    if value=='plotly':
        options = [{'label':'Scatterplot', 'value':'Scatterplot'},
                   {'label':'Histogram', 'value':'Histogram'}]

    return options


@app.callback(
    Output(component_id='data-store', component_property='data'),
    Output(component_id='upload-status', component_property='children'),
    Input(component_id='upload-widget',component_property='contents'),
    Input(component_id='upload-widget', component_property='filename'),
    Input(component_id='upload-widget', component_property='last_modified')
)
def upload_data(contents, filename,last_modified):
    df = pd.DataFrame([])
    success_message = str('')

    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        print(content_type)
        timestamp = datetime.datetime.fromtimestamp(last_modified)
        print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            print(df.head())
        elif 'xlsx' in filename:
            pass
        else:
            return None

        success_message = 'file with name ' +str(filename) + " uploaded."
    except Exception as e:
        print(e)

    return df.to_json( orient='split'),success_message


@app.callback(
    Output(component_id='data-table', component_property='columns'),
    Output(component_id='data-table', component_property='data'),
    Input(component_id='data-store', component_property='data')
)
def view_data(json_data):
    df = pd.read_json(json_data, orient='split')

    df = df.head(5)

    column_dict = [{'name':col, 'id':col} for col in df.columns]
    print('json loaded')
    print(column_dict)

    data = df.to_dict('records')

    return  column_dict,data


@app.callback(
    Output(component_id='graph-controls-card', component_property='children'),
    Input(component_id="visualization-library-dropdown", component_property='value'),
    Input(component_id='chart-type-dropdown', component_property='value'),
    Input(component_id='data-table', component_property='data')
)
def create_graph_controls_card(visualization_library, chart_type, data):
    print('callback hell')
    df = pd.DataFrame(data)
    print(df.shape)
    column_list = [{'label': col, 'value':col} for col in df.columns]
    print(column_list)
    print('here agaian')

    xaxis = create_formgroup(label='X axis', dropdown_id='x-axis', placeholder_text='X axis', options=column_list)
    yaxis = create_formgroup(label='Y axis', dropdown_id='y-axis', placeholder_text='Y axis', options=column_list)
    color = create_formgroup(label='Color', dropdown_id='color', placeholder_text='Select color', options=column_list)
    size = create_formgroup(label='Size', dropdown_id='size', placeholder_text='Size', options=column_list)

    print(xaxis.children[1])

    if visualization_library=='plotly':
        if chart_type=='Scatterplot':
            # if data is not None:

            return [xaxis, yaxis, color, size]




@app.callback(
    Output(component_id='graph-area', component_property='figure'),
    Input(component_id='data-store', component_property='data'),
    Input(component_id="visualization-library-dropdown", component_property='value'),
    Input(component_id='x-axis', component_property='value'),
    Input(component_id='y-axis', component_property='value'),
    Input(component_id='color', component_property='value'),
    Input(component_id='size', component_property='value')
)
def create_scatterplot( json_data, visualization_library, xaxis, yaxis, color, size):
    print(json_data)
    print(xaxis)
    df = pd.read_json(json_data, orient='split')
    plot = px.scatter()
    print(df.shape)
    if visualization_library=='plotly':
        if xaxis:

            plot = px.scatter(data_frame=df,
                              x=xaxis,
                              y=yaxis,
                              color=color,
                              size=size)

        return plot


app.layout = html.Div(children=[app_title_widget,
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
                                                         id='graph-controls-card'
                                                         ),
                                                width=3),
                                        dbc.Col(dcc.Graph(id='graph-area'), width=8)
                                    ]
                                )
                                ],
                      )


if __name__ == '__main__':
    app.run_server(debug=True)