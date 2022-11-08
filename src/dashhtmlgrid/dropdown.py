from dash import html, dcc


def get_full_dropdown_settings(dropdown_settings, dropdown_indx=0):

    full_dropdown_settings = {
        'multiple_flag': True,
        'html_className': 'div-for-dropdown',
        'id': 'dropdownselector',
        'className': 'dropdownselector',
        'options': dropdown_settings[dropdown_indx]['options'],
        'start_value': dropdown_settings[dropdown_indx]['options'][0]['label'],
        'style': {
            'backgroundColor': '#ffffff'
        },
        'html_style': {
            'color': '#000000'
        }
    }

    return full_dropdown_settings


def get_dropdown_div(dropdown_settings, dropdown_indx=0):

    full_dropdown_settings = get_full_dropdown_settings(dropdown_settings,
                                                        dropdown_indx=0)

    drop_down_div = html.Div(
        className=full_dropdown_settings['html_className'],
        children=[
            dcc.Dropdown(id=full_dropdown_settings['id'],
                         options=full_dropdown_settings['options'],
                         multi=full_dropdown_settings['multiple_flag'],
                         value=[full_dropdown_settings['start_value']],
                         style=full_dropdown_settings['style'],
                         className=full_dropdown_settings['className']),
        ],
        style=full_dropdown_settings['html_style'])

    return drop_down_div