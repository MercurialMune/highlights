import urllib.request,json
from .models import News

News = News.News
# Getting api key
api_key = None

# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        description = news_item.get('description')
        author = news_item.get('author')
        publishedAt = news_item.get('publishedAt')
        urlToImage = news_item.get('urlToImage')

        if urlToImage:
            news_object = News(id,description,author,publishedAt,urlToImage)
            news_results.append(news_object)

    return news_results