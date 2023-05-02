from flask import Flask,render_template

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

if __name__ == "__main__":
    app.run(host="192.168.1.26", port=5000)
