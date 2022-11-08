from dash import Dash
from dash.dependencies import Input, Output

from dashhtmlgrid.tests.test_data import get_input_data
from dashhtmlgrid.dropdown import get_drop_down_div
from dashhtmlgrid.plt_children import get_figure_for_chart1, get_figure_for_chart2
from dashhtmlgrid.html_layout import get_html_layout_multiple_abstracted
from dashhtmlgrid.tests.data_table import get_example_data_table_df, get_dash_table_from_df

# Initialize the app
app = Dash(__name__)
app.config.suppress_callback_exceptions = True

grid_array = ['dropdown', 'table', 'chart', 'chart']

data_source = get_input_data()

drop_down_div = get_drop_down_div(data_source=data_source)
app.layout = get_html_layout_multiple_abstracted(drop_down_div)


@app.callback(Output('chart_1', 'figure'), [Input('stockselector', 'value')])
def update_chart_1(selected_dropdown_value):

    data_source = get_input_data()
    chart_1_df = data_source['df'].copy()
    figure = get_figure_for_chart1(chart_1_df, selected_dropdown_value)

    return figure


@app.callback(Output('chart_2', 'figure'), [Input('stockselector', 'value')])
def update_chart_2(selected_dropdown_value):

    data_source = get_input_data()
    chart_2_df = data_source['df'].copy()
    figure = get_figure_for_chart2(chart_2_df, selected_dropdown_value)

    return figure


# Callback for Table #1 (i.e. Example table)
@app.callback(Output('table_1_html', 'children'),
              [Input('stockselector', 'value')])
def update_table_1(selected_dropdown_value):

    df = get_example_data_table_df(selected_dropdown_value)
    table = get_dash_table_from_df(df, table_data_id='table_1_data')

    return table


if __name__ == '__main__':
    app.run_server(debug=True)
