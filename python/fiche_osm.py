from md_to_html import convert
import requests
import math
import sys


# Genere un fichier Markdown à partir des données d’un node OpenStreetMap
def node_to_md(data, filename):
    element = data["elements"][0] # Recuperation du premier element retourne par l’api (un seul node attendu)
    tags = element.get("tags", {}) # Recuperation des tags du node (informations descriptives)

    name = tags.get("name", "Nom non renseigné") # Recuperation du nom du node
    amenity = tags.get("amenity", "Type inconnu") # Recuperation du type d’equipement
    lat = element.get("lat") # Recuperation de la latitude
    lon = element.get("lon") # Recuperation de la longitude
    horaire_ouverture = tags.get("opening_hours", "Non renseigné") # Recuperation des horaires d’ouverture
 

    with open(filename, "w", encoding="utf-8") as f: # Ouverture du fichier en ecriture
        f.write("# Fiche OpenStreetMap\n\n") # Titre principal
        f.write("## Informations générales\n") # Sous-titre
        f.write(f"- Nom : {name}\n") # Ecriture du nom
        f.write(f"- Type : {amenity}\n") # Ecriture du type d’equipement
        f.write(f"- Latitude : {lat}\n") # Ecriture de la latitude
        f.write(f"- Longitude : {lon}\n")# Ecriture de la longitude
        f.write(f"- Horaire d'ouverture : {horaire_ouverture}\n\n") # Ecriture des horaires d’ouverture

def get_node(osm_id):# Recuperation des donnees d’un node OpenStreetMap via l’API Overpass
    url = "https://overpass-api.de/api/interpreter" # URL de l’API Overpass
    
# Requete Overpass pour obtenir le node avec l’ID specifie
    query = f""" 
    [out:json];
    node({osm_id}); 
    out;
    """

    response = requests.post(url, data=query) # Envoi de la requete POST a l’API Overpass

    if response.status_code != 200: # Verification du code de statut HTTP
        raise Exception("Erreur Overpass API") # Gestion des erreurs de l’API

    return response.json() # Retour des donnees JSON recuperees


def fiche_osm(osm_id): # Generation de la fiche Markdown et HTML pour un node OpenStreetMap
    data = get_node(osm_id) # Recuperation des donnees du node

    if not data.get("elements"): # Verification de la presence d’elements dans les donnees recuperees
        print("Aucun node trouvé.") # Message d’erreur si aucun node n’est trouve
        return # Arret de l’execution de la fonction

    md_file = "../markdown/fiche.md" # Chemin du fichier Markdown a generer
    html_file = "../html/fiche.html" # Chemin du fichier HTML a generer

    node_to_md(data, md_file) # Generation du fichier Markdown a partir des donnees du node
    convert(md_file, html_file) # Conversion du fichier Markdown en HTML

    print("Fiche générée avec succès") # Message de succes


if __name__ == "__main__":# Point d’entree du script
    if len(sys.argv) != 2:# Verification du nombre d’arguments
        print("Usage: python fiche_osm.py <osm_id>")# Message d’utilisation si le nombre d’arguments est incorrect
    else:# Generation de la fiche pour l’ID OSM fourni en argument
        fiche_osm(int(sys.argv[1]))# Appel de la fonction principale avec l’ID OSM converti en entier
