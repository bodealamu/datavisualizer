import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import dash

#
# app = dash.Dash(__name__)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

upload_button_style = {'width':'100%',
                       'height':'60px',
                       'margin':'10px',
                       'textAlign':'center'}

app_title = html.Div(children=[html.H1('Data Visualizer')],
                     style={'textAlign':'center'})
upload = dcc.Upload(children=html.Div(children=["Drag and drop file here or",
                                                html.A('Select files')],
                                      style=upload_button_style))



app.layout = html.Div(children=[app_title,upload])


if __name__ == '__main__':
    app.run_server(debug=True)