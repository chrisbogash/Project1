"""This is a test script to test flask application"""
import pytest
from application.app import init_app

@pytest.fixture
def app():
    """Creates and configures a test app instance."""
    app = init_app()  # Call the function to get an app instance
    return app

@pytest.fixture
def client(app):
    """Creates a test client using the app instance."""
    return app.test_client()  # Now app is a Flask instance

def test_aboutpage_content(client):
    """flask unit testing for content in about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data
