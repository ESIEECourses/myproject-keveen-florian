# coding: iso-8859-1 -*-
import pandas as pd
import requests
from config import URL_CSV, URL_COORD, BINS, LABELS

def load_data():
    """
    T�l�charge et charge les donn�es de fr�quentation des gares et leurs coordonn�es.

    Returns:
        tuple: Deux DataFrames contenant respectivement les donn�es de fr�quentation et les coordonn�es des gares.
    """
    csv = 'data/raw/frequentation-gares.csv'
    coord_csv = 'data/raw/liste-des-gares.csv'
    try:
        response = requests.get(URL_CSV)
        with open(csv, 'wb') as f:
            f.write(response.content)

        response = requests.get(URL_COORD)
        with open(coord_csv, 'wb') as f:
            f.write(response.content)
    except :
        pass

    df = pd.read_csv(csv, sep=';')
    cdf = pd.read_csv(coord_csv, sep=';', on_bad_lines='skip')

    df['Code UIC'] = df['Code UIC'].astype(str).str.strip()
    cdf['CODE_UIC'] = cdf['CODE_UIC'].astype(str).str.strip()

    return df, cdf

def prepare_frequentation_bins(year):
    """
    Pr�pare les donn�es de fr�quentation en les groupant par tranches pour une ann�e donn�e.

    Args:
        year (int): Ann�e pour laquelle les tranches de fr�quentation doivent �tre calcul�es.

    Returns:
        DataFrame: Donn�es de fr�quentation avec une colonne suppl�mentaire pour les tranches de fr�quentation.
    """
    df, _ = load_data() 
    df["Tranche de fr�quentation"] = pd.cut(df[f"Total Voyageurs + Non voyageurs {year}"], bins=BINS, labels=LABELS, right=False)
    df.to_csv(f'data/cleaned/frequentation_tranche_{year}.csv', sep=';', index=False, encoding='utf-8')
    return df
