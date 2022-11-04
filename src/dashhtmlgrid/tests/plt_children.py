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