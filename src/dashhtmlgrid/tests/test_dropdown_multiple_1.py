from dash import Dash, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

from dashhtmlgrid.tests.test_data import get_input_data
from dashhtmlgrid.dropdown import get_drop_down_div
from dashhtmlgrid.plt_children import get_figure_for_chart1, get_figure_for_chart2
from dashhtmlgrid.html_layout import get_html_layout_multipe_1
from dashhtmlgrid.tests.data_table import get_example_data_df, get_dash_table_from_df

# Initialize the app
app = Dash(__name__)
app.config.suppress_callback_exceptions = True

data_source = get_input_data()
df1 = data_source['df'].copy()
df2 = data_source['df'].copy()

drop_down_div = get_drop_down_div(data_source=data_source)
app.layout = get_html_layout_multipe_1(drop_down_div)


# Callback for Child Chart #1 (i.e. timeseries price)
@app.callback(Output('timeseries', 'figure'), [Input('stockselector', 'value')])
def update_timeseries(selected_dropdown_value):

    figure = get_figure_for_chart1(df1, selected_dropdown_value)

    return figure


# Callback for Child Chart #2 (i.e. Change Chart)
@app.callback(Output('change', 'figure'), [Input('stockselector', 'value')])
def update_change(selected_dropdown_value):

    figure = get_figure_for_chart2(df2, selected_dropdown_value)

    return figure


# Callback for Table #1 (i.e. Example table)
@app.callback(Output('election_data_table_out', 'children'),
              [Input('stockselector', 'value')])
def update_table(selected_dropdown_value):

    df = get_example_data_df(selected_dropdown_value)
    table = get_dash_table_from_df(df)

    return table


if __name__ == '__main__':
    app.run_server(debug=True)
