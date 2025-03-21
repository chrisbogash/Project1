"""
Main Flask Application Initialization
"""
from flask import Flask, render_template
from flask_migrate import Migrate
from application.database import db
from application.bp.homepage.homepage import homepage
import config



migrate = Migrate()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config.Config())

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    @app.errorhandler(404)
    def not_found_error(error):
         return render_template('404.html'), 404

    with app.app_context():
        app.register_blueprint(homepage)
        return app
