from md_to_html import convert # Importation de la fonction de conversion Markdown → HTML
import requests # Importation de la bibliothèque requests pour les requêtes HTTP

def get_dataset():# Récupération du dataset des parcs et jardins à Sfax via l’API Overpass
    url = "https://overpass-api.de/api/interpreter" # URL de l’API Overpass

# Requête Overpass pour obtenir les parcs et jardins à Sfax
    query = """
    [out:json][timeout:25];
    // fetch area “sfax” to search in
    {{geocodeArea:sfax}}->.searchArea;
    nwr["leisure"="park"](area.searchArea);
    out geom;

    response = requests.post(url, data=query) # Envoi de la requête POST à l’API Overpass

    print("Status:", response.status_code)# Debug: afficher le code de statut HTTP
    print("Text:", response.text[:200])# Debug: afficher les premiers 200 caractères de la réponse

    if response.status_code != 200:# Vérification du code de statut HTTP
        raise Exception("Erreur Overpass API") # Gestion des erreurs de l’API

    return response.json()# Retour des données JSON récupérées



def compute_statistics(data): 
    """
    Calcule des statistiques simples sur les parcs.
    """
    elements = data.get("elements", [])# Récupération de la liste des éléments

    total = len(elements) # Nombre total de parcs
    with_name = 0 
    without_name = 0 

    for element in elements:# Parcours des éléments pour compter les noms
        tags = element.get("tags", {})# Récupération des tags de l’élément
        if "name" in tags:# Vérification de la présence du tag "name"
            with_name += 1# Incrémentation du compteur de parcs avec nom
        else:# Sinon
            without_name += 1# Incrémentation du compteur de parcs sans nom

    return {# Retour des statistiques sous forme de dictionnaire
        "total": total,# Nombre total de parcs
        "with_name": with_name,# Nombre de parcs avec nom
        "without_name": without_name# Nombre de parcs sans nom
    }


def dataset_to_md(data, stats, filename):
    """
    Génère un fichier Markdown listant les parcs et les statistiques.
    """
    elements = data.get("elements", [])# Récupération de la liste des éléments

    with open(filename, "w", encoding="utf-8") as f:# Ouverture du fichier en écriture
        f.write("# Parcs et jardins à Sfax\n\n")# Titre principal

        f.write("## Statistiques\n") # Sous-titre pour les statistiques
        f.write(f"- Nombre total de parcs : {stats['total']}\n") # Ecriture du nombre total de parcs
        f.write(f"- Parcs avec nom : {stats['with_name']}\n") # Ecriture du nombre de parcs avec nom
        f.write(f"- Parcs sans nom : {stats['without_name']}\n\n") # Ecriture du nombre de parcs sans nom

        f.write("## Liste des parcs\n") # Sous-titre pour la liste des parcs
        for element in elements: # Parcours des éléments pour lister les parcs
            tags = element.get("tags", {}) # Récupération des tags de l’élément
            name = tags.get("name", "Parc sans nom") # Récupération du nom du parc
            f.write(f"- {name}\n") # Ecriture du nom du parc dans la liste


def infos_locales():
    """
    Fonction principale : dataset → stats → markdown → html.
    """
    data = get_dataset() # Récupération du dataset
    stats = compute_statistics(data) # Calcul des statistiques

    md_file = "../markdown/parks_sfax.md" # Chemin du fichier Markdown à générer
    html_file = "../html/parks_sfax.html" # Chemin du fichier HTML à générer

    dataset_to_md(data, stats, md_file) # Génération du fichier Markdown
    convert(md_file, html_file) # Conversion du fichier Markdown en HTML

    print("Fichier Markdown et HTML générés avec succès.") # Message de succès


if __name__ == "__main__": # Point d’entrée du script
    infos_locales() # Appel de la fonction principale

