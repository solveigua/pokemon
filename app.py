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
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Pokemon index"

# LAYOUT

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="👾", className="header-emoji"),
                html.H1(children="Pokemon index", className="header-title"),
                html.P(children="Find the perfect Pokémon for your battle!", className="header-description"),
            ], className="header"),
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
            ],
            className="wrapper",
        ),
    ]
)

# RUN
if __name__ == "__main__":
    app.run_server(debug=True)
