from dash import html, dcc
from plt_children import plt_setting

# Layout settings
html_text = {
    "H2": 'DASH - STOCK PRICES',
    "p1": 'Visualising time series with Plotly - Dash.',
    "p2": 'Pick one or more stocks from the dropdown below.'
}


def get_html_layout(drop_down_div):

    plt_children_html = get_plt_children_html()

    html_layout = html.Div(children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2(html_text["H2"]),
                                  html.P(html_text["p1"]),
                                  html.P(html_text["p2"]),
                                  html.Div(drop_down_div)
                              ]),
                     html.Div(className=plt_setting['html_className'],
                              children=plt_children_html)
                 ])
    ])

    return html_layout


#TODO Refactor using configuration
def get_plt_children_html():
    plt_children_html = [
        dcc.Graph(id=plt_setting['id'][0],
                  config={'displayModeBar': False},
                  animate=True),
        dcc.Graph(id=plt_setting['id'][1],
                  config={'displayModeBar': False},
                  animate=True),
    ]

    return plt_children_html
