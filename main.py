from flask import Flask,render_template

app = Flask(__name__)

services = ["Playout", "Audio tech", "Core Tech", "MAM/PostProd"]


content = [
    {
    "title" : "Titre du ticket",
    "keyword" : "Afficher les keywords",
    "paragraph" : "Paragraphe"
},
    {
    "title" : "Titre du ticket",
    "keyword" : "Afficher les keywords",
    "paragraph" : "Paragraphe"
},
    {
    "title" : "Titre du ticket",
    "keyword" : "Afficher les keywords",
    "paragraph" : "Paragraphe"
},
    {
    "title" : "Titre du ticket",
    "keyword" : "Afficher les keywords",
    "paragraph" : "Paragraphe"
},
{
    "title" : "Titre du ticket",
    "keyword" : "Afficher les keywords",
    "paragraph" : "Paragraphe"
},
{
    "title" : "Titre du ticket",
    "keyword" : "Afficher les keywords",
    "paragraph" : "Paragraphe"
},
{
    "title" : "Titre du ticket",
    "keyword" : "Afficher les keywords",
    "paragraph" : "Paragraphe"
}
]

@app.route("/")
def ticket():
    return render_template("index.html", content=content, services=services)

if __name__ == "__main__":
    app.run(debug=True)
