from flask import Blueprint
from app.users.controllers.UserController import UserController

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_users():
    user = UserController()
    return user.get_users()
