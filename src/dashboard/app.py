# coding: iso-8859-1 -*-
import pandas as pd
from dash import Dash, dcc, html, Input, Output
from .histogram import main_graph, detail_graph
from .map import create_map
from src.utils.get_data import load_data, prepare_frequentation_bins

df, cdf = load_data()

# Initalisation de l'application Dash
app = Dash(__name__)

# Mise en forme du dashboard
app.layout = html.Div(style={
        'background-color': '#f0f4f8',  
        'padding': '20px',
        'min-height': '100vh',
    }, children=[
    html.H1("Dashboard sur la fréquentation des gares SNCF", style={'text-align': 'center'}),
    html.H2("Le chargement de la carte peut prendre un certain temps en raison d'un grand nombre de marqueurs. De plus, si vous rencontrez une erreur au chargement du dashboard, veuillez rafraîchir la page.", style={'text-align': 'center'}),

    html.Div([
        html.Label("Sélectionnez l'année :", style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='year',
            options=[{'label': str(year), 'value': str(year)} for year in range(2015, 2024)],
            value='2023',
            style={'width': '50%', 'margin': '0 auto'},
        )
    ], style={'text-align': 'center', 'margin-bottom': '20px'}),

    html.Div(style={
                'background-color': 'white',
                'border': '2px solid #ccc',
                'border-radius': '10px',
                'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)',
                'height': '850px',
                'padding-top': '20px',
            }, children=[
        html.Div([
            dcc.Graph(id='main-graph', style={'height': '300px'}),
            dcc.Graph(id='detail-graph', style={'height': '300px'}),
        ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        html.Div([
            html.Div(id='map-container', children=[
                html.Iframe(id='map', srcDoc='', width='90%', height='600px'),  
                html.P(
                    f"Carte de la fréquentation des gares SNCF en France ainsi que leur position",
                    style={'text-align': 'center', 'margin-top': '10px', 'font-size': '20px'}
                ),
                html.P(
                    f"Cliquez sur les marqueurs pour afficher les détails. Cliquez sur le bouton en haut à droite de la carte pour choisir le mode de celle-ci.",
                    style={'text-align': 'center', 'margin-top': '10px', 'font-size': '15px'}
                ),
                html.P(
                    id='text',
                    style={'text-align': 'center', 'margin-top': '10px', 'font-size': '15px'}
                ),
            ]),
        ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    ]),
])

def insert_text(year):
    """
    Génère le texte pour le nombre total de voyageurs pour une année donnée et identifie la gare la plus fréquentée.

    Args:
        year (str): Année pour laquelle les données doivent être calculées.

    Returns:
        str: Texte incluant le nombre total de voyageurs et la gare la plus fréquentée.
    """
    df[f'Total Voyageurs + Non voyageurs {year}'] = pd.to_numeric(df[f'Total Voyageurs + Non voyageurs {year}'], errors='coerce')
    total_voyageurs = df[f'Total Voyageurs + Non voyageurs {year}'].sum()
    gare_max = df.loc[df[f'Total Voyageurs + Non voyageurs {year}'].idxmax()]
    gare_nom = gare_max['Nom de la gare']
    gare_voyageurs = gare_max[f'Total Voyageurs + Non voyageurs {year}']
    return f"Total Voyageurs + Non voyageurs {year}: {total_voyageurs:,} | Gare la plus fréquentée : {gare_nom} ({gare_voyageurs:,} voyageurs)"


# Mise à jour du graphique principal
app.callback(
    Output('main-graph', 'figure'),
    Input('year', 'value')
)(main_graph)

# Mise à jour du graphique détaillé
app.callback(
    Output('detail-graph', 'figure'),
    [Input('main-graph', 'clickData'), Input('year', 'value')]
)(detail_graph)

# Mise à jour de la carte
app.callback(
    Output('map', 'srcDoc'),
    Input('year', 'value')
)(create_map)

# Mise à jour du texte 
app.callback(
    Output('text', 'children'),
    Input('year', 'value')
)(insert_text)
