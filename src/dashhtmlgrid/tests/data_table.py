from dash import dash_table
import pandas as pd
from collections import OrderedDict


def get_example_data_df(selected_dropdown_value=None):
    data_election = OrderedDict([
        (
            "Date",
            [
                "July 12th, 2013 - July 25th, 2013",
                "July 12th, 2013 - August 25th, 2013",
                "July 12th, 2014 - August 25th, 2014",
            ],
        ),
        (
            "Election Polling Organization",
            ["The New York Times", "Pew Research", "The Washington Post"],
        ),
        ("Rep", [1, -20, 3.512]),
        ("Dem", [10, 20, 30]),
        ("Ind", [2, 10924, 3912]),
        (
            "Region",
            [
                "Northern New York State to the Southern Appalachian Mountains",
                "Canada",
                "Southern Vermont",
            ],
        ),
    ])

    df = pd.DataFrame(data_election)
    return df


def get_dash_table_from_df(df):
    df_dash_table = dash_table.DataTable(
        id='election_data_input',
        data=df.to_dict('records'),
        columns=[{
            'id': c,
            'name': c
        } for c in df.columns],
        tooltip_data=[{
            column: {
                'value': str(value),
                'type': 'markdown'
            } for column, value in row.items()
        } for row in df.to_dict('records')],

    # Overflow into ellipsis
        style_cell={
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 0,
        },
        tooltip_delay=0,
        tooltip_duration=None)

    return df_dash_table
