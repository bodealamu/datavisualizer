import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from widgets import (title_of_chart_widget,xaxis_widget,yaxis_widget,size_widget,color_widget,text_widget,
                     hover_text_widget,symbol_widget,bins_widget,barmode_widget, boxmode_widget,
                     violinmode_widget,marginalx_widget,marginaly_widget, facetrow_widget,
                     facetcol_widget,logx_widget, logy_widget,linegroup_widget)

tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Visualizer", tab_id="tab-1"),
                dbc.Tab(label="About", tab_id="tab-2"),
                dbc.Tab(label="Tutorial videos", tab_id="tab-3"),
            ],
            id="tabs",
            active_tab="tab-1",
        ),
        html.Div(id="cont"),
    ]
)


tab1_content = dbc.Row(
                        [
                            dbc.Col(dbc.Card(body=True,
                                             id='graph-controls-card',
                                             children=[title_of_chart_widget,
                                                       xaxis_widget,yaxis_widget,size_widget,color_widget,text_widget,
                                                       hover_text_widget,symbol_widget,bins_widget,barmode_widget,
                                                       boxmode_widget, violinmode_widget,marginalx_widget,
                                                       marginaly_widget, facetrow_widget, facetcol_widget,
                                                       logx_widget, logy_widget,linegroup_widget
                                                       ]),width=3,),
                            dbc.Col(width=9,
                                    children=[dbc.Card(dcc.Graph(id='graph-area'),body=True),dbc.Card(html.Div())]),
                        ])

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.P("This app was created by Olabode Alamu, a Data scientist that believes everyone should be able to create beautiful charts without code.", className="card-text"),
            html.P("Check out the tutorial section for videos on how to use this tool. ",className="card-text"),
            html.P("The size of files which can be uploaded is limited by the amount of compute available for this site (which depends on how much I am willing to pay Heroku), if interested in sponsoring this site with compute resources please reach out to me.", className="card-text"),
        ]
    ),
    className="mt-3",
)

tab3_content = dbc.Card(body=True,style={'align':'center'},
                        children=[html.H3('Tutorial videos'),
                                  html.P("How to add Boxplots."),
                                  html.Iframe(src="https://www.youtube.com/embed/iamxgU1hIZ4",
                                              style={"height": "350px","width": "60%",'align':'center','title':"YouTube video player"}),
                                  html.P("How to add Scatter plots."),
                                  html.Iframe(src="https://www.youtube.com/embed/LkwHaSf4g7Y",
                                              style={"height": "350px", "width": "60%", 'align': 'center',
                                                     'title': "YouTube video player"})
                                  ])




