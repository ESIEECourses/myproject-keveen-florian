# Dashboard fréquentation des gares SNCF

## Objectif
Nous souhaitions analyser la fréquentation des gares SNCF afin de savoir quelles sont les gares les plus fréquenter ainsi que les différences de fréquentation entre les différentes gares et l'évolution de cette fréquentation avec le temps.

## User guide
1. Clonez le dépôt : `git clone https://github.com/ESIEECourses/myproject-keveen-florian.git`
2. Installez les modules : `pip install -r requirements.txt`
3. Exécutez l'application : `python main.py`
4. Accédez au dashboard en ouvrant votre navigateur et en visitant http://127.0.0.1:8051/.

## Data
Nous utilisons les données officielles disponibles sur le site de la sncf 'ressources.data.sncf.com' : 

- Ce jeu de données nous donne les noms et positions géographiques de chaque gare sncf. 
'https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/liste-des-gares/exports/csv?lang=fr&timezone=Europe%2FParis&use_labels=true&delimiter=%3B'

- Ce jeu de données nous donne la fréquententation de chaque gare pour les années 2015 à 2023.
'https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/frequentation-gares/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B'

## Developper Guide
### Structure du Projet :

- `main.py`: Contient la classe principale `Main` qui lance l'application Dash.
- `config.py`:  Contient les constantes et les configurations globales.
- `requirements.txt`:  Liste des modules nécessaires pour exécuter le projet.
- `README.md`: Documentation générale sur le projet.

- `src/utils/`: Ce répertoire regroupe les fonctions pour le traitement des données.
- `get_data.py`: Charge et prépare les données des gares SNCF.

- `src/dashboard/`: Contient les fichiers pour la création de la carte et des histogrammes.
- `map.py`: Crée une carte des gares SNCF.
- `histogram.py`: Crée un histogramme de la fréquentation des gares SNCF.

- `data/`: Contient les données des gares SNCF.

### Modifications si besoin :
- Pour changer le port du serveur local, il suffit de modifier la variable `PORT` dans le fichier config.py.
- Pour changer les données des gares SNCF, il suffit de mettre à jour les url dans le fichier config.py.
- Pour changer les tranches de fréquentation, il suffit de modifier les variables `BINS` et `LABELS` dans le fichier config.py.

## Rapport d'analyse

En mettant sur une carte les fréquentations des différentes gares, nous avons remarqué que la totalité de la France métropolitaine est deservi par la sncf, cependant il y a une forte concentrations de gares et de voyageurs en Ile de France. L'histogramme nous a fait remarqué que la gare du nord est la plus fréquentée et de loin, avec 226 millions de voyageurs en 2023 comparée à St lazare qui arrive en 2eme position avec 110 millions. Cette domination existe depuis des années. La conclusion que l'on tire est que les gares SNCF ont globalement la meme fréquentation chaque année, exeptée en 2020 ou la fréquentation de toutes les gares a baissé drastiquement, ceci est probablement à dûe au confinement.

## Copyrights
Certaines parties des docstrings, ainsi que des extraits de code, ont été générées avec l'aide de ChatGPT, un modèle de langage développé par OpenAI. L'utilisation de cet outil a permis de gagner du temps et d'optimiser la clarté du contenu.
Néanmoins, nous déclarons sur l’honneur que la grande majorité du code a été conçu et écrit par nous même, Keveen BOUENDJA & Florian BOZEL . 
