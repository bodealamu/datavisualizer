import dash_bootstrap_components as dbc
import dash_core_components as dcc
from widgets import create_dropdown, create_input_component


def create_formgroup(label, component_id, placeholder_text, drop_down_options=None, widget_type='dropdown'):
    form_group = None
    if widget_type == 'dropdown':
        if drop_down_options is not None:
            form_group = dbc.FormGroup([
                dbc.Label(label),
                create_dropdown(component_id, placeholder_text, drop_down_options)
            ])

    if widget_type == 'text_input':
        form_group = dbc.FormGroup([
            dbc.Label(label),
            create_input_component(input_id=component_id, type_of_input='text',
                                   placeholder=placeholder_text, debounce=False)

        ])

    if widget_type == 'number_input':
        form_group = dbc.FormGroup([
            dbc.Label(label),
            create_input_component(input_id=component_id, type_of_input='number',
                                   placeholder=placeholder_text, debounce=False)

        ])

    return form_group

