from flask import Blueprint,render_template,jsonify

main = Blueprint("main",__name__)

@main.route("/")
def home ():
    return render_template("index.html")

@main.route("/hello")
def hello ():
    return jsonify({"message":"hello from flask!"})
import time

@main.route("/slow")
def slow ():
    time.sleep(20)
    return "done"
