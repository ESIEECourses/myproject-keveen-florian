URL_CSV = 'https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/frequentation-gares/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'
URL_COORD = 'https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/liste-des-gares/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B'

BINS = [0, 10000, 50000, 100000, 500000, 1000000, 20000000, float('inf')]
LABELS = ["0-10k", "10k-50k", "50k-100k", "100k-500k", "500k-1M", "1M-5M", "20M+"]

PORT = 8051


