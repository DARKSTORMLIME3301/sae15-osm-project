from md_to_html import convert
import requests
import sys


# Genere un fichier Markdown à partir des données d’un node OpenStreetMap
def node_to_md(data, filename):
    element = data["elements"][0] # Recuperation du premier element retourne par l’api (un seul node attendu)
    tags = element.get("tags", {}) # Recuperation des tags du node (informations descriptives)

    name = tags.get("name", "Nom non renseigné") # Recuperation du nom du node
    amenity = tags.get("amenity", "Type inconnu") 
    lat = element.get("lat") 
    lon = element.get("lon") 
    horaire_ouverture = tags.get("opening_hours", "Non renseigné") # Recuperation des horaires d’ouverture
 

    with open(filename, "w", encoding="utf-8") as f: # Ouverture du fichier en ecriture
        f.write("# Fiche OpenStreetMap\n\n") # Titre principal du document
        f.write("## Informations générales\n") 
        f.write(f"- Nom : {name}\n") 
        f.write(f"- Type : {amenity}\n") 
        f.write(f"- Latitude : {lat}\n") 
        f.write(f"- Longitude : {lon}\n")
        f.write(f"- Horaire d'ouverture : {horaire_ouverture}\n\n") 

def get_node(osm_id):# Recuperation des donnees d’un node OpenStreetMap via l’API Overpass
    url = "https://overpass-api.de/api/interpreter" 
# Requete Overpass pour obtenir le node avec l’ID specifie
    query = f""" 
    [out:json];
    node({osm_id}); 
    out;
    """

    response = requests.post(url, data=query) # Envoi de la requete POST a l’API Overpass

    if response.status_code != 200: # Verification du code de statut HTTP
        raise Exception("Erreur Overpass API") # Gestion des erreurs de l’API

    return response.json() 


def fiche_osm(osm_id): # Generation de la fiche Markdown et HTML pour un node OpenStreetMap
    data = get_node(osm_id) # Recuperation des donnees du node

    if not data.get("elements"): # Verification de la presence d’elements dans les donnees recuperees
        print("Aucun node trouvé.") 
        return 

    md_file = "../markdown/fiche.md" # Chemin du fichier Markdown a generer
    html_file = "../html/fiche.html" # Chemin du fichier HTML a generer

    node_to_md(data, md_file) # Generation du fichier Markdown a partir des donnees du node
    convert(md_file, html_file) # Conversion du fichier Markdown en HTML

    print("Fiche générée avec succès")


if __name__ == "__main__":# Point d’entree du script
    if len(sys.argv) != 2:# Verification du nombre d’arguments
        print("Usage: python fiche_osm.py <osm_id>")
    else:# Generation de la fiche pour l’ID OSM fourni en argument
        fiche_osm(int(sys.argv[1]))# Appel de la fonction principale avec l’ID OSM converti en entier
