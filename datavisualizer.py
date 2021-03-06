import plotly.express as px
import base64
import dash
import io
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from layout_module import main_layout
import time
from tabs_module import tab2_content, tab1_content,tab3_content
import plotly.graph_objects as go


app = dash.Dash(external_stylesheets=[dbc.themes.SIMPLEX],suppress_callback_exceptions=True)
#LITERA SOLAR SLATE DARKLY COSMO FLATLY JOURNAL LUMEN MATERIA PULSE SANDSTONE

server = app.server

app.layout = main_layout


@app.callback(
    Output("loading-1", 'children'),
    Input(component_id='data-store', component_property='data'),
    prevent_initial_callbacks=True
)
def spinners(data):
    """Handles the pre-loading functionality"""
    time.sleep(1)
    return


@app.callback(
    Output(component_id='bins-html', component_property='style'),
    Output(component_id='size-html', component_property='style'),
    Output(component_id='symbol-html', component_property='style'),
    Output(component_id='barmode-html', component_property='style'),
    Output(component_id='marginaly-html', component_property='style'),
    Output(component_id='text-html', component_property='style'),
    Output(component_id='marginalx-html', component_property='style'),
    Output(component_id='boxmode-html', component_property='style'),
    Output(component_id='violinmode-html', component_property='style'),
    Output(component_id='linegroup-html', component_property='style'),
    Output(component_id='box_boolean-html', component_property='style'),
    Output(component_id='show_points-html', component_property='style'),
    Input('chart-type-dropdown', component_property='value')
)
def hide_options(chart_type):
    if chart_type == 'Scatterplot':
        return {'display':'none'},{'display':'block'},{'display':'block'}, {'display': 'none'},{'display':'block'},{'display':'block'},{'display':'block'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'}, {'display': 'none'}, {'display': 'none'}
    if chart_type == 'Lineplot':
        return {'display':'none'},{'display':'none'},{'display':'none'}, {'display': 'none'},{'display':'none'},{'display':'none'},{'display':'none'}, {'display': 'none'}, {'display': 'none'},{'display':'block'}, {'display': 'none'}, {'display': 'none'}
    if chart_type=='Histogram':
        return {'display': 'block'}, {'display': 'none'}, {'display': 'none'}, {'display': 'none'},{'display':'none'},{'display':'none'},{'display':'block'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'}, {'display': 'none'}, {'display': 'none'}

    if chart_type=='Bar Charts':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'},{'display': 'block'},{'display':'none'},{'display':'none'},{'display':'none'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'}, {'display': 'none'}, {'display': 'none'}

    if chart_type=='Boxplot':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'},{'display':'none'},{'display':'none'},{'display':'none'}, {'display': 'block'}, {'display': 'none'},{'display': 'none'}, {'display': 'none'}, {'display': 'none'}

    if chart_type=='Violinplot':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'},{'display':'none'},{'display':'none'},{'display':'none'}, {'display': 'none'}, {'display': 'block'},{'display': 'none'}, {'display': 'block'}, {'display': 'block'}

    if chart_type=='Density Contour Charts':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'},{'display':'block'},{'display':'none'},{'display':'block'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'}, {'display': 'none'}, {'display': 'none'}

    if chart_type=='Density Heatmap':
        return {'display': 'none'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'},{'display':'block'},{'display':'none'},{'display':'block'}, {'display': 'none'}, {'display': 'none'},{'display': 'none'}, {'display': 'none'}, {'display': 'none'}

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
        # timestamp = datetime.datetime.fromtimestamp(last_modified)
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            # print(df.describe())
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
    Output(component_id='hover-text', component_property='options'),
    Output(component_id='symbol', component_property='options'),
    Output(component_id='linegroup-axis', component_property='options'),
    Input(component_id='data-table', component_property='data')
)
def generate_options(data_dict):
    df = pd.DataFrame(data_dict)
    column_list = [{'label': col, 'value': col} for col in df.columns]

    return column_list,column_list,column_list,column_list, column_list,column_list, \
           column_list,column_list, column_list, column_list


@app.callback(
    Output(component_id='graph-area', component_property='figure'),
    Input(component_id='data-store', component_property='data'),
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
    Input(component_id='theme-selection', component_property='value'),
    Input(component_id='barmodex', component_property='value'),
    Input(component_id='boxmode', component_property='value'),
    Input(component_id='violinmode', component_property='value'),
    Input(component_id='linegroup-axis', component_property='value'),
    Input(component_id='box_boolean', component_property='value'),
    Input(component_id='show_points', component_property='value'),
)
def create_graph( json_data, xaxis, yaxis,
                        color, size, symbol, hover_name,text, title, chart_type, bins,
                  marginx, marginy, facet_row, facet_column, logx, logy, theme, barmode,
                  boxmode,violinmode,linegroup, box_boolean, show_points):
    log_dict = dict()
    log_dict['True'] = True
    log_dict['False'] = False

    box_dict = dict()
    box_dict['True'] = True
    box_dict['False'] = False

    show_point_dict = dict()
    show_point_dict['False'] = False
    show_point_dict['all'] = 'all'
    show_point_dict['outliers'] = 'outliers'

    df = pd.read_json(json_data, orient='split')
    # plot = go.Figure()

    plot = None

    if chart_type == 'Lineplot':
        plot = px.line(data_frame=df,
                       x=xaxis,
                       y=yaxis,
                       color=color,
                       hover_name=hover_name,
                       text=text,
                       title=title,
                       facet_row=facet_row,
                       facet_col=facet_column,
                       log_x=log_dict[logx],
                       log_y=log_dict[logy],
                       template=theme,
                       line_group=linegroup)

    if chart_type=='Scatterplot':

        plot = px.scatter(data_frame=df,
                          x=xaxis,
                          y=yaxis,
                          color=color,
                          size=size,
                          symbol=symbol,
                          hover_name=hover_name,
                          text=text,
                          title=title,
                          marginal_x=marginx,
                          marginal_y=marginy,
                          facet_row=facet_row,
                          facet_col=facet_column,
                          log_x=log_dict[logx],
                          log_y=log_dict[logy],
                          template=theme)

        plot.write_image("scatter.png")

    if chart_type == 'Histogram':
        plot = px.histogram(data_frame=df,
                            x=xaxis,
                            y=yaxis,
                            nbins=bins,
                            color=color,
                            title=title,
                            template=theme,
                            barmode=barmode,
                            facet_row=facet_row,
                            facet_col=facet_column,
                            marginal=marginx
                            )

    if chart_type== 'Bar Charts':
        plot = px.bar(data_frame=df,
                      x=xaxis,
                      y=yaxis,
                      facet_row=facet_row,
                      facet_col=facet_column,
                      color=color,
                      log_x=log_dict[logx],
                      log_y=log_dict[logy],
                      template=theme,
                      barmode=barmode,
                      title=title,)

    if chart_type == 'Boxplot':
        plot = px.box(data_frame=df,
                      x=xaxis,
                      y=yaxis,
                      facet_row=facet_row,
                      facet_col=facet_column,
                      color=color,
                      log_x=log_dict[logx],
                      log_y=log_dict[logy],
                      template=theme,
                      title=title,boxmode=boxmode
                    )

    if chart_type == 'Density Contour Charts':
        plot = px.density_contour(data_frame=df,
                                  x=xaxis,
                                  y=yaxis,
                                  facet_row=facet_row,
                                  facet_col=facet_column,
                                  color=color,
                                  log_x=log_dict[logx],
                                  log_y=log_dict[logy],
                                  marginal_x=marginx,
                                  marginal_y=marginy,
                                  template=theme,
                                  hover_name=hover_name,
                                  title=title)

    if chart_type == 'Density Heatmap':
        plot = px.density_heatmap(data_frame=df,
                                  x=xaxis,
                                  y=yaxis,
                                  facet_row=facet_row,
                                  facet_col=facet_column,
                                  log_x=log_dict[logx],
                                  log_y=log_dict[logy],
                                  marginal_x=marginx,
                                  marginal_y=marginy,
                                  hover_name=hover_name,
                                  template=theme,
                                  title=title,)

    if chart_type == 'Violinplot':
        plot = px.violin(data_frame=df,
                         x=xaxis,
                         y=yaxis,color=color,
                         facet_row=facet_row,
                         facet_col=facet_column,
                         log_x=log_dict[logx],
                         log_y=log_dict[logy],
                         template=theme,
                         title=title,
                         violinmode=violinmode,
                         box=box_dict[box_boolean],
                         points=show_point_dict[show_points])

    return plot

@app.callback(Output('tab-div', "children"),
              [Input("tabs", "active_tab")])
def switch_tab(at):
    if at == "tab-1":
        return tab1_content
    if at == "tab-2":
        return tab2_content
    if at == "tab-3":
        return tab3_content


if __name__ == '__main__':
    app.run_server(debug=True)