import markdown # Importation de la bibliothèque markdown pour la conversion
def convert(md_file, html_file): 
    """
    Convertit un fichier Markdown en fichier HTML.
    """
    # Lecture du fichier Markdown
    with open(md_file, "r", encoding="utf-8") as f: # Ouverture du fichier Markdown en lecture
        text = f.read() # Lecture du contenu du fichier

    # Conversion en HTML
    html = markdown.markdown(text) # Conversion du texte Markdown en HTML 

    # Ecriture du fichier HTML
    with open(html_file, "w", encoding="utf-8") as f: # Ouverture du fichier HTML en ecriture
        f.write(html) # Ecriture du contenu HTML dans le fichier de sortie

    print("Conversion terminée :", html_file) # Message de confirmation


# autorise de lancer le programme automatiquement depuis la ligne de commande (terminal)
if __name__ == "__main__": # Point d’entrée du script
    import sys # Importation du module sys pour accéder aux arguments de la ligne de commande
    if len(sys.argv) != 3: # Vérification du nombre d’arguments
        print("Usage: python md_to_html.py <input.md> <output.html>")# Message d’utilisation si le nombre d’arguments est incorrect
    else:# Conversion du fichier Markdown en HTML avec les arguments fournis
        convert(sys.argv[1], sys.argv[2]) # Appel de la fonction de conversion avec les fichiers spécifiés
    print(">>> SCRIPT md_to_html.py TERMINÉ") # Message de fin de script
    

