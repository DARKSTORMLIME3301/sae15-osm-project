from md_to_html import convert
import requests

def get_dataset():
    url = "https://overpass-api.de/api/interpreter"

    query = """
    [out:json];
    node(5553036408);
    out;
    """

    response = requests.post(url, data=query)

    print("Status:", response.status_code)
    print("Text:", response.text[:200])

    if response.status_code != 200:
        raise Exception("Erreur Overpass API")

    return response.json()



def compute_statistics(data):
    """
    Calcule des statistiques simples sur les parcs.
    """
    elements = data.get("elements", [])

    total = len(elements)
    with_name = 0
    without_name = 0

    for element in elements:
        tags = element.get("tags", {})
        if "name" in tags:
            with_name += 1
        else:
            without_name += 1

    return {
        "total": total,
        "with_name": with_name,
        "without_name": without_name
    }


def dataset_to_md(data, stats, filename):
    """
    Génère un fichier Markdown listant les parcs et les statistiques.
    """
    elements = data.get("elements", [])

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Parcs et jardins à Sfax\n\n")

        f.write("## Statistiques\n")
        f.write(f"- Nombre total de parcs : {stats['total']}\n")
        f.write(f"- Parcs avec nom : {stats['with_name']}\n")
        f.write(f"- Parcs sans nom : {stats['without_name']}\n\n")

        f.write("## Liste des parcs\n")
        for element in elements:
            tags = element.get("tags", {})
            name = tags.get("name", "Parc sans nom")
            f.write(f"- {name}\n")


def infos_locales():
    """
    Fonction principale : dataset → stats → markdown → html.
    """
    data = get_dataset()
    stats = compute_statistics(data)

    md_file = "../markdown/parks_sfax.md"
    html_file = "../html/parks_sfax.html"

    dataset_to_md(data, stats, md_file)
    convert(md_file, html_file)

    print("Fichier Markdown et HTML générés avec succès.")


if __name__ == "__main__":
    infos_locales()

