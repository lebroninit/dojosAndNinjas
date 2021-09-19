from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.controllers import ninjas

@app.route('/')
def home():
    return redirect('/dojos')

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("home.html", allDojos = dojos)

@app.route("/toDojos", methods=["post"])
def toDojos():
    return redirect("/dojos")

@app.route("/createDojo", methods=["post"])
def createDojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.create(data)
    return redirect("/dojos")

@app.route("/toNinjas", methods=["post"])
def toNinjas():
    thisid = request.form["id"]
    return redirect(f"/dojos/{thisid}")

@app.route("/dojos/<id>")
def dojosId(id):
    names = Dojo.get_name(id)
    name = names[0]["name"]
    allNinjas = Ninja.get_all_from(id)
    return render_template("ninjas.html", allNinjas = allNinjas, myName = name)
