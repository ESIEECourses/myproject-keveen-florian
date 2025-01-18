# coding: iso-8859-1 -*-
import folium
from folium.plugins import MarkerCluster, HeatMap
import pandas as pd
from src.utils.get_data import load_data

def create_map(year):
    """
    Créer une carte de France avec des marqueurs et une heatmap représentant le nombre de voyageurs et non-voyageurs pour l'année spécifiée.

    Args:
        year (int): L'année pour laquelle les données des voyageurs doivent être affichées.

    Returns:
        str: Contenu HTML de la carte générée.
    """
    df, cdf = load_data() 
    # Pour zoomer sur la France
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

    # On croise les deux dataframes pour avoir les coordonnées des gares qui ont le meme code UIC
    df[f'Total Voyageurs + Non voyageurs {year}'] = pd.to_numeric(df[f'Total Voyageurs + Non voyageurs {year}'], errors='coerce')
    matching_uic = df[df['Code UIC'].isin(cdf['CODE_UIC'])]
    marker_cluster = MarkerCluster().add_to(m)
    heatmap_data = []
    # Boucle sur ces gares pour les afficher sur la carte
    for index, row in matching_uic.iterrows():
        code_uic = row['Code UIC']
        geo_point = cdf[cdf['CODE_UIC'] == code_uic]['Geo Point']

        # On vérifie que la gare a bien des coordonnées 
        if not geo_point.empty:
            lat, lon = map(float, geo_point.values[0].split(','))
            folium.Marker(
                location=[lat, lon],
                popup=f"Gare: {row['Nom de la gare']}<br>Total Voyageurs + Non voyageurs {year}: {row[f'Total Voyageurs + Non voyageurs {year}']}",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(marker_cluster)

            # On ajoute les données pour la heatmap
            if not pd.isna(row[f'Total Voyageurs + Non voyageurs {year}']):
                heatmap_data.append([lat, lon, row[f'Total Voyageurs + Non voyageurs {year}']])

    HeatMap(heatmap_data, min_opacity=0.2, radius=10, blur=3).add_to(m)
    folium.LayerControl().add_to(m)
    map_filename = "carte_france_gares.html"
    m.save(map_filename)

    with open(map_filename, 'r') as f:
        return f.read()

