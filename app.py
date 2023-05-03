# app.py

import pandas as pd
from dash import html, Dash, dcc, Input, Output
import plotly.express as px

# INITIALIZATION AND DATA
# uses pandas to read csv files and query.
data = (
    pd.read_csv("pokemon.csv", index_col="pokedex_number", on_bad_lines="skip")
)
types = data["type1"].sort_values().unique()
japanese_names = data["japanese_name"].sort_values().unique()
names = data["name"].sort_values().unique()
  

# type colors:
colors = ['#a8b820', '#6f5848', '#7038f8', '#f9d030', '#ee99ac', '#c03128', '#f08030', '#a790f0', '#705898', '#78c84f','#e0c068','#99d8d8', '#a8a878', '#a040a0','#f85888','#b7a039','#b8b8d0', '#6890f0']

# for scatter plot:
scatter_colors = [ '#78c84f', '#f08030', '#6890f0', '#a8b820', '#a8a878', '#a040a0',  '#f9d030', '#e0c068',  '#ee99ac',  '#c03128', '#f85888', '#b7a039', '#705898', '#99d8d8',  '#7038f8',  '#6f5848', '#b8b8d0',  '#a790f0']
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

                html.Div([
                    html.H3(children="Special Attacks-and-Defense Stats Across Primary Types", className="card-description"),
                    dcc.RadioItems(
                        id="radio-mode", 
                        value="simple \t", 
                        options=["simple \t", "show speed"],
                        className="radio-mode"
                    ),
                    dcc.Graph(
                        id="scatter-plot",                    
                        config={"displayModeBar": False},
                        className="scatter-plot",
                        )
                    ], className="card",) ,
                


                
            ],
            className="wrapper",
        ),
        html.Div([    
            html.A("Made by Solveig <3", href='https://github.com/solveigua', target="_blank", className="footer-link"), 
        ], className="footer",
    ), 
    ]
)

# CALLBACKS

@app.callback(
    Output('dropdown', 'children'),
    Output('poke-search-chart', 'figure'),
    Output('scatter-plot', 'figure'),
    Input('poke-search', 'value'),
    Input('radio-mode', 'value')
)
def update_figure(name, mode):
    filtered_data = data[data.name==name].iloc[:, 1:19]
    y = filtered_data.values.flatten().tolist()
    try:
        jap_name = data[data.name==name]["japanese_name"].values[0]
    except:
        jap_name = ""
    
    figure = {
            "data": [
                {
                "x": types,
                "y": y,
                "type": "bar",
                "marker" : { "color" : colors }},
                ],
                         "layout": {
                                "title": {
                                    "text": "Efficiency against types:",
                                    "x": 0.05,
                                    "xanchor": "left",
                                },
                                "xaxis": {"fixedrange": True},
                                "yaxis": {"fixedrange": True},
                        },
    }

    if (mode == 'show speed'):
        size = "speed"
    else:
        size = None
    scatter = px.scatter(
                data, x="sp_defense",
                y="sp_attack", 
                size=size, 
                color="type1",
                color_discrete_sequence=scatter_colors,
                hover_name="name",
                labels={
                        "type1": "Primary Type",
                        "speed" : "Speed",
                        "sp_defense" : "Special Defense",
                        "sp_attack" : "Special Attack"}
        )
    scatter.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',)
    scatter.update_traces(marker=dict(line=dict(width=0)))

    return f'Viewing stats for {jap_name}', figure, scatter

# RUN
if __name__ == "__main__":
    app.run_server(debug=True)
