import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash
from styles import upload_button_style, app_title_style
from widgets import app_title_widget, upload, visualization_library_dropdown, chart_type_dropdown
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


app.layout = html.Div(children=[app_title_widget,
                                upload,
                                html.Div(children=[visualization_library_dropdown,chart_type_dropdown]), ])


if __name__ == '__main__':
    app.run_server(debug=True)