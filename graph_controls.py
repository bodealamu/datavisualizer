import dash_bootstrap_components as dbc
import dash_core_components as dcc


scatter_plot_controls = dbc.Card(body=True,
                                 children=[
                                     dbc.FormGroup(
                                         [
                                             dbc.Label('X axis'),
                                             dcc.Dropdown(
                                                 id='scatter-dropdown-xaxis',
                                                 placeholder="Select columns for X axis",

                                             )

                                         ]
                                     ),
                                     dbc.FormGroup(
                                         [
                                             dbc.Label('Y axis'),
                                             dcc.Dropdown(
                                                 id='scatter-dropdown-yaxis',
                                                 placeholder='Select column for Y axis'
                                             )
                                         ]
                                     )
                                 ])