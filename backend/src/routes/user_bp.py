from flask import Blueprint
from src.controllers.user_controller import signup, login, profile, logout

# Blueprint for user authentication routes
user_bp = Blueprint('user_bp', __name__)

# Define routes
user_bp.route('/signup', methods=['POST'])(signup)
user_bp.route('/login', methods=['POST'])(login)
user_bp.route('/profile', methods=['GET'])(profile)
user_bp.route('/logout', methods=['POST'])(logout)
