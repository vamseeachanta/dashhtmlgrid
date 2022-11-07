import pandas as pd

from dash import Dash
from dash.dependencies import Input, Output
from dash import html, dcc
import dash_bootstrap_components as dbc

from dashhtmlgrid.tests.data_table import get_example_data_df, get_dash_table_from_df
from dashhtmlgrid.tests.test_data import get_input_data
from dashhtmlgrid.dropdown import get_drop_down_div

app = Dash(__name__)

div_text = {
    "H2": 'DASH - STOCK PRICES',
    "p1": 'Visualising time series with Plotly - Dash.',
    "p2": 'Pick one or more options from the dropdown below.'
}

table_div_text = {
    "H2": 'Example Table',
    "p1": 'Additional description for the table',
}

data_source = get_input_data()
df1 = data_source['df'].copy()

drop_down_div = get_drop_down_div(data_source=data_source)

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

app.layout = html_layout


# Callback for Table #1 (i.e. Example table)
@app.callback(Output('election_data_table_out', 'children'),
              [Input('stockselector', 'value')])
def update_table(selected_dropdown_value):

    df = get_example_data_df(selected_dropdown_value)
    table = get_dash_table_from_df(df)

    return table


if __name__ == '__main__':
    app.run_server(debug=True)
