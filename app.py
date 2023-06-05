from flask import Flask, render_template

def convert_md_to_html(md_file, html_file):
    # Ouvrir le fichier Markdown en mode lecture
    with open(md_file, 'r') as f:
        contenu_md = f.read()
    
    # Convertir le contenu Markdown en HTML
    html_content = ""
    lines = contenu_md.split("\n")

    for line in lines:
        # Gérer les balises spéciales Markdown
        
        # Titres
        if line.startswith("#"):
            level = line.count("#")
            line = line.strip("#").strip()
            html_content += f"<h{level}>{line}</h{level}>"
        
        # Paragraphes
        elif line.strip() != "":
            html_content += f"<p>{line}</p>"

        #Listes
        if line.startswith("-"):
            html_content += f"<ul> <li> {line} </li> </ul>"

        #> blockquote 
        if line.startswith(">"):
            html_content += f"<blockquote>{line}</blockquote>"

    # Écrire le contenu HTML dans le fichier
    with open(html_file, 'w') as f:
        f.write(html_content)

# Exemple d'utilisation
chemin = "Md/mon_fichier.md"
sortie = "Output/index.html"
convert_md_to_html(chemin, sortie)


app = Flask(__name__)
app.static_folder = 'static'


#affichage du fichier markdown convertit en html
@app.route('/')
def index():
    global sortie
    
    with open(sortie, 'r') as fichier:
        content = fichier.read()

    return render_template('base.html', 
           content=content,
           title="Projet Tutoré"
           )

#affichage du fichier markdown de base
@app.route('/md')
def md():

    global chemin 

    with open(chemin,'r') as fichier :
        content=fichier.read()
    
    return render_template('md.html',content=content)

#affichage du fichier html de base
@app.route('/html')
def html():
    global sortie

    with open(sortie,'r') as fichier :
        content=fichier.read()
    
    return render_template('html.html',content=content)

if __name__ == '__main__':
    app.run()






