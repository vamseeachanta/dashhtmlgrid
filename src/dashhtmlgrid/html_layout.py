import pandas as pd

from dash import html, dcc
from dashhtmlgrid.plt_children import plt_settings_generic
from dashhtmlgrid.tests.data_table import get_dash_table_from_df


def get_html_layout_multiple_abstracted(drop_down_div):

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
                         html.P(id='table_1_html'),
                         get_dash_table_from_df(df=pd.DataFrame(),
                                                table_data_id='table_1_data')
                     ]),
                     html.Div(className=plt_settings_generic['html_className'],
                              children=plt_children_html)
                 ])
    ])

    return html_layout


def get_html_layout_multiple_chart_table(drop_down_div, layout_settings_custom):

    div_text = layout_settings_custom['dropdown'][0]
    table_div_text = layout_settings_custom['table'][0]
    figure_settings_custom = layout_settings_custom['figure']
    plt_children_html = get_plt_children_html(figure_settings_custom)

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
                         html.P(id='table_1_html'),
                         get_dash_table_from_df(df=pd.DataFrame(),
                                                table_data_id='table_1_data')
                     ]),
                     html.Div(className=plt_settings_generic['html_className'],
                              children=plt_children_html)
                 ])
    ])

    return html_layout


def get_plt_children_html(figure_settings_custom):
    plt_children_html = [
        dcc.Graph(id='figure_1', config={'displayModeBar': False},
                  animate=True),
        dcc.Graph(id='figure_2', config={'displayModeBar': False},
                  animate=True),
    ]

    # for figure_index in range(0, len(figure_settings_custom)):
    #     dcc_graph_child = dcc.Graph(id=figure_settings_custom[figure_index]['id'],
    #                           config={'displayModeBar': False},
    #                           animate=True),
    #     plt_children_html.append(dcc_graph_child)

    return plt_children_html


def get_html_layout_data_table_call_back(drop_down_div, layout_settings_custom):

    div_text = layout_settings_custom['dropdown'][0]
    table_div_text = layout_settings_custom['table'][0]

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
                         html.P(id='table_1_html'),
                         get_dash_table_from_df(df=pd.DataFrame(),
                                                table_data_id='table_1_data')
                     ]),
                 ])
    ])

    return html_layout
