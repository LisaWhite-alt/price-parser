import requests
from bs4 import BeautifulSoup


URL = "https://www.xplit.ru/plitka-shestiugolnaya/"

def extract_max_page():
    s = requests.Session()
    s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    x_requests = s.get(URL)
    x_soup = BeautifulSoup(x_requests.text, "html.parser")
    x_paginator = x_soup.find_all("a", {"class": "page-link"})
    pages = []
    for page in x_paginator:
        pages.append(page.text)
    return int(pages[-2])

def extract_x_elements(last_page):
    for page in range(1, last_page+1):
        result = requests.get(f"{URL}{page}/")
        print(result.status_code)

extract_x_elements(extract_max_page())
