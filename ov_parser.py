import requests
from bs4 import BeautifulSoup


URL = "https://stackoverflow.com/jobs?q=python"


def extract_max_page():
    ov_requests = requests.get(URL)
    ov_soup = BeautifulSoup(ov_requests.text, "html.parser")
    ov_paginator = ov_soup.find(
        "div",
        {"class": "s-pagination"}
    ).find_all("a")
    max_page = int(ov_paginator[-2].text.strip())
    return max_page

def extract_job(html):
    title = html.find("h2").find("a").text
    link_id = html.find("h2").find("a")["href"]
    link = "https://stackoverflow.com" + link_id
    company = html.find("h3").find_all("span")[0].text.strip()
    location = html.find("h3").find_all("span")[1].text.strip()
    return {"title": title, "link": link, "company": company, "location": location}

def extract_jobs(last_page):
    jobs = []
    for page in range(1, last_page+1):
        result = requests.get(f"{URL}&pg={page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all(
            "div",
            {"class": "-job"}
        )
        for result in results:
            jobs.append(extract_job(result))
    return jobs

def get_jobs():
    return extract_jobs(extract_max_page())
