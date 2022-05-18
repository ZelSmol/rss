import eel

from rss_parser import get_feed
from show_news import show_news


@eel.expose
def news_by_url(url):
    '''Возвращает новостную ленту источника'''
    return show_news(get_feed([url]))


def get_sources():
    '''Подгрузка списка пользовательских источников'''
    sources = open("data/news_sources", "r")
    return sources.read().split("\n")


@eel.expose
def get_news_set():
    '''Возвращает новостную ленту множества источников'''
    return show_news(get_feed(get_sources()))
