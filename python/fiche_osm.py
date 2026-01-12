def node_to_md(data, filename):
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

def fiche_osm(osm_id):
    print("node_to_md appellee")
    data = get_node(osm_id)

    md_file = "SAE15-OSM-PROJET/markdown/fiche.md"
    html_file = "SAE15-OSM-PROJET/html/fiche.html"

    node_to_md(data, md_file)
    convert(md_file, html_file)
