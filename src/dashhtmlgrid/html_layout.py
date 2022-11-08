import pandas as pd

from dash import html, dcc
from dashhtmlgrid.plt_children import plt_setting
from dashhtmlgrid.tests.data_table import get_dash_table_from_df

# Layout settings
#TODO refactor using array configuration & indexes
div_text = {
    "H2": 'DASH - STOCK PRICES',
    "p1": 'Visualising time series with Plotly - Dash.',
    "p2": 'Pick one or more options from the dropdown below.'
}

table_div_text = {
    "H2": 'Example Table',
    "p1": 'Additional description for the table',
}


def get_html_layout_multipe_1(drop_down_div):

    plt_children_html = get_plt_children_html()

    html_layout = html.Div(children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2(div_text["H2"]),
                                  html.P(div_text["p1"]),
                                  html.P(div_text["p2"]),
                                  html.Div(drop_down_div)
                              ]),
                     html.Div([
                         html.H4(table_div_text["H2"]),
                         html.P(table_div_text["p1"]),
                         html.P(id='election_data_table_out'),
                         get_dash_table_from_df(df=pd.DataFrame())
                     ]),
                     html.Div(className=plt_setting['html_className'],
                              children=plt_children_html)
                 ])
    ])

    return html_layout


#TODO refactor using array configuration & indexes
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


def get_html_layout_data_table_call_back(drop_down_div):

    html_layout = html.Div(children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls',
                              children=[
                                  html.H2(div_text["H2"]),
                                  html.P(div_text["p1"]),
                                  html.P(div_text["p2"]),
                                  html.Div(drop_down_div)
                              ]),
                     html.Div([
                         html.H4(table_div_text["H2"]),
                         html.P(table_div_text["p1"]),
                         html.P(id='election_data_table_out'),
                         get_dash_table_from_df(df=pd.DataFrame())
                     ]),
                 ])
    ])

    return html_layout
