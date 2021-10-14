import requests
from price import PRICE
from bs4 import BeautifulSoup


NAME_URL = {
    "REX BROWN POLISHED RECT 60*120 (КГ) 1,44м(2шт)/46,08м": "https://www.xplit.ru/catalog/rex-ape-ceramica/67800.html",
    "ATREO BLANCO PULIDO 60*120 (КГ) 1,44м(2шт)/38,88м": "https://www.xplit.ru/catalog/60x120-argenta/63815.html",
    "AURORA BLUE 60*120 (КГ) 1,44м(2шт)/46,08м": "https://www.xplit.ru/catalog/60x120-argenta/67944.html",
    "TANTALO NEGRO PULIDO 60*120 (КГ) 1,44м(2шт)/38,88м": "https://www.xplit.ru/catalog/60x120-argenta/63814.html",
    "BLACK GOLDEN 60*119,50 (КГ, полир., рект.) 1к-1,434м(2шт)/50,19м": "https://www.xplit.ru/catalog/black-golden-cifre-ceramica/48789.html",
    "CAPRAIA GOLD 60*120 (КГ) 1,44м2(2шт)/46,08м2": "https://www.xplit.ru/catalog/capraia-cifre-ceramica/77864.html",
    "AMAZZONITE JADE 60*120 (КГ, суперполир., рект.) 1,44м2(2шт)/46,08м2": "https://www.xplit.ru/catalog/amazzonite-cifre-ceramica/73676.html",
    "ICEBERG NPLUS 59,8*119,8 (КГ) 1,433м2 (2шт)/42,99м": "https://www.xplit.ru/catalog/iceberg-fanal-ceramica/78002.html",
}

def extract_price():
    fail = []
    for name in NAME_URL:
        if name in PRICE:
            page = requests.get(NAME_URL[name])
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, "html.parser")
                name_price_str = ((soup.find("div", {"class": "money"}).find("span").text)[:-4])
                name_price = int("".join(name_price_str.split()))
                if name_price < PRICE[name]:
                    fail.append({"site": "xplit", "name": name, "link": NAME_URL[name], "price_fail": name_price, "price_true": PRICE[name]})
    return fail

def get_fail_list():
    return extract_price()
