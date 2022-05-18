import json
import eel


def create_new_profile():
    data = {
        "categories": {"sport": 0, "world": 0, "business": 0,
                       "health": 0, "entertainment": 0, "sci_tech": 0},
        "sources": {},
    }
    with open("./data/user_profile.json", 'w', encoding='utf-8') as profile:
        json.dump(data, profile)


@eel.expose
def update_user_profile(category, source):
    '''Обновляет пользовательский профиль после перехода на интересную новость'''
    with open("./data/user_profile.json", 'r', encoding='utf-8') as profile:
        data = json.load(profile)

    data["categories"][category] -= 1
    if source in data["sources"]:
        data["sources"][source] -= 1
    else:
        data["sources"][source] = -1

    with open("./data/user_profile.json", 'w', encoding='utf-8') as profile:
        json.dump(data, profile)


def get_user_data():
    '''Возвращает информацию о профиле'''
    with open("./data/user_profile.json", 'r', encoding='utf-8') as profile:
        return json.load(profile)
