from datetime import datetime

import requests
from requests_html import HTMLSession

from news_object import News
from predict_category import predict_category


def get_source(url: str):
    """
    Возвращает ответ с источника, иначе ошибку подключения
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def get_feed(urls: list) -> list:
    """
    Возвращает список объектов класса News`
    """
    feed = []
    for url in urls:
        response = get_source(url)
        with response as r:

            items = r.html.find("item", first=False)

            for item in items[:10]:

                title = item.find('title', first=True).text
                pub_date = item.find('pubDate', first=True).text
                guid = item.find('guid', first=True).text
                description = item.find('description', first=True).text

                # Вычленение автора (если есть)
                if item.find("credit", first=True):
                    author = item.find("credit", first=True).text
                elif item.find("creator", first=True):
                    author = item.find("creator", first=True).text
                else:
                    author = "Unknown"

                # Вычленение изображения (если есть)
                if item.find("content", first=True):
                    img_link = item.find("content", first=True)
                    img_link = str(img_link).split()[4][5:-1]
                elif item.find("enclosure", first=True):
                    img_link = item.find("enclosure", first=True)
                    img_link = str(img_link).split()[2][5:-1]
                else:
                    img_link = "https://realsound.jp/wp-content/uploads/2020/08/rs-font-thumbnail_news_300.jpg"

                category = predict_category(title)

                feed.append(News(title, description, pub_date, guid,
                                 category, author, img_link,
                                 datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z").timestamp(),url))

    return feed
