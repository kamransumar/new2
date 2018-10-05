import os
import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
                                       loader=jinja2.FileSystemLoader('templates'))


class Config:
    NEWS_API_SOURCE_URL = "https://newsapi.org/v2/sources?language=en&country=us&apiKey={}"
    NEWS_API_ARTICLES = "https://newsapi.org/v2/top-headlines?sources={}&apiKey={}"
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY ')


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
