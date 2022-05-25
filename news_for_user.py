import eel

from rss_parser import get_feed
from show_news import show_news


@eel.expose
def news_by_url(url):
    '''Возвращает новостную ленту источника'''
    with open("./data/news_sources", 'r', encoding='utf-8') as sources:
        news_sources=sources.readlines()
    if url not in news_sources:
        with open("./data/news_sources", 'a', encoding='utf-8') as sources:
            sources.write("\n")
            sources.write(url)
    return show_news(get_feed([url]))


def get_sources():
    '''Подгрузка списка пользовательских источников'''
    sources = open("data/news_sources", "r")
    return sources.read().split("\n")


@eel.expose
def get_news_set():
    '''Возвращает новостную ленту множества источников'''
    return show_news(get_feed(get_sources()))
