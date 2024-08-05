from flask import Flask
from flask_cors import CORS
import re
import requests
import random
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Your Tumblr API key
load_dotenv()
API_KEY = os.getenv('TUMBLR_API_KEY')

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
    return {
        'statusCode': 200,
        'body': json.dumps({'url': random_url}),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        }
    }

if __name__ == '__main__':
    app.run(debug=True)
