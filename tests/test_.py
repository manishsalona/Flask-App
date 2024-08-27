import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home page."""
    response = client.get('/')
    assert response.data == b"Welcome to the Flask App!"
    assert response.status_code == 200

def test_greet(client):
    """Test the greet API."""
    response = client.post('/api/greet', json={"name": "Alice"})
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Alice!"}

def test_greet_no_name(client):
    """Test the greet API with no name."""
    response = client.post('/api/greet', json={})
    assert response.status_code == 200
    assert response.json == {"message": "Hello, Guest!"}
