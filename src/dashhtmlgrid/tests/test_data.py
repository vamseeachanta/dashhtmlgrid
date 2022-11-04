import pandas as pd

data_source = {
    'type': 'csv',
    'filename': 'src/dashhtmlgrid/tests/test_data/stockdata.csv'
}
data_definitions = {'x': 'Date', 'y': 'value'}
data_source.update({'data_definitions': data_definitions})


def get_input_data():

    if data_source['type'] == 'csv':
        df = pd.read_csv(data_source['filename'], index_col=0, parse_dates=True)
        df.index = pd.to_datetime(df['Date'])
        data_source['drop_down_options'] = get_options(df['stock'].unique())
        data_source['df'] = df
    else:
        raise ("Data source is undefined. Custom data reading is required")

    return data_source


def get_drop_down_options():

    if data_source['type'] == 'csv':
        df = pd.read_csv(data_source['filename'], index_col=0, parse_dates=True)
        df.index = pd.to_datetime(df['Date'])
        data_source['drop_down_options'] = get_options(df['stock'].unique())
        data_source['df'] = df
    else:
        raise ("Data source is undefined. Custom data reading is required")

    return data_source


def get_options(list_stocks):
    dict_list = []
    for i in list_stocks:
        dict_list.append({'label': i, 'value': i})

    return dict_list
