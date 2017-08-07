import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, Event

import datetime


app = dash.Dash(__name__)


app.layout = html.Div(
    html.Div([
        html.H4('Test live feed'),
        html.Div(id='live-update-text'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000 # in milliseconds
        )
    ])
)

@app.callback(Output('live-update-text', 'children'),
              events=[Event('interval-component', 'interval')])
def update_metrics():
    d = datetime.datetime.now()
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Time: {0}'.format(d), style=style)
    ]


if __name__ == '__main__':
    app.run_server()