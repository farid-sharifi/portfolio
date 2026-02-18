from flask import Blueprint,request,render_template,jsonify
from app.send_email import send_email
import time

home_bp = Blueprint("home",__name__)

rate_limits = {}

@home_bp.before_request
def rate_limit_by_ip():
    if request.path != "/form_contact":
        return
    ip = request.remote_addr
    now = time.time()

    if ip not in rate_limits:
        rate_limits[ip] = []
    rate_limits[ip] = [t for t in rate_limits[ip] if now - t < 600]

    if len(rate_limits[ip]) >= 5:
        return jsonify({"error":"Rate limit exceeded. Try again later!"}),429
    
    rate_limits[ip].append(now)

@home_bp.route("/")
def home():
    return render_template("home.html")

@home_bp.route("/projects")
def projects():
    return render_template("projects.html")

@home_bp.route("/contact")
def contact():
    return render_template("contact.html")

@home_bp.route("/form_contact",methods = ["POST"])
def form_contact():
    data = request.form
    if data:
        if not data.get("username"):
            return jsonify({"error":"Name is required!"}),400
        if not  data.get("email"):
            return jsonify({"error":"Email is required!"}),400
        if not data.get("message"):
            return jsonify({"error":"Message is required!"}),400

        ok = send_email(data)
        if ok:
            return jsonify({"message":"Your message was sent successfully!"}),200
        return jsonify({"error":"Server-side error!(Email could not be sent!)"}),500
    return jsonify({"error":"User-side error!(data-error)"}),400
