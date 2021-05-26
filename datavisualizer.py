import plotly.express as px
import dash_core_components as dcc
import base64
import dash_html_components as html
import dash
import datetime
import dash_table
import io
from styles import upload_button_style, app_title_style
import pandas as pd
from widgets import (app_title_widget, upload, visualization_library_dropdown,
                     chart_type_dropdown,data_store, data_table,
                     label_for_visualization_library,label_for_dropdown,
                     upload_status)
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])

server = app.server


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
    success_message =''

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

        success_message = 'file with name ' +str(filename)
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


# dbc.Col(label_for_dropdown, width=2),

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


                                ],
                      )


if __name__ == '__main__':
    app.run_server(debug=True)