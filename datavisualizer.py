import plotly.express as px
import dash_core_components as dcc
import base64
import dash_html_components as html
import dash
import datetime
import dash_table
import io
from styles import upload_button_style, app_title_style
from graph_controls import (create_formgroup)
from widgets import create_dropdown
import pandas as pd
from widgets import (app_title_widget, upload, visualization_library_dropdown,
                     chart_type_dropdown,data_store, data_table,
                     label_for_visualization_library,label_for_dropdown,
                     upload_status)
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from layout_module import main_layout


app = dash.Dash(external_stylesheets=[dbc.themes.LITERA],suppress_callback_exceptions=True)

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
                   {'label':'Bar Charts', 'value':'Bar Charts'},
                   {'label':'Boxplot', 'value':'Boxplot'},
                   {'label':'Density Contour Charts', 'value':'Density Contour Charts'},
                   {'label':'Density Heatmap', 'value':'Density Heatmap'},
                   {'label':'Histogram', 'value':'Histogram'},
                   {'label':'Violinplot', 'value':'Violinplot'}]

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
        timestamp = datetime.datetime.fromtimestamp(last_modified)
        print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
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

    data = df.to_dict('records')

    return  column_dict,data


@app.callback(
    Output(component_id='x-axis', component_property='options'),
    Output(component_id='y-axis', component_property='options'),
    Output(component_id='size', component_property='options'),
    Output(component_id='color', component_property='options'),
    Output(component_id='text', component_property='options'),
    Output(component_id='facetrow', component_property='options'),
    Output(component_id='facetcolumn', component_property='options'),
    Input(component_id='data-table', component_property='data')
)
def generate_options(data_dict):
    df = pd.DataFrame(data_dict)
    column_list = [{'label': col, 'value': col} for col in df.columns]

    return column_list,column_list,column_list,column_list, column_list,column_list, column_list


@app.callback(
    Output(component_id='graph-area', component_property='figure'),
    Input(component_id='data-store', component_property='data'),
    Input(component_id="visualization-library-dropdown", component_property='value'),
    Input(component_id='x-axis', component_property='value'),
    Input(component_id='y-axis', component_property='value'),
    Input(component_id='color', component_property='value'),
    Input(component_id='size', component_property='value'),
    Input(component_id='symbol', component_property='value'),
    Input(component_id='hover-text', component_property='value'),
    Input(component_id='text', component_property='value'),
    Input(component_id='title', component_property='value'),
    Input(component_id='chart-type-dropdown', component_property='value'),
    Input(component_id='bins', component_property='value'),
    Input(component_id='marginalx', component_property='value'),
    Input(component_id='marginaly', component_property='value'),
    Input(component_id='facetrow', component_property='value'),
    Input(component_id='facetcolumn', component_property='value'),
    Input(component_id='logx', component_property='value'),
    Input(component_id='logy', component_property='value'),
)
def create_graph( json_data, visualization_library, xaxis, yaxis,
                        color, size, symbol, hover_name,text, title, chart_type, bins,
                  marginx, marginy, facet_row, facet_column, logx, logy):
    log_dict = dict()
    log_dict['True'] = True
    log_dict['False'] = False

    df = pd.read_json(json_data, orient='split')
    plot = px.scatter()

    if visualization_library=='plotly':
        if chart_type=='Scatterplot':

            plot = px.scatter(data_frame=df,
                              x=xaxis,
                              y=yaxis,
                              color=color,
                              size=size,
                              symbol=symbol,
                              hover_name=hover_name,
                              text=text, title=title,
                              marginal_x=marginx,
                              marginal_y=marginy,
                              facet_row=facet_row,
                              facet_col=facet_column,
                              log_x=log_dict[logx],
                              log_y=log_dict[logy])

        if chart_type == 'Histogram':
            plot = px.histogram(data_frame=df,
                                x=xaxis,
                                y=yaxis,
                                nbins=bins,
                                title=title,
                                )

        if chart_type== 'Bar Charts':
            plot = px.bar(data_frame=df,
                          x=xaxis,
                          y=yaxis,
                          facet_row=facet_row,
                          facet_col=facet_column,
                          color=color,
                          log_y=logy,
                          log_x=logx,
                          title=title,)

        if chart_type == 'Boxplot':
            plot = px.box(data_frame=df,
                          x=xaxis,
                          y=yaxis,
                          facet_row=facet_row,
                          facet_col=facet_column,
                          color=color,
                          log_y=logy,
                          log_x=logx,
                          title=title,)

        if chart_type == 'Density Contour Charts':
            plot = px.density_contour(data_frame=df,
                                      x=xaxis,
                                      y=yaxis,
                                      facet_row=facet_row,
                                      facet_col=facet_column,
                                      color=color,
                                      log_y=logy,
                                      log_x=logx,
                                      title=title)

        if chart_type == 'Density Heatmap':
            plot = px.density_heatmap(data_frame=df,
                                      x=xaxis,
                                      y=yaxis,
                                      facet_row=facet_row,
                                      facet_col=facet_column,
                                      log_y=logy,
                                      log_x=logx,
                                      title=title,)

        if chart_type == 'Violinplot':
            plot = px.violin(data_frame=df,
                             x=xaxis,
                             y=yaxis,
                             facet_row=facet_row,
                             facet_col=facet_column,
                             log_y=logy,
                             log_x=logx,
                             title=title,)

        return plot


app.layout = main_layout


if __name__ == '__main__':
    app.run_server(debug=True)