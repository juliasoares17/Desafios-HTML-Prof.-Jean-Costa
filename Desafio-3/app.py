from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("home.html")

@app.route("/Protagonistas")
def protagonistas():
    return render_template("protagonistas.html")

@app.route("/Professores")
def professores():
    return render_template("professores.html")

@app.route("/Contato")
def contato():
    return render_template("contato.html")
