from dash import Dash
from dash.dependencies import Input, Output

from dashhtmlgrid.data_table import get_dash_table_from_df
from dashhtmlgrid.tests.example_data_table import get_example_data_table_df
from dashhtmlgrid.tests.test_data import get_input_data
from dashhtmlgrid.dropdown import get_drop_down_div
from dashhtmlgrid.html_layout import get_html_layout_data_table_call_back

app = Dash(__name__)

# Dashboard custom settings
dropdown_settings = [{
    "H2": 'DASH - STOCK PRICES',
    "p1": 'Visualising time series with Plotly - Dash.',
    "p2": 'Pick one or more options from the dropdown below.'
}]

table_setings = [{
    "H2": 'Example Table',
    "p1": 'Additional description for the table',
}]

layout_settings_custom = {
    'dropdown': dropdown_settings,
    'table': table_setings,
    'figure': None
}

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

html_layout = get_html_layout_data_table_call_back(drop_down_div,
                                                   layout_settings_custom)
app.layout = html_layout


# Callback for Table #1 (i.e. Example table)
@app.callback(Output('table_1_html', 'children'),
              [Input('stockselector', 'value')])
def update_table_1(selected_dropdown_value):

    df = get_example_data_table_df(selected_dropdown_value)
    dash_table = get_dash_table_from_df(df, table_data_id='table_1_data')

    return dash_table


if __name__ == '__main__':
    app.run_server(debug=True)
