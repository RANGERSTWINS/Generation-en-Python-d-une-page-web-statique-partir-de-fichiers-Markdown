import markdown
from flask import Flask, render_template

#convertir le fichier md en fichier html

with open("mon_fichier.md", "r") as fichier_md:
    contenu_md = fichier_md.read()

contenu_html = markdown.markdown(contenu_md)

with open("index.html", "w") as fichier_html:
    fichier_html.write(contenu_html)

#création du serveur local pour affichage du fichier html généré 

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def index():
    
    with open('index.html', 'r') as f:
        content = f.read()

    return render_template('template.html', 
           content=content,
           title="Test"
           )

if __name__ == '__main__':
    app.run()






