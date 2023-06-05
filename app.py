import markdown
from flask import Flask, render_template

#convertir le fichier md en fichier html
def generation_html(chemin):

    print("Génération de la page Html ...")

    try :
        
        with open(chemin, "r") as fichier_md:
            contenu_md = fichier_md.read()

        contenu_html = markdown.markdown(contenu_md)

        with open("Output/index.html", "w") as fichier_html:
            fichier_html.write(contenu_html)

        print("Génération terminée ! ")

    except :
        print("Le fichier n existe pas . Recommencer")

nom_fichier = "Exemple"+".md"
chemin = "Md/"+nom_fichier
generation_html(chemin)

#création du serveur local pour affichage du fichier html généré avec css et template

app = Flask(__name__)
app.static_folder = 'static'


#affichage du fichier markdown convertit en html
@app.route('/')
def index():
    
    with open('Output/index.html', 'r') as fichier:
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

    with open('Output/index.html','r') as fichier :
        content=fichier.read()
    
    return render_template('html.html',content=content)

if __name__ == '__main__':
    app.run()






