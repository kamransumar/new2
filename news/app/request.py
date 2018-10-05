from app import app
from .config import Config
from .models import source, articles
import urllib
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

Source = source.Source
Articles = articles.Articles
# Getting api key
api_key = app.config['NEWS_API_KEY']
api_url = app.config['NEWS_API_SOURCE_URL']
api_articles = app.config['NEWS_API_ARTICLES']


def get_url():
    get_url = api_url.format(api_key)
    print(get_url)

    with urllib.request.urlopen(get_url) as source:
        data = source.read()
        data = json.loads(data)
        print(data)

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
    print(get_articles)

    with urllib.request.urlopen(get_articles) as source:
        data = source.read()
        data = json.loads(data)
        print(data)

        articles = None

        if data['articles']:
            articles_list = data['articles']
            articles = process_articles(articles_list)

    return articles


def process_articles(articles_list):
    articles = []
    for article in articles_list:
        name = article.get('name')
        author = article.get('author')
        description = article.get('description')
        urlToImage = article.get('urlToImage')
        url = article.get('url')

        if url:
            article_object = Articles(
                name, author, description, urlToImage, url)
            articles.append(article_object)

    return articles
