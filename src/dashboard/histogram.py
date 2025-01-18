# coding: iso-8859-1 -*-
import plotly.express as px
import pandas as pd
from src.utils.get_data import prepare_frequentation_bins

def update_main_graph(year):
    df_prepared = prepare_frequentation_bins(year)
    grouped_data = df_prepared["Tranche de fréquentation"].value_counts().sort_index()
    fig = px.bar(
        grouped_data,
        x=grouped_data.index,
        y=grouped_data.values,
        labels={'x': "Tranche de fréquentation", 'y': "Nombre de gares"},
        title=f"Nombre de gares par tranche de fréquentation en {year}"
    )
    return fig

def update_detail_graph(click_data, year):
    df_prepared = prepare_frequentation_bins(year)
    if click_data is None:
        return px.bar(title="Cliquez sur une barre pour voir les détails des gares")
    tranche = click_data['points'][0]['x']
    filtered_df = df_prepared[df_prepared["Tranche de fréquentation"] == tranche].sort_values(by=f"Total Voyageurs + Non voyageurs {year}", ascending=False)
    fig = px.bar(
        filtered_df,
        x="Nom de la gare",
        y=f"Total Voyageurs + Non voyageurs {year}",
        labels={"Nom de la gare": "Gare", f"Total Voyageurs + Non voyageurs {year}": "Voyageurs"},
        title=f"Détail des gares pour la tranche {tranche} en {year}",
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

