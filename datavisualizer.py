import plotly.express as px
import dash_core_components as dcc
import base64
import dash_html_components as html
import dash
import dash_table
import io
from styles import upload_button_style, app_title_style
import pandas as pd
from widgets import (app_title_widget, upload, visualization_library_dropdown,
                     chart_type_dropdown,data_store, data_table)
from dash.dependencies import Input, Output

# app = dash.Dash(__name__)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
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
    Input(component_id='upload-widget',component_property='contents'),
    Input(component_id='upload-widget', component_property='filename'),
    Input(component_id='upload-widget', component_property='last_modified')
)
def upload_data(contents, filename,last_modified):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    print(content_type)
    # print(content_string)
    # print(decoded)
    if 'csv' in filename:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        print(df.head())
    elif 'xlsx' in filename:
        pass
    else:
        return None

    return df.to_json( orient='split')


@app.callback(
    Output(component_id='data-table', component_property='columns'),
    Output(component_id='data-table', component_property='data'),
    Input(component_id='data-store', component_property='data')
)
def view_data(json_data):
    df = pd.read_json(json_data, orient='split')

    column_dict = [{'name':col, 'id':col} for col in df.columns]
    print('json loaded')
    print(column_dict)

    data = df.to_dict('records')

    return  column_dict,data


app.layout = html.Div(children=[app_title_widget,
                                upload,
                                html.Div(children=[visualization_library_dropdown,chart_type_dropdown]),
                                data_store, data_table])


if __name__ == '__main__':
    app.run_server(debug=True)