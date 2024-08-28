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
    
    # Parse the JSON response data
    response_data = json.loads(response.data)
    
    # Check that 'body' is in the response data
    assert 'body' in response_data
    
    # Parse the 'body' field which is expected to be a JSON string
    body = json.loads(response_data['body'])
    
    # Check that 'url' is a key in the body and it's a list
    assert 'url' in body
    assert isinstance(body['url'], list)
    
    # Check that the list is not empty and contains strings
    assert len(body['url']) > 0
    assert all(isinstance(url[0], str) for url in body['url'])
    
    # Check that each URL in the list starts with 'http'
    assert all(url[0].startswith('http') for url in body['url'])
    
    # Verify the headers
    assert 'headers' in response_data
    assert response_data['headers']['Access-Control-Allow-Origin'] == '*'
    assert response_data['headers']['Content-Type'] == 'application/json'
