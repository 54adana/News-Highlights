from app import app
import urllib.request,json
from .models import news
News = news.News
# Getting api key
api_key = app.config['NEWS_API_KEY']
#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)
    return news_results
    
def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        source = news_item.get('source')
        title = news_item.get('title')
        description = news_item.get('description')
        poster = news_item.get('urlToImage')
        url = news_item.get('url')
        # category = news_item.get('category')
        
        news_object = News(source, title, description, poster, url)
        news_results.append(news_object)
    return news_results

def get_News(id):
    get_news_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('title')
            description = news_details_response.get(' description')
            poster = news_details_response.get('poster')
            news_object = News(id,title, description,poster,url)
    return News_object