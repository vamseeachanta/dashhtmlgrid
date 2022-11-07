from lib2to3.pgen2.pgen import DFAState
import plotly.graph_objects as go

plt_setting = {
    'html_className':
        'eight columns div-for-charts',
    'id': ['timeseries', 'change'],
    'color_list': [[
        "#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'
    ], ["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056']]
}


def get_plt_trace(cfg):
    df = cfg['data_source']
    plt_trace = go.Scatter(
        x=df[df[cfg['filter_column']] == cfg['filter_value']][cfg['x']],
        y=df[df[cfg['filter_column']] == cfg['filter_value']][cfg['y']],
        mode='lines',
        opacity=0.7,
        name=cfg['filter_value'],
        textposition='bottom center')

    return plt_trace


trace_cfg_array = [{
    'data_source': None,
    'filter_column': 'stock',
    'filter_value': None,
    'x': 'Date',
    'y': 'value'
}, {
    'data_source': None,
    'filter_column': 'stock',
    'filter_value': None,
    'x': 'Date',
    'y': 'change'
}]


#TODO Parametrize the chart settings further
def get_plt_go_layout(plt_range):
    plt_go_layout = []

    plt_go_layout = go.Layout(
        colorway=plt_setting['color_list'][1],
        template='plotly_white',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        margin={'t': 50},
        height=250,
        hovermode='x',
        autosize=True,
        title={
            'text': 'Daily Change',
            'font': {
                'color': 'black'
            },
            'x': 0.5
        },
        xaxis={
            'showticklabels': False,
            'range': plt_range
        },
    )

    return plt_go_layout


def get_figure_for_chart1(df, selected_dropdown_value):

    trace = []
    # Draw and append traces for each selected value
    for stock in selected_dropdown_value:
        trace_cfg = trace_cfg_array[0].copy()
        trace_cfg.update({'data_source': df, 'filter_value': stock})
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


def get_figure_for_chart2(df, selected_dropdown_value):
    ''' Draw traces of the feature 'change' based one the currently selected stocks '''
    trace = []
    # Draw and append traces for each selected value

    for stock in selected_dropdown_value:
        trace_cfg = trace_cfg_array[1].copy()
        trace_cfg.update({'data_source': df, 'filter_value': stock})
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
