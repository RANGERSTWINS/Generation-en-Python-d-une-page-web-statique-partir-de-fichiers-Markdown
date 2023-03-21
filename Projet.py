import markdown

with open("test.md", "r") as fichier_md:
    contenu_md = fichier_md.read()

contenu_html = markdown.markdown(contenu_md)

with open("test.html", "w") as fichier_html:
    fichier_html.write(contenu_html)
