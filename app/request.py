# import app
# from . import main
# from config import Config
from .models import Articles, Source
import urllib.request
import json
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# Source = source.Source
# Articles = articles.Articles
# Getting api key
api_key =None
api_url = None
api_articles = None

def configure_request(app):
    global api_key, api_url, api_articles
    api_key = app.config['NEWS_API_KEY']
    # print(api_key)
    api_url = app.config['NEWS_API_SOURCE_URL']
    # print(api_url)
    api_articles = app.config['NEWS_API_ARTICLES']

# print(api_key)

def get_url():
    get_url = api_url.format(api_key)
    # print(get_url)

    with urllib.request.urlopen(get_url) as source:
        data = source.read()
        data = json.loads(data)
        # print(data)

        sources = None

        if data['sources']:
            sources_list = data['sources']
            sources = process_source(sources_list)

    return sources


def process_source(sources_list):
    sources = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        country = source.get('country')

        if url:
            source_object = Source(id, name, description, url, country)
            sources.append(source_object)

    return sources


def get_articles(id):
    get_articles = api_articles.format(id, api_key)
    # print(get_articles)

    with urllib.request.urlopen(get_articles) as source:
        data = source.read()
        data = json.loads(data)
        # print(data)

        articles = None

        if data['articles']:
            articles_list = data['articles']
            articles = process_articles(articles_list)

    return articles


def process_articles(articles_list):
    articles = []
    for article in articles_list:
        title = article.get('title')
        author = article.get('author')
        description = article.get('description')
        urlToImage = article.get('urlToImage')
        url = article.get('url')
        publishedAt = article.get('publishedAt')

        if url:
            article_object = Articles(
                title, author, description, urlToImage, url, publishedAt)
            articles.append(article_object)

    return articles
