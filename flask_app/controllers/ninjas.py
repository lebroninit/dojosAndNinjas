from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.controllers import dojos

@app.route("/ninja")
def ninja():
    dojos = Dojo.get_all()
    return render_template("ninja.html", allDojos = dojos)

@app.route("/toNinja", methods=["post"])
def toNinja():
    return redirect("/ninja")

@app.route("/createNinja", methods=["post"])
def createNinja():
    data = {
        "fName": request.form["fName"],
        "lName": request.form["lName"],
        "age": request.form["age"],
        "dojoid": request.form.get("inputSelect")
    }
    Ninja.create(data)
    return redirect("/dojos")
