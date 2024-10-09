from flask import Flask, abort, render_template
import os

TEMPLATES = "templates"

app = Flask(__name__, template_folder=TEMPLATES)

@app.route("/")
@app.route("/hello")
def hello():
    print("home")
    return "<h1>Hello World</h1>"

@app.route("/ping")
def ping():
    print("ping")
    return '<a href="pong">Ping!</a>'

@app.route("/pong")
def pong():
    print("pong")
    return '<a href="ping">Pong!</a>'

@app.route("/output")
def output():
 print("output")
 return render_template("output/index.html")

# @app.route('/<path:page>')
# def show_page(page):
#     print("pelican page")
#     fnrel = os.path.join("output", page)
#     print(f"{fnrel = }")
#     fnabs = os.path.join(TEMPLATES, "output", page)
#     print(f"{fnabs = }")
#     # checks whether page exists
#     if os.path.exists(fnabs):
#         print("render_template")
#         return render_template(fnrel)
#     else:
#         print("ko")
#         abort(404)

# velo route
@app.route("/velo")
def velo():
    return render_template("velo/index.html")



