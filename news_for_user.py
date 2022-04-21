import eel

from rss_parser import get_feed
from show_news import show_news


@eel.expose
def news_by_url(url):
    return show_news(get_feed([url]))


def get_sources():
    sources = open("news_sources", "r")
    return sources.read().split("\n")


@eel.expose
def get_news_set():
    return show_news(get_feed(get_sources()))
