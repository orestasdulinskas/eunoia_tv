from flask import Flask, jsonify
from flask_cors import CORS
import requests
import random

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

api = 0

with open('./api_keys.txt', 'r') as f:
    apis = [line.strip() for line in f]

with open('./topics.txt', 'r') as f:
    topics = [line.strip() for line in f]

@app.route('/random-content')
def random_content():
    global api
    if api < len(apis)-1: api += 1
    else:   api = 0
    search_endpoint = f'https://api.giphy.com/v1/gifs/search?api_key={apis[api]}&q={random.choice(topics)}&limit=5'
    response = requests.get(search_endpoint)
    data = response.json()
    return jsonify({'url': data['data'][random.randint(0, 4)]['images']['original']['url']})
if __name__ == '__main__':
    app.run(debug=True)
