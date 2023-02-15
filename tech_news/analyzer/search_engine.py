from tech_news.database import search_news

# Requisito 7
def search_by_title(title):
    query = search_news({"title": {"$regex": title, "$options": "i"}})
    list_title = []

    for index in query:
        new = (index["title"], index["url"])
        list_title.append(new)
    
    return list_title


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
