import markdown

#on ouvre notre fichier "test.md" en tant que fichier_md , on le lit  et on met le contenu dans la variable contenu_md.

with open("test.md", "r") as fichier_md:
    contenu_md = fichier_md.read()

#on convertit le contenu du fichier en html grâce au module markdown .
contenu_html = markdown.markdown(contenu_md)

#on ouvre/crée un second fichier "test.html" et on écrit le contenu traduit de notre premier fichier.
with open("test.html", "w") as fichier_html:
    fichier_html.write(contenu_html)
