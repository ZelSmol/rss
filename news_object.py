class News:
    def __init__(self, title, description, pub_date, guid, category, author, img_link, timestamp,url):
        self.title = title
        self.description = description
        self.pub_date = pub_date
        self.guid = guid
        self.category = category
        self.author = author
        self.img_link = img_link
        self.timestamp = timestamp
        self.url = url

    def get_html(self):
        '''Преобразует объект новости в html код'''
        news_widget = open("web_interface/news_widget", "r").read()
        news_colors = {"sport": "warning", "world": "info", "business": "danger",
                       "health": "success", "entertainment": "secondary", "sci_tech": "primary"}
        return news_widget.format(color=news_colors[self.category], description=self.description,
                                  title=self.title, pub_date=self.pub_date, guid=self.guid,
                                  author=self.author, img_link=self.img_link, category=self.category, url=self.url)

    def __eq__(self, other):
        return self.timestamp == other.timestamp

    def __lt__(self, other):
        return self.timestamp > other.timestamp

    def __le__(self, other):
        return self.timestamp >= other.timestamp

    def __gt__(self, other):
        return self.timestamp < other.timestamp

    def __ge__(self, other):
        return self.timestamp <= other.timestamp
