from dash import Dash, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

from dashhtmlgrid.tests.test_data import get_input_data
from dashhtmlgrid.dropdown import get_drop_down_div
from dashhtmlgrid.plt_children import get_figure_for_chart1, get_figure_for_chart2
from dashhtmlgrid.html_layout import get_html_layout_multiple_chart_table
from dashhtmlgrid.tests.data_table import get_example_data_table_df, get_dash_table_from_df

# Define data
# figure dataframes
data_source = get_input_data()
figure_1_df = data_source['df'].copy()
figure_2_df = data_source['df'].copy()

# table dataframes

# Dashboard custom settings
grid_array = ['dropdown', 'table', 'figure', 'figure']

figure_settings = [{
    'id': 'figure_1',
    'plt_range': []
}, {
    'id': 'figure_2',
    'plt_range': []
}]

dropdown_settings = [{
    "H2": 'DASH - STOCK PRICES',
    "p1": 'Visualising time series with Plotly - Dash.',
    "p2": 'Pick one or more options from the dropdown below.'
}]

table_setings = [{
    "H2": 'Example Table',
    'id': 'table_1_data',
    "p1": 'Additional description for the table',
}]

layout_settings_custom = {
    'dropdown': dropdown_settings,
    'table': table_setings,
    'figure': figure_settings
}

# Initialize the app
app = Dash(__name__)
app.config.suppress_callback_exceptions = True

data_source = get_input_data()
df1 = data_source['df'].copy()
df2 = data_source['df'].copy()

drop_down_div = get_drop_down_div(data_source=data_source)
app.layout = get_html_layout_multiple_chart_table(drop_down_div,
                                                  layout_settings_custom)


# Callback for Child Chart #1 (i.e. timeseries price)
@app.callback(Output(figure_settings[0]['id'], 'figure'),
              [Input('stockselector', 'value')])
def update_figure_0(selected_dropdown_value):

    data_source = get_input_data()
    figure_0_df = data_source['df'].copy()
    figure = get_figure_for_chart1(figure_0_df, selected_dropdown_value)

    return figure


# Callback for Child Chart #2 (i.e. Change Chart)
@app.callback(Output(figure_settings[1]['id'], 'figure'),
              [Input('stockselector', 'value')])
def update_figure_1(selected_dropdown_value):

    data_source = get_input_data()
    figure_1_df = data_source['df'].copy()
    figure = get_figure_for_chart2(figure_1_df, selected_dropdown_value)

    return figure


# Callback for Table #1 (i.e. Example table)
@app.callback(Output('table_1_html', 'children'),
              [Input('stockselector', 'value')])
def update_table_0(selected_dropdown_value):

    table_1_df = get_example_data_table_df()
    table = get_dash_table_from_df(table_1_df,
                                   table_data_id=table_setings[0]['id'])

    return table


if __name__ == '__main__':
    app.run_server(debug=True)
