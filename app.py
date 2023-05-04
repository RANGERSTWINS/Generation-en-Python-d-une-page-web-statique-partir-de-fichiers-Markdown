import markdown
from flask import Flask, render_template

#convertir le fichier md en fichier html

with open("mon_fichier.md", "r") as fichier_md:
    contenu_md = fichier_md.read()

contenu_html = markdown.markdown(contenu_md)

with open("index.html", "w") as fichier_html:
    fichier_html.write(contenu_html)

#création du serveur local pour affichage du fichier html généré avec css et template

app = Flask(__name__)
app.static_folder = 'static'


#affichage du fichier markdown convertit en html
@app.route('/')
def index():
    
    with open('index.html', 'r') as f:
        content = f.read()

    return render_template('base.html', 
           content=content,
           title="Projet Tutoré"
           )

#affichage du fichier markdown de base
@app.route('/md')
def md():

    with open('mon_fichier.md','r') as fichier :
        content=fichier.read()
    
    return render_template('md.html',content=content)

#affichage du fichier html de base
@app.route('/html')
def html():

    with open('index.html','r') as fichier :
        content=fichier.read()
    
    return render_template('html.html',content=content)

if __name__ == '__main__':
    app.run()






