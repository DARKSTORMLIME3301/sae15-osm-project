# SAÉ 1.05 – Traiter des données (OpenStreetMap)

## Présentation du projet
Ce projet est réalisé dans le cadre de la SAÉ 1.05 « Traiter des données ».
L’objectif est de collecter des données depuis OpenStreetMap via des API,
de les traiter avec Python, puis de produire des fiches lisibles aux formats
Markdown et HTML.

Le projet est réalisé en binôme, avec une séparation claire des rôles
entre le traitement des données et l’affichage.

---

## Organisation du travail

### Personne A (Hussein) – Traitement des données (Python)
Responsable de :
- l’utilisation des API OpenStreetMap et Overpass
- la récupération des données (JSON)
- le traitement et les statistiques
- la génération automatique des fichiers Markdown

### Personne B (Emna) – Affichage et rendu visuel
Responsable de :
- la rédaction des fichiers Markdown
- la génération des pages HTML
- l’intégration d’une mini-carte OpenStreetMap
- l’organisation visuelle des fiches

Chaque personne travaille sur son propre ordinateur.
Les travaux sont ensuite regroupés dans une structure commune.

---

## Structure du projet
SAE15/
├── python/
│ ├── md_to_html.py
│ ├── fiche_osm.py
│ └── infos_locales.py
│
├── md/
│ └── fiche.md
│
├── html/
│ └── fiche.html
│
├── maps/
│ └── map.png
│
└── README.md


---

## Fonctionnalités prévues

- Conversion de fichiers Markdown en HTML
- Génération d’une fiche pour un point d’intérêt OpenStreetMap
- Récupération d’objets dans une zone géographique
- Calcul de statistiques simples
- Affichage clair et structuré des résultats

---

## État d’avancement
- Structure du projet définie
- Répartition des rôles effectuée
- Premiers fichiers Python, Markdown et HTML créés
