from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import random
import re

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Your Tumblr API key
API_KEY = '4JlRp52tQElhZnLKSBn3n4CGa5wfW7RZ'
#API_KEY = 'fyJYc9OHmlh9Iyb271bzkFA9cGEUrcoB6FmkClVTgejQCMshfH'
@app.route('/random-content')
def random_content():    
    search_query = 'puppies'
    count = 1
    search_endpoint = f'https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={search_query}&limit={count}'
    response = requests.get(search_endpoint)
    data = response.json()
    return jsonify({'url': data['data'][0]['images']['original']['url']})

if __name__ == '__main__':
    app.run(debug=True)