from flask import Flask
from flask_cors import CORS
import re
import requests
import os
import json
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Your Tumblr API key
load_dotenv()
API_KEY = os.getenv('TUMBLR_API_KEY')

@app.route('/random-content')
def random_content():
    all_posts = []
    offset = 0
    limit = 20

    session = requests.Session()
    retry = Retry(connect=5, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)

    # Tumblr blog URL
    blog_url = 'eunoia-tv.tumblr.com'

    while True:
        # Make a request to the Tumblr API to get posts
        response = session.get(f'https://api.tumblr.com/v2/blog/{blog_url}/posts?api_key={API_KEY}&offset={offset}&limit={limit}', timeout=10)
        data = response.json()

        # Check if there are posts in the response
        if not data['response']['posts']:
            break

        # Extract post URLs (assuming they are images for simplicity)
        post_urls = [re.findall(r'src="([^"]+)"', post['body']) for post in data['response']['posts']]

        all_posts.extend(post_urls)

        # Increment the offset
        offset += limit

    # Return the list of URLs
    return {
        'statusCode': 200,
        'body': json.dumps({'url': all_posts}),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        }
    }

if __name__ == '__main__':
    app.run(debug=True)
