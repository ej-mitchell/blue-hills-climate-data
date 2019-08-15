import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

app = dash.Dash()
df = pd.read_csv('data/1919_2019_global-monthly.csv')

month_numbers = {
    "January": "01", 
    "February": "02", 
    "March": "03", 
    "April": "04", 
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

month_dfs = {}

for month in month_numbers:
    is_month = df['DATE'].str.contains("-{}".format(month_numbers[month]), regex=False)
    month_dfs[month] = df[is_month]

cols = ["DX70","DX90","EMSN","EMXP","EMXT","SNOW","TAVG"]

app.layout = html.Div(children=[
    html.Div(children=[
        dcc.Dropdown(
            id='month',
            options=[{'label': i, 'value': month_dfs[i].to_json()} for i in month_dfs],
            value=month_dfs["January"].to_json()
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
            margin=go.layout.Margin(l=20, r=10, t=40, b=30)
        )

    }

if __name__ == '__main__':
    app.run_server(debug=True)