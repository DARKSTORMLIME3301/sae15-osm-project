print(">>> SCRIPT fiche_osm.py DEMARRÉ")
import requests
from md_to_html import convert
import markdown
def node_to_md(data, filename):
    print(">>> node_to_md APPELÉE")

    element = data["elements"][0]
    tags = element.get("tags", {})

    name = tags.get("name", "Nom non renseigné")
    amenity = tags.get("amenity", "Type inconnu")
    lat = element.get("lat")
    lon = element.get("lon")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Fiche OpenStreetMap\n\n")
        f.write("## Informations générales\n")
        f.write(f"- Nom : {name}\n")
        f.write(f"- Type : {amenity}\n")
        f.write(f"- Latitude : {lat}\n")
        f.write(f"- Longitude : {lon}\n")

def get_node(osm_id):
    url = f"https://www.openstreetmap.org/api/0.6/node/{osm_id}.json"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Erreur lors de la récupération des données OSM")

    return response.json()

def fiche_osm(osm_id):
    data = get_node(osm_id)

    md_file = "../markdown/fiche.md"
    html_file = "../html/fiche.html"

    node_to_md(data, md_file)
    convert(md_file, html_file)

    print("Fiche générée avec succès")


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python fiche_osm.py <osm_id>")
    else:
        fiche_osm(int(sys.argv[1]))
    print(">>> SCRIPT fiche_osm.py TERMINÉ")
    