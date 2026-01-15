import markdown
def convert(md_file, html_file):
    """
    Convertit un fichier Markdown en fichier HTML.
    """
    # lire fichier markdown 
    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()

    # convertir markdown a html 
    html = markdown.markdown(text)

    # ecrire fichier html 
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

    print("Conversion terminée :", html_file)


# autorise de lancer le programme automatiquement depuis la ligne de commande (terminal)
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python md_to_html.py <input.md> <output.html>")
    else:
        convert(sys.argv[1], sys.argv[2])
    print(">>> SCRIPT md_to_html.py TERMINÉ")
    

