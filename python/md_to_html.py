import markdown

def convert(md_file, html_file):
    """
    Convertit un fichier Markdown en fichier HTML.
    """
    # قراءة ملف Markdown
    with open(md_file, "r", encoding="utf-8") as f:
        text = f.read()

    # تحويل Markdown إلى HTML
    html = markdown.markdown(text)

    # كتابة ملف HTML
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

    print("Conversion terminée :", html_file)


# يسمح بتشغيل الملف مباشرة
if __name__ == "__main__":
    convert("../md/parks_sfax.md", "../html/parks_sfax.html")
