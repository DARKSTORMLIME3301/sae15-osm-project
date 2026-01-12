import requests

def infos_locales():
    """
    Récupère les parcs et jardins de la ville de Sfax via Overpass API.
    """
    url = "https://overpass-api.de/api/interpreter"

    query = """
    [out:json];
    area["name"="Sfax"]["boundary"="administrative"]->.a;
    node["leisure"="park"](area.a);
    out;
    """

    response = requests.post(url, data=query)
    data = response.json()

    print("Nombre de parcs trouvés :", len(data["elements"]))

    # afficher les 3 premiers noms (si موجودين)
    for element in data["elements"][:3]:
        tags = element.get("tags", {})
        name = tags.get("name", "Parc sans nom")
        print("-", name)


if __name__ == "__main__":
    infos_locales()
