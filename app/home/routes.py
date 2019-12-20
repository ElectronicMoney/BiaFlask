from flask import Blueprint
from app.home.controllers.HomeController import HomeController
from flask import render_template

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def get_home():
    home = HomeController()
    return render_template('index.html', home=home.get_home())
