import requests
from requests_html import HTMLSession
from news_classificator import predict_category
from NewsClass import News
from datetime import datetime


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
    Возвращает список объектов класса News
    """
    data = []
    for url in urls:
        response = get_source(url)
        with response as r:

            items = r.html.find("item", first=False)

            for item in items[:10]:

                title = item.find('title', first=True).text
                pub_date = item.find('pubDate', first=True).text
                guid = item.find('guid', first=True).text
                description = item.find('description', first=True).text
                author = "Unknown"
                img_link = "https://realsound.jp/wp-content/uploads/2020/08/rs-font-thumbnail_news_300.jpg"

                # Проверяем нашелся ли автор статьи
                if item.find("credit", first=True):
                    author = item.find("credit", first=True).text
                elif item.find("creator", first=True):
                    author = item.find("creator", first=True).text

                # Проверяем нашлось ли изображение
                if item.find("content", first=True):
                    img_link = item.find("content", first=True)
                    img_link = str(img_link).split()[4][5:-1]
                elif item.find("enclosure", first=True):
                    img_link = item.find("enclosure", first=True)
                    img_link = str(img_link).split()[2][5:-1]

                category = predict_category(title)

                data.append(News(title, description, pub_date, guid,
                                 category, author, img_link,
                                 datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z").timestamp()))

    return data
