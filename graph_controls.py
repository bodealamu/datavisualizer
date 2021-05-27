import dash_bootstrap_components as dbc
import dash_core_components as dcc


def create_dropdown(dropdown_id, placeholder_text, options):
    dropdown = dcc.Dropdown(id=dropdown_id,
                         placeholder=placeholder_text,
                            options=options
                         )
    return dropdown


def create_formgroup(label,dropdown_id, placeholder_text, options):
    formgroup = dbc.FormGroup([
        dbc.Label(label),
        create_dropdown(dropdown_id, placeholder_text, options)
    ])

    return formgroup

