from app import app
import urllib.request
import json
from app.models import Article, Source

api_key = None
base_url = None


def configure_request(app):
    '''
    Configures the request by getting the api_key and base_url
    '''
    global api_key, base_url
    api_key = app.config.get('NEWS_API_KEY')
    base_url = app.config.get('NEWS_BASE_URL')
    
    
def send_request(request_url):
    '''
    Send request to news api and returns a json response
    '''
    with urllib.request.urlopen(request_url) as data:
        return json.loads(data.read())