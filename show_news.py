import eel

from rss_parser import get_feed


def show_news(news):
    news_widget = open("news_widget", "r").read()
    news_colors = {"sport": "warning", "world": "info", "business": "danger",
                   "health": "success", "entertainment": "secondary", "sci_tech": "primary"}
    result = []
    for item in news:
        result.append(news_widget.format(color=news_colors[item["category"]], description=item["description"],
                                         title=item["title"], pub_date=item["pub_date"], guid=item["guid"],
                                         author=item["author"], img_link=item["img_link"], category=item["category"], ))

    return "".join(result)
