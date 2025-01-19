# Dashboard fréquentation des gares SNCF

## Objectif
Nous souhaitions analyser la fréquentation des gares SNCF afin de connaitre son évolution avec le temps et les disparités de la fréquentation des différentes gares en france. 

## User guide
1. Clonez le dépôt : $ git clone https://github.com/ESIEECourses/myproject-keveen-florian.git
2. Se déplacer dans le dossier crée : $ cd myproject-keveen-florian
3. Installez les modules : $ pip install -r requirements.txt
4. Exécutez l'application : $ python main.py
5. Accédez au dashboard en ouvrant votre navigateur et en visitant http://127.0.0.1:8051/.

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
- En cartographiant la fréquentation des différentes gares, nous avons constaté que la SNCF couvre l'ensemble de la France métropolitaine. Cependant, l'analyse révèle une forte concentration de gares et de voyageurs en Île-de-France. Cette région, en raison de sa densité de population et de son activité économique, représente une part significative du trafic ferroviaire national.

- L'histogramme de fréquentation des gares a mis en évidence que la Gare du Nord est de loin la plus fréquentée, avec 226 millions de voyageurs en 2023. Elle dépasse largement la Gare Saint-Lazare, qui se positionne en deuxième place avec 110 millions de voyageurs. Cette domination de la Gare du Nord n'est pas un phénomène récent, mais une tendance stable observée depuis plusieurs années.

- L'analyse des données historiques montre que la fréquentation des gares SNCF reste globalement stable d'une année à l'autre. Une exception notable est l'année 2020, où la fréquentation a chuté drastiquement dans toutes les gares, conséquence directe des confinements liés à la pandémie de COVID-19. Cette baisse sans précédent illustre l'impact significatif des restrictions sanitaires sur la mobilité des voyageurs.

### Conclusions générales : 
La SNCF joue un rôle clé dans le transport à travers toute la France, avec une forte dominance de l'Île-de-France.
La Gare du Nord, en tant que point stratégique, reste incontestablement en tête des fréquentations.
Les fluctuations exceptionnelles de 2020 rappellent la vulnérabilité des transports publics face aux crises globales, mais aussi leur capacité à retrouver des niveaux de fréquentation élevés en période de normalité.

## Copyrights
Certaines parties des docstrings, ainsi que des extraits de code, ont été générées avec l'aide de ChatGPT, un modèle de langage développé par OpenAI. L'utilisation de cet outil a permis de gagner du temps et d'optimiser la clarté du contenu.
Néanmoins, nous déclarons sur l’honneur que la grande majorité du code a été conçu et écrit par nous même, Keveen BOUENDJA & Florian BOZEL . 
