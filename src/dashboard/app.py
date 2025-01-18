import pandas as pd
from dash import Dash, dcc, html, Input, Output
from histogram import update_main_graph, update_detail_graph
from map import update_map
from get_data import load_data, prepare_frequentation_bins

# Charger les données
df, cdf = load_data()

# Créer l'application Dash
app = Dash(__name__)

# Disposition de l'application
app.layout = html.Div(style={
        'background-color': '#f0f4f8',  # Bleu-gris pour la page entière
        'padding': '20px',
        'min-height': '100vh',
    }, children=[
    html.H1("Analyse de fréquentation des gares SNCF", style={'text-align': 'center'}),

    # Barre de sélection au-dessus de tout
    html.Div([
        html.Label("Sélectionnez l'année :", style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='year-dropdown',
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
        # Colonne gauche pour les histogrammes
        html.Div([
            dcc.Graph(id='main-graph', style={'height': '300px'}),
            dcc.Graph(id='detail-graph', style={'height': '300px'}),
        ], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'}),

        # Colonne droite pour la carte et les informations
        html.Div([html.Div(id='map-container', children=[
            html.Iframe(id='map', srcDoc='', width='90%', height='600px'), 
            html.P(f"Cliquez sur les marqueurs pour afficher les détails.", style={'text-align': 'center', 'margin-top': '10px', 'font-size': '14px'}),
            html.P(id='summary-text', style={'text-align': 'center', 'margin-top': '10px', 'font-size': '14px'}),
        ])], style={'width': '50%', 'display': 'inline-block', 'verticalAlign': 'top'}),
    ]),

])

# Callbacks pour mettre à jour les éléments du frontend

# Callback pour mettre à jour le graphique principal
app.callback(
    Output('main-graph', 'figure'),
    Input('year-dropdown', 'value')
)(update_main_graph)

# Callback pour afficher les détails des gares
app.callback(
    Output('detail-graph', 'figure'),
    [Input('main-graph', 'clickData'), Input('year-dropdown', 'value')]
)(update_detail_graph)

# Callback pour mettre à jour la carte
app.callback(
    Output('map', 'srcDoc'),
    Input('year-dropdown', 'value')
)(update_map)


