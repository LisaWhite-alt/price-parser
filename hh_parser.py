import requests
from bs4 import BeautifulSoup


URL = "https://hh.ru/search/vacancy?area=1&fromSearchLine=true&st=searchVacancy&text=python"
HEADERS = {
    "Host": "hh.ru",
    "User-Agent": "Safari",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

def extract_max_page():
    hh_requests = requests.get(URL, headers=HEADERS)
    hh_soup = BeautifulSoup(hh_requests.text, "html.parser")
    pages = []
    hh_paginator = hh_soup.find_all(
        "span",
        {"class": "pager-item-not-in-short-range"}
    )
    for page in hh_paginator:
        pages.append(int(page.find("a").text))
    return pages[-1]

def extract_job(html):
    title = html.find("a").text
    link = html.find("a")["href"]
    company = html.find("div", {"class": "vacancy-serp-item__meta-info-company"}).text
    location = (html.find("span", {"data-qa": "vacancy-serp__vacancy-address"}).text).partition(",")[0]
    return {"title": title, "link": link, "company": company, "location": location}

def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{URL}&page={page}", headers=HEADERS)
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all(
            "div",
            {"class": "vacancy-serp-item"}
        )
        for result in results:
            jobs.append(extract_job(result))
    return jobs

def get_jobs():
    return extract_jobs(extract_max_page())
