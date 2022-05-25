import eel
from news_for_user import get_news_set, news_by_url


#Запуск и развертывание окна веб-интерфейса
eel.init("web_interface")
eel.start('index.html', size=(700, 700))
