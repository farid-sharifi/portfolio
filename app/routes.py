from flask import Blueprint,render_template,jsonify

main = Blueprint("main",__name__)

@main.route("/")
def home ():
    return render_template("index.html")


import time

@main.route("/slow")
def slow ():
    time.sleep(20)
    return "done"
