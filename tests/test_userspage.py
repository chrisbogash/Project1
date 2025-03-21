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

def test_user_page_content(client):
    """flask unit testing for content in user page"""
    response = client.get("/users/1")
    assert response.status_code == 200
    assert b"Jason Brown" in response.data

def test_users_error_page_content(client):
        """flask unit testing for content in user page"""
        response = client.get("/users/9999")
        assert response.status_code == 404
        assert b"Not Found" in response.data

def test_users_page_content(client):
    """Flask unit testing for content in the /users page"""
    response = client.get("/users")
    assert response.status_code == 200
    assert b"User Count" in response.data
