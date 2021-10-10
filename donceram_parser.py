import requests
from bs4 import BeautifulSoup


URL = "https://donceram.ru/katalog/mozaika?type=products"
HEADERS = {
    "Host": "donceram.ru",
    "User-Agent": "Safari",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def extract_max_page():
    dc_requests = requests.get(URL, headers=HEADERS)
    dc_soup = BeautifulSoup(dc_requests.text, "html.parser")
    dc_paginator = dc_soup.find_all(
        "a",
        {"class": "pagination__link pagination__box"}
    )
    return int(dc_paginator[1].text)

def extract_dc_elements(last_page):
    for page in range(1, last_page+1):
        result = requests.get(f"{URL}&page={page}", headers=HEADERS)
        print(result.status_code)

extract_dc_elements(extract_max_page())
