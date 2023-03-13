# app.py

import pandas as pd
from dash import Dash, dcc, html

# INITIALIZATION
# uses pandas to read csv files and query.
data = (
    pd.read_csv("pokemon.csv", index_col="name", on_bad_lines="skip")
)
#print(data)

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
                    children=dcc.Graph(
                        id="speed-chart",
                        config={"displayModeBar": False},
                        figure={
                            "data": [
                            {
                                "x": data["pokedex_number"],
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
                                "x": data["pokedex_number"],
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
                                "yaxis": {"fixedrange": False},
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

# RUN
if __name__ == "__main__":
    app.run_server(debug=True)
