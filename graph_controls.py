import dash_bootstrap_components as dbc
import dash_core_components as dcc
from widgets import create_dropdown, create_input_component
import dash_html_components as html


def create_formgroup(label, component_id, placeholder_text, drop_down_options=None,
                     widget_type='dropdown', html_id='symbol-html'):
    form_group = None
    if widget_type == 'dropdown':
        form_group = dbc.FormGroup(html.Div(id=html_id,
                                            children=[dbc.Label(label),
                                                      dcc.Dropdown(id=component_id,
                                                                   placeholder=placeholder_text,
                                                                   options=drop_down_options,
                                                                   value=None
                                                                   )
                                         ]))

    if widget_type == 'text_input':
        form_group = dbc.FormGroup(html.Div(id=html_id,
                                            children=[dbc.Label(label),
                                                      create_input_component(input_id=component_id,
                                                                             type_of_input='text',
                                                                             placeholder=placeholder_text,
                                                                             debounce=False)
                                         ]))

    if widget_type == 'number_input':
        form_group = dbc.FormGroup(html.Div(id=html_id,
                                            children=[dbc.Label(label),
                                                      create_input_component(input_id=component_id,
                                                                             type_of_input='number',
                                                                             placeholder=placeholder_text,
                                                                             debounce=False)
                                         ]))

    return form_group

