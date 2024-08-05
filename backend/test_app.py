import pytest
import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_random_content_with_real_api(client):
    response = client.get('/random-content')
    assert response.status_code == 200
    
    response_data = json.loads(response.data)
    assert 'body' in response_data
    body = json.loads(response_data['body'])
    assert 'url' in body
    assert isinstance(body['url'][0], str)
    assert body['url'][0].startswith('http')
    
    assert 'headers' in response_data
    assert response_data['headers']['Access-Control-Allow-Origin'] == '*'
    assert response_data['headers']['Content-Type'] == 'application/json'