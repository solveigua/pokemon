# app.py

import pandas as pd
from dash import Dash, dcc, html, Input, Output

# INITIALIZATION
# uses pandas to read csv files and query.
data = (
    pd.read_csv("pokemon.csv", index_col="pokedex_number", on_bad_lines="skip")
)
#print(data)
types = data["type1"].sort_values().unique()
japanese_names = data["japanese_name"].sort_values().unique()
names = data["name"].sort_values().unique()
#print(japanese_names)


# STYLESHEET config

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Sono&display=swap',
]


app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "pokémon index"
app._favicon = "favico.ico"
app.css.config.serve_locally = True


# LAYOUT

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Img(src=r"assets/images/raichu.png", className="header-icon"),
                html.H1(children="pokémon index", className="header-title"),
                html.P(children="Find the perfect Pokémon for your battle!", className="header-description"),
            ], className="header", style={'textAlign': 'center'}),
        html.Div(
            children=[
                 html.Div(
                    children= [
                     html.H3(children="Search for Pokémon ... ", className="card-description"),
                        dcc.Dropdown(
                            data["name"],
                            id="poke-search",
                            clearable=False,
                            searchable=True,
                            className="dropdown",
                        ),
                        html.Div(id="dropdown", className="selection-text"),
                        dcc.Graph(
                            id="poke-search-chart",
                            config={"displayModeBar":False},
                            ),
                    ],
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="speed-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                            {
                                "x": data["name"],
                                "y": data["speed"],
                                "type": "lines", # bar
                            },
                        ],
                        "layout": {
                                "title": {
                                    "text": "Speed per pokemon",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["purple"],
                        },
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="attack-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                            {
                                "x": data["name"],
                                "y": data["sp_attack"],
                                "type": "bar"
                            },
                        ],
                        "layout": {
                                "title": {
                                    "text": "Sp. attack per pokemon",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": False},
                                "yaxis": {"fixedrange": True},
                                "colorway": ["#f5bb1c"],
                        },
                        },
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

# CALLBACKS

@app.callback(
    Output('dropdown', 'children'),
    Output('poke-search-chart', 'figure'),
    Input('poke-search', 'value')
)
def update_figure(value):
    filtered_data = data[data.name==value].iloc[:, 1:18]
    y = filtered_data.values.flatten().tolist()
    try:
        jap_name = data[data.name==value]["japanese_name"].values[0]
    except:
        jap_name = ""
    figure = {
            "data": [
                {
                "x": types,
                "y": y,
                "type": "bar",
                "marker" : { "color" : ['#a8b820', '#6f5848', '#7038f8', '#f9d030', '#ee99ac', '#c03128', '#f08030', '#a790f0', '#705898', '#78c84f','#e0c068','#99d8d8', '#a8a878', '#a040a0','#f85888','#b7a039','#b8b8d0']}},
                ],
                         "layout": {
                                "title": {
                                    "text": "Efficiency against types:",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": False},
                        },
    }
#     return f'You have selected {value}'
    return f'Viewing stats for {jap_name}', figure

# RUN
if __name__ == "__main__":
    app.run_server(debug=True)
