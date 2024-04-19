from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Contato")
def contato():
    return render_template("contato.html")

@app.route("/QuemSomos")
def quemsomos():
    return render_template("quemsomos.html")