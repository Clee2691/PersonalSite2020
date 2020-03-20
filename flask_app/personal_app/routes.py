from flask import render_template, url_for, redirect
from personal_app import site_app

@site_app.route("/")
def index():
    return render_template("index.html")

@site_app.route("/about")
def about():
    return render_template("about.html")

@site_app.route("/contact")
def contact():
    return render_template("contact.html")