# SAE 1.05 - Traiter des donnees (OpenStreetMap)

## NOMS & PRENOMS : ABDULRAHMAN Hussein & YOUSFI Emna 

## Introduction

Le projet SAE 1.05 a pour but de nous apprendre les bases de la programmation en Python en utilisant des donnees reelles.
Dans ce projet, nous utilisons les donnees d’OpenStreetMap grace a une API appelee Overpass API.
Le projet permet de recuperer des donnees, de les traiter en Python, puis de creer des fichiers Markdown et HTML.

Le projet est composé de trois scripts principaux : `fiche_osm.py`, `infos_locales.py` et `md_to_html.py`

## OpenStreetMap et les donnees

OpenStreetMap est une grande base de donnees geographiques ouverte.
On y trouve des informations comme les villes, les routes, les restaurants ou les parcs.

Les donnees sont organisees sous forme d’objets appeles nodes, ways et relations.
Chaque objet possede un identifiant et des tags comme `name`, `amenity` ou `leisure`.

## Script fiche_osm

Le fichier `fiche_osm.py` permet de creer une fiche pour un point precis d’OpenStreetMap a partir de son identifiant.

Le programme :

- envoie une requete a l’API Overpass avec l’ID du node,

- recupere les donnees au format JSON,

- extrait les informations principales,

- cree un fichier Markdown,

- puis le convertit en HTML.

Ce script m’a aide a comprendre la structure des donnees JSON et l’utilisation des fonctions en Python.

## Script infos_locales

Le fichier `infos_locales.py` permet de recuperer tous les objets d’un meme type dans une zone geographique donnee.
Dans mon projet, j’ai travaille sur les parcs (leisure=park) dans la ville de Sfax.

Le programme :

- recupere une liste d’objets,

- calcule des statistiques simples (nombre total, avec nom, sans nom),

- cree une fiche Markdown,

- puis la convertit en HTML.

Les resultats dependent des donnees disponibles dans OpenStreetMap.
Pour la ville de Sfax, les donnees sur les parcs sont peu nombreuses, ce qui peut donner des resultats faibles ou nuls.

## Script md_to_html

Le fichier md_to_html.py permet de convertir automatiquement les fichiers Markdown en fichiers HTML.
Cette fonction est utilisee dans les deux scripts `fiche_osm.py` et `infos_locales.py`.
Cela permet d’eviter de repeter le meme code et de mieux organiser le projet.

## Difficultes rencontrees

En tant que debutant en Python, j’ai rencontre plusieurs difficultes :

- comprendre la structure des donnees JSON,

- gerer les tags manquants,

- utiliser une API externe,

- comprendre que certaines donnees peuvent etre absentes dans OpenStreetMap.

Ces difficultes m’ont aide a mieux comprendre les limites des donnees et des API.

## Amelioration possible

Une amelioration possible du projet serait d’ajouter une carte avec un marqueur.
nous n'avons pas realise cette partie car nous n'avons  pas encore appris comment gerer les cartes.
on a  prefere de  concentrer sur les bases du projet et bien comprendre le code que nous avons ecrit.

## Conclusion

Ce projet nous a permis de mieux comprendre Python, les API et la manipulation de donnees reelles.
Meme si certaines donnees sont manquantes, le projet nous a  aide a progresser et a analyser les resultats obtenus

