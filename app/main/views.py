from flask import render_template
from . import main
from ..request import get_url, get_articles

# Views


@main.route('/')
def index():

    # Getting news source
    popular_sources = get_url()
    print(popular_sources)

    sources = popular_sources

    return render_template('index.html', popular=sources)


@main.route('/source/<id>')
def articles(id):

    # Getting news articles
    popular_articles = get_articles(id)
    print(popular_articles)
    articles = popular_articles

    return render_template('article.html', articles=articles, id=id)
