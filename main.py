import eel
import os
from news_for_user import news_by_url
from rss_parser import get_feed

eel.init("web_interface")
eel.start('index.html', size=(700, 700))
