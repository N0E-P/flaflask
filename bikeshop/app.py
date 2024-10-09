from flask import Flask, abort, render_template, request
import os
import json

TEMPLATES = "templates"

app = Flask(__name__, template_folder=TEMPLATES)

@app.route("/")
@app.route("/home")
def hello():
    print("home")
    return render_template("home.html") 

@app.route("/velos")
def velos():
    with open("bikes.json") as f:
        bike_data = json.load(f)
    return render_template("velos.html", bikes=bike_data)

@app.route("/velos/<int:id>")
def presentation(id):
    with open("bikes.json") as f:
        bike_data = json.load(f)
    bike = bike_data[id-1]
    return render_template("presentation.html", bike=bike)

@app.route('/achat/<code>', methods = ["GET", "POST"])
def achat(code):
    if request.method == "GET":
        return render_template("achat.html", code=code)
    else:
        #Récupérer les données du formulaire
        form = request.form
        print(form)
        print(form["name"])
        print(form["livraison"])
        with open("bikes.json") as f:
            bike_data = json.load(f)
        bike = bike_data[int(code)-1]

        #Ecrire que le vélo n'est plus disponible dans le fichier json
        bike_data[int(code)-1]["in_stock"] = False
        with open("bikes.json", "w") as f:
            json.dump(bike_data, f)

        return render_template("fin.html", nom=form["name"] , livraison=form["livraison"], bike=bike)


