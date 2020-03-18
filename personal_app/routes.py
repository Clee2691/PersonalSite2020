from flask import render_template
from personal_app import site_app

@site_app.route('/')
def index():
    return render_template('index.html')