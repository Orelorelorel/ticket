from flask import Flask,render_template, request, send_file, redirect, url_for, make_response, jsonify
from testpassword import extract_password_v2
from testpassword import create_html_dataframes
from testpassword import save_dataframes_to_txt
import os
import requests

app = Flask(__name__)

services = ["Playout", "Audio tech", "Core Tech", "MAM/PostProd"]
host = "http://192.168.1.26:3000/"

content = [
        {
            "title" : "Titre du ticket 1",
            "keyword" : "Afficher les keywords 1",
            "paragraph" : "Paragraphe 1",
            "service" : 'playout'
        },
        {
            "title" : "Titre du ticket 2",
            "keyword" : "Afficher les keywords 2",
            "paragraph" : "Paragraphe 2",
            "service" : 'playout'
        },
        {
            "title" : "Titre du ticket 3",
            "keyword" : "Afficher les keywords 3",
            "paragraph" : "Paragraphe 3",
            "service" : 'Audio tech'
        },
        {
            "title" : "Titre du ticket 4",
            "keyword" : "Afficher les keywords 4",
            "paragraph" : "Paragraphe 4",
            "service" : 'Core Tech'
        },
        {
            "title" : "Titre du ticket 5",
            "keyword" : "Afficher les keywords 5",
            "paragraph" : "Paragraphe 5",
            "service" : 'MAM/PostProd'
        }

    ]


@app.route("/")
def ticket():
    return render_template("index.html", content=content, services=services)

@app.route("/alltickets")
def alltickets():
    service = "All tickets"
    return render_template('alltickets.html',content=content, service = service)

@app.route("/")
def index():
    return render_template("index.html", content=content, services=services)

@app.route("/playout")
def playout_ticket():
    filter_content = [item for item in content if item["service"] == "playout"]
    service = "Playout"
    return render_template("playout.html",content=filter_content, service = service)

@app.route("/audiotech")
def audiotech_ticket():
    filter_content = [item for item in content if item["service"] == "Audio tech"]
    service = "Audio Tech"
    return render_template("audiotech.html",content=filter_content, service = service)

@app.route("/coretech")
def coretech_ticket():
    filter_content = [item for item in content if item["service"] == "Core Tech"]
    service = "Core tech"
    return render_template("coretech.html",content=filter_content, service = service)

@app.route("/mampostprod")
def mam_ticket():
    filter_content = [item for item in content if item["service"] == "MAM/PostProd"]
    service = "Mam / Post prod"
    return render_template("mampostprod.html",content=filter_content, service = service)


@app.route('/password_v4', methods=['GET', 'POST'])
def show_dataframes2():
    html_dataframes = {}
    txt_content = None

    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = uploaded_file.filename
        uploaded_file.save(filename)

        dataframes = extract_password_v2(filename)

        save_dataframes_to_txt(dataframes, 'data.txt')

        html_dataframes = create_html_dataframes(dataframes)

        os.remove(filename)

    # Vérifiez si le fichier texte existe
    if os.path.exists('data.txt'):
        # Lire le contenu du fichier
        with open('data.txt', 'r') as file:
            txt_content = file.read()

    return render_template('dataframestxt.html', dataframes=html_dataframes, txt_content=txt_content)

@app.route('/download_txt', methods=['GET'])
def download_txt():
    # Check if the data.txt file exists
    if os.path.exists('data.txt'):
        # Chemin vers le fichier texte généré
        txt_file = 'data.txt'
        # Nom de fichier à afficher lors du téléchargement
        download_filename = 'data.txt'

        # Créer une réponse avec le fichier en tant que pièce jointe
        response = make_response(send_file(txt_file))
        response.headers['Content-Disposition'] = f'attachment; filename="{download_filename}"'
        return response
    else:
        # Si le fichier data.txt n'existe pas, redirige vers la page d'origine
        return redirect(url_for('show_dataframes2'))


@app.route('/packagepath')
def packagepath():
    return render_template('packagepath.html')

@app.route('/search', methods=['POST'])
def search():
    destination = request.form['destination']
    headers = {}
    results = []

    while destination:
        url = "http://nhnbncsapi.discovery.com:8080/packager/v1/tally/destination/" + str(destination)
        response = requests.get(url, headers=headers)
        response_json = response.json()

        # Récupérer les informations nécessaires
        languages = []
        for language in response_json.get('Languages', []):
            languages.append({
                'index': language.get('index', ''),
                'type': language.get('type', ''),
                'tag': language.get('tag', '')
            })

        result = {
            'destination': destination,
            'source_package': response_json.get('Source_Package'),
            'languages': languages
        }
        results.append(result)

        destination = response_json.get('Source_Package')

    # Inverser l'ordre des résultats
    results.reverse()

    return render_template('search.html', results=results)

if __name__ == "__main__":
    app.run(host="192.168.1.26", port=5000, debug=True)
