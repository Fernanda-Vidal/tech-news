from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    list_title = []

    for index in search:
        new = (index["title"], index["url"])
        list_title.append(new)

    return list_title


# Requisito 8
def search_by_date(date):
    list_search = []

    try:
        fomatted = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        search = search_news({"timestamp": {"$regex": fomatted}})
        for index in search:
            new = (index["title"], index["url"])
            list_search.append(new)
    except ValueError:
        raise ValueError("Data inválida")

    else:
        return list_search


# Requisito 9
def search_by_category(category):
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    list_title = []

    for index in search:
        new = (index["title"], index["url"])
        list_title.append(new)

    return list_title
