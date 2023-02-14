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
    select = Selector(html_content)

    url = select.css("head > link[rel=canonical]::attr(href)").get()
    title = select.css("h1.entry-title::text").get().strip()
    timestamp = select.css("li.meta-date::text").get().strip()
    writer = select.css("span.author > a ::text").get().strip()
    reading_time = select.css("li.meta-reading-time::text")
    summary = select.css("div.entry-content > p:first-of-type *::text").getall()
    category = select.css("span.label::text").get().strip()


    return {
    "url": url,
    "title": title,
    "timestamp": timestamp,
    "writer": writer,
    "reading_time": int(reading_time.re_first(r"\d+")),
    "summary": "".join(summary).strip(),
    "category": category
    }


# Requisito 5
def get_tech_news(amount):
  ...