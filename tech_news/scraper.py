import requests
from parsel import Selector
import time


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        res = requests.get(url, {"user-agent": "Fake user-agent"}, timeout=3)
        if res.status_code == 200:
            return res.text

    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    select = Selector(html_content)
    return select.css("a.cs-overlay-link ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(html_content)
    return select.css("a.next ::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
