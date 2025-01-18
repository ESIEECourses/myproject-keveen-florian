# coding: iso-8859-1 -*-
import plotly.express as px
import pandas as pd
from src.utils.get_data import prepare_frequentation_bins

def main_graph(year):
    """
    Cr�er le graphique principal montrant le nombre de gares par tranche de fr�quentation pour une ann�e donn�e.

    Args:
        year (int): L'ann�e pour laquelle les donn�es doivent �tre affich�es.

    Returns:
        plotly.graph_objs._figure.Figure: Graphique en barres des gares par tranche de fr�quentation.
    """
    df_prepared = prepare_frequentation_bins(year)
    # On groupe les gares par tranche de fr�quentation
    grouped_data = df_prepared["Tranche de fr�quentation"].value_counts().sort_index()
    fig = px.bar(
        grouped_data,
        x=grouped_data.index,
        y=grouped_data.values,
        labels={'x': "Tranche de fr�quentation", 'y': "Nombre de gares"},
        title=f"Nombre de gares par tranche de fr�quentation en {year}"
    )
    return fig

def detail_graph(click_data, year):
    """
    Cr�er le graphique d�taill� montrant les gares pour une tranche de fr�quentation s�lectionn�e.

    Args:
        click_data (dict): Donn�es du clic sur une barre du graphique principal.
        year (int): L'ann�e pour laquelle les donn�es doivent �tre affich�es.

    Returns:
        plotly.graph_objs._figure.Figure: Graphique en barres d�taillant les gares pour la tranche s�lectionn�e.
    """
    df_prepared = prepare_frequentation_bins(year)
    # Si aucune barre n'est cliqu�e, on affiche un graph vide
    if click_data is None:
        return px.bar(title="Cliquez sur une barre pour voir les d�tails des gares")
    # On r�cup�re la tranche de fr�quentation s�lectionn�e pour afficher les gares correspondantes
    tranche = click_data['points'][0]['x']
    filtered_df = df_prepared[df_prepared["Tranche de fr�quentation"] == tranche].sort_values(by=f"Total Voyageurs + Non voyageurs {year}", ascending=False)
    fig = px.bar(
        filtered_df,
        x="Nom de la gare",
        y=f"Total Voyageurs + Non voyageurs {year}",
        labels={"Nom de la gare": "Barre de d�filement pour parcourir les gares", f"Total Voyageurs + Non voyageurs {year}": "Voyageurs"},
        title=f"D�tail des gares pour la tranche {tranche} en {year}",
    )
    fig.update_layout(
        height=500,
        xaxis=dict(
            tickangle=45,
            automargin=True,
            range=[0, 20],
            rangeslider=dict(visible=True)
        )
    )
    return fig

