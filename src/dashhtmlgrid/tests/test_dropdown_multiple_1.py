from dash import Dash, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

from test_data import get_input_data
from dropdown import get_drop_down_div
from plt_children import get_plt_go_layout, get_plt_trace
from html_layout import get_html_layout

# Initialize the app
app = Dash(__name__)
app.config.suppress_callback_exceptions = True

data_source = get_input_data()
df = data_source['df']

drop_down_div = get_drop_down_div(data_source=data_source)
app.layout = get_html_layout(drop_down_div)

trace_cfg_array = [{
    'data_source': df.copy(),
    'filter_column': 'stock',
    'filter_value': None,
    'x': 'Date',
    'y': 'value'
}, {
    'data_source': df.copy(),
    'filter_column': 'stock',
    'filter_value': None,
    'x': 'Date',
    'y': 'change'
}]


# Callback for Child Chart #1 (i.e. timeseries price)
@app.callback(Output('timeseries', 'figure'), [Input('stockselector', 'value')])
def update_timeseries(selected_dropdown_value):

    trace = []
    # Draw and append traces for each selected value
    for stock in selected_dropdown_value:
        trace_cfg = trace_cfg_array[0].copy()
        trace_cfg.update({'filter_value': stock})
        trace_value = get_plt_trace(trace_cfg)
        trace.append(trace_value)

    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    plt_range = [df[trace_cfg['x']].min(), df[trace_cfg['x']].max()]
    plt_go_layout = get_plt_go_layout(plt_range)

    figure = {
        'data': data,
        'layout': plt_go_layout,
    }

    return figure


# Callback for Child Chart #2 (i.e. Change Chart)
@app.callback(Output('change', 'figure'), [Input('stockselector', 'value')])
def update_change(selected_dropdown_value):
    ''' Draw traces of the feature 'change' based one the currently selected stocks '''
    trace = []
    # Draw and append traces for each selected value

    for stock in selected_dropdown_value:
        trace_cfg = trace_cfg_array[1].copy()
        trace_cfg.update({'filter_value': stock})
        trace_value = get_plt_trace(trace_cfg)
        trace.append(trace_value)

    traces = [trace]
    data = [val for sublist in traces for val in sublist]
    # Define Figure
    plt_range = [df[trace_cfg['x']].min(), df[trace_cfg['x']].max()]
    plt_go_layout = get_plt_go_layout(plt_range)

    figure = {
        'data': data,
        'layout': plt_go_layout,
    }

    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
