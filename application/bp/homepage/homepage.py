from flask import Blueprint, render_template
from application.database import User, db

# Declare the Blueprint
homepage = Blueprint('homepage', __name__, template_folder='templates')

# Default route
@homepage.route('/')
def index():
    return render_template('homepage.html')

# About route
@homepage.route('/about')
def about():
    return render_template('about.html')

# Users route
@homepage.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@homepage.route('/users/<int:user_id>')
def user_detail(user_id):
    user = User.query.get(user_id)
    if not user:
        return render_template('404.html'), 404
    return render_template('user_detail.html', user=user)

