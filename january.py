import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

app = dash.Dash()
df = pd.read_csv('data/1919_2019_global-monthly.csv')

# TODO: Get this done more iteratively
is_january = df['DATE'].str.contains('-01', regex=False)
january_df = df[is_january]

is_february = df['DATE'].str.contains('-02', regex=False)
february_df = df[is_february]

cols = ["DX70","DX90","EMSN","EMXP","EMXT","SNOW","TAVG"]

app.layout = html.Div(children=[
    html.Div(children=[
        dcc.Dropdown(
            id='month',
            options=[{'label': 'January', 'value': january_df.to_json()}, {'label': 'February', 'value': february_df.to_json()}],
            value=january_df.to_json()
        ),
        dcc.Dropdown(
            id='stat',
            options=[{'label': i, 'value': i} for i in cols],
            value='EMXP'

        ),
        dcc.Graph(
            id='stats-graph'
        )
    ])
])

@app.callback(
    dash.dependencies.Output('stats-graph', 'figure'),
    [dash.dependencies.Input('stat', 'value'), dash.dependencies.Input('month', 'value')])
def select_stat(stat, month):
    df = pd.read_json(month)
    return {
        'data': [go.Bar(
            x = df['DATE'],
            y = df[stat]
        )],
        'layout': go.Layout(
            title='{}'.format(stat),
            showlegend=False,
            margin=go.layout.Margin(l=40, r=0, t=40, b=30)
        )

    }

if __name__ == '__main__':
    app.run_server(debug=True)