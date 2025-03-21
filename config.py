"""Configuration Class for Flask"""
import os

class Config:
    """Default Config Settings"""
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

