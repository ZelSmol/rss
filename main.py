import eel
import os
from news_for_user import news_by_url
from rss_parser import get_feed
from user_profile import update_user_profile

eel.init("web_interface")
eel.start('index.html', size=(700, 700))
