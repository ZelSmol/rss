import heapq

from user_profile import get_user_data


def show_news(news):
    q = []
    data = get_user_data()
    for item in news:
        try:
            source = data["sources"][item.guid]
        except:
            source = 0
        heapq.heappush(q, (data["categories"][item.category], source, item))
    result = []

    while q:
        next_item = heapq.heappop(q)
        result.append(next_item[2].get_html())

    return "".join(result)
