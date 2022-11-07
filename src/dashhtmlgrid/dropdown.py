from dash import html, dcc


def get_drop_down_settings(data_source):

    drop_down_settings = {
        'multiple_flag': True,
        'html_className': 'div-for-dropdown',
        'id': 'stockselector',
        'className': 'stockselector',
        'options': data_source['drop_down_options'],
        'start_value': data_source['drop_down_options'][0]['label'],
        'style': {
            'backgroundColor': '#ffffff'
        },
        'html_style': {
            'color': '#000000'
        }
    }

    return drop_down_settings


def get_drop_down_div(data_source):

    drop_down_settings = get_drop_down_settings(data_source)

    drop_down_div = html.Div(className=drop_down_settings['html_className'],
                             children=[
                                 dcc.Dropdown(
                                     id=drop_down_settings['id'],
                                     options=drop_down_settings['options'],
                                     multi=drop_down_settings['multiple_flag'],
                                     value=[drop_down_settings['start_value']],
                                     style=drop_down_settings['style'],
                                     className=drop_down_settings['className']),
                             ],
                             style=drop_down_settings['html_style'])

    return drop_down_div