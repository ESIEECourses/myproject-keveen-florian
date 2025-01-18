import pandas as pd

# Charger les données
def load_data():
    url_csv = 'https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/frequentation-gares/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'
    url_coord = 'https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/liste-des-gares/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B'

    df = pd.read_csv(url_csv, sep=';')
    cdf = pd.read_csv(url_coord, sep=';', on_bad_lines='skip')

    df['Code UIC'] = df['Code UIC'].astype(str).str.strip()
    cdf['CODE_UIC'] = cdf['CODE_UIC'].astype(str).str.strip()

    return df, cdf

# Préparer les données pour les tranches de fréquentation
def prepare_frequentation_bins(year):
    df, _ = load_data()
    bins = [0, 10000, 50000, 100000, 500000, 1000000, 20000000, float('inf')]
    labels = ["0-10k", "10k-50k", "50k-100k", "100k-500k", "500k-1M", "1M-5M", "20M+"]
    
    df["Tranche de fréquentation"] = pd.cut(df[f"Total Voyageurs + Non voyageurs {year}"], bins=bins, labels=labels, right=False)
    
    return df
