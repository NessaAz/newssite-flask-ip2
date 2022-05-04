from app import app


api_key = None
base_url = None


def configure_request(app):
    '''
    Configures the request by getting the api_key and base_url
    '''
    global api_key, base_url
    api_key = app.config.get('NEWS_API_KEY')
    base_url = app.config.get('NEWS_BASE_URL')
    
    
