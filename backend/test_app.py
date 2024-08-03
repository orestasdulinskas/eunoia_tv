import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_random_content_with_real_api(client):
    response = client.get('/random-content')
    assert response.status_code == 200
    assert 'url' in response.json
    assert isinstance(response.json['url'][0], str)
    assert response.json['url'][0].startswith('http')