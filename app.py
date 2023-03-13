# app.py

import pandas as pd
from dash import Dash, dcc, html

# INITIALIZATION
# uses pandas to read csv files and query.
data = (
    pd.read_csv("pokemon.csv", index_col="name", on_bad_lines="skip")
)
print(data)

app = Dash(__name__)

# LAYOUT

app.layout = html.Div(
    children=[
        html.H1(children="Pokemon index"),
        html.P(
            children=(
                "Find the perfect Pokémon for your battle!"
            ),
        ),
                dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["pokedex_number"],
                        "y": data["speed"],
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Speed"},
            },
        ),
    ]
)

# RUN
if __name__ == "__main__":
    app.run_server(debug=True)
