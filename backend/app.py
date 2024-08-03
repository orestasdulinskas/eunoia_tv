from flask import Flask, jsonify
from flask_cors import CORS
import re
import requests
import random

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Your Tumblr API key
#API_KEY = 'fyJYc9OHmlh9Iyb271bzkFA9cGEUrcoB6FmkClVTgejQCMshfH'
with open('./api_keys.txt', 'r') as f:
    API_KEY = f.read()

@app.route('/random-content')
def random_content():
    # Tumblr blog URL
    blog_url = 'eunoia-tv.tumblr.com'
    # Make a request to the Tumblr API to get posts
    response = requests.get(f'https://api.tumblr.com/v2/blog/{blog_url}/posts?api_key={API_KEY}')
    # Parse the JSON response
    data = response.json()
    # Extract post URLs (assuming they are images for simplicity)
    post_urls = [re.findall(r'src="([^"]+)"',post['body']) for post in data['response']['posts']]
    # Choose a random post URL
    random_url = random.choice(post_urls)
    # Return the random post URL
    return jsonify({'url': random_url})

if __name__ == '__main__':
    app.run(debug=True)
