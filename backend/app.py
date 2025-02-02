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
CORS(app)

load_dotenv()
API_KEY = os.getenv('TUMBLR_API_KEY')
BLOG_URL = 'eunoia-tv.tumblr.com'

@app.route('/get-posts')
def get_posts():
    all_posts = []
    offset = 0
    limit = 20

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('https://', adapter)
    
    try:
        while True:
            response = session.get(
                f'https://api.tumblr.com/v2/blog/{BLOG_URL}/posts?api_key={API_KEY}&offset={offset}&limit={limit}',
                timeout=10
            )
            
            if response.status_code != 200:
                return {
                    'statusCode': response.status_code,
                    'body': json.dumps({'error': 'Failed to fetch from Tumblr API'}),
                    'headers': {
                        'Access-Control-Allow-Origin': '*',
                        'Content-Type': 'application/json'
                    }
                }
                
            data = response.json()
            
            if not data['response']['posts']:
                break

            post_urls = [re.findall(r'src="([^"]+)"', post['body']) for post in data['response']['posts']]
            filtered_urls = [urls[0] for urls in post_urls if urls]
            all_posts.extend(filtered_urls)
            
            #if len(all_posts) >= 50:
            #    break
                
            offset += limit

        return {
            'statusCode': 200,
            'body': json.dumps({'urls': all_posts}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            }
        }

if __name__ == '__main__':
    app.run(debug=True)