import dash_core_components as dcc
import dash_html_components as html
from widgets import (app_title_widget, upload, theme_selection_dropdown,
                     chart_type_dropdown,data_store, data_table,
                     label_for_visualization_library,
                     spinners_widget,
                     upload_status)
from tabs_module import tabs
import dash_bootstrap_components as dbc

main_layout = html.Div(children=[dbc.Card([app_title_widget,data_store,label_for_visualization_library,
                                           spinners_widget,
                                 dbc.Row(
                                    [
                                        dbc.Col(theme_selection_dropdown),
                                        dbc.Col(chart_type_dropdown)
                                    ]
                                ),
                                dbc.Container([upload,
                                               upload_status])], body=True),
                                 html.Br(),
                                dbc.Container(data_table),
                                html.Br(),
                                 tabs,
                                 html.Div(id='tab-div',),

                                ],id='content'
                      )