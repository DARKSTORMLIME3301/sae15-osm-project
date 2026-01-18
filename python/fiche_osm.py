from md_to_html import convert
import requests
import math
import sys

def node_to_md(data, filename):
    element = data["elements"][0]
    tags = element.get("tags", {})

    name = tags.get("name", "Nom non renseigné")
    amenity = tags.get("amenity", "Type inconnu")
    lat = element.get("lat")
    lon = element.get("lon")
    horaire_ouverture = tags.get("opening_hours", "Non renseigné")


    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Fiche OpenStreetMap\n\n")
        f.write("## Informations générales\n")
        f.write(f"- Nom : {name}\n")
        f.write(f"- Type : {amenity}\n")
        f.write(f"- Latitude : {lat}\n")
        f.write(f"- Longitude : {lon}\n")
        f.write(f"- Horaire d'ouverture : {horaire_ouverture}\n\n")

def get_node(osm_id):
    url = "https://overpass-api.de/api/interpreter"

    query = f"""
    [out:json];
    node({osm_id});
    out;
    """

    response = requests.post(url, data=query)

    if response.status_code != 200:
        raise Exception("Erreur Overpass API")

    return response.json()


def fiche_osm(osm_id):
    data = get_node(osm_id)

    if not data.get("elements"):
        print("Aucun node trouvé.")
        return

    md_file = "../markdown/fiche.md"
    html_file = "../html/fiche.html"

    node_to_md(data, md_file)
    convert(md_file, html_file)

    print("Fiche générée avec succès")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fiche_osm.py <osm_id>")
    else:
        fiche_osm(int(sys.argv[1]))
