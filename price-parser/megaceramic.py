import requests
from price import PRICE
from bs4 import BeautifulSoup


NAME_URL = {
    "REX BROWN POLISHED RECT 60*120 (КГ) 1,44м(2шт)/46,08м": "https://megaceramic.ru/index.php?route=product/product&product_id=214436",
    "BLACK GOLDEN 60*119,50 (КГ, полир., рект.) 1к-1,434м(2шт)/50,19м": "https://megaceramic.ru/index.php?route=product/product&product_id=215301",
    "CAPRAIA GOLD 60*120 (КГ) 1,44м2(2шт)/46,08м2": "https://megaceramic.ru/index.php?route=product/product&product_id=250009",
    "LUXURY BEIGE 60*120 (КГ, полир.) 1,44м(2шт)": "https://megaceramic.ru/index.php?route=product/product&product_id=215297",
    "LUXURY WHITE 60*120 (КГ, полир.) 1,44м(2шт)": "https://megaceramic.ru/index.php?route=product/product&product_id=215299",
    "AMAZZONITE JADE 60*120 (КГ, суперполир., рект.) 1,44м2(2шт)/46,08м2": "https://megaceramic.ru/index.php?route=product/product&product_id=250010",
    "PAONAZZO 60*120 (КГ, суперполир., рект.) 1,44м2(2шт)/46,08м2": "https://megaceramic.ru/index.php?route=product/product&product_id=250011",
    "ICEBERG NPLUS 59,8*119,8 (КГ) 1,433м2 (2шт)/42,99м": "https://megaceramic.ru/index.php?route=product/product&product_id=255588",
}

def extract_price():
    fail = []
    for name in NAME_URL:
        if name in PRICE:
            page = requests.get(NAME_URL[name])
            if page.status_code == 200:
                soup = BeautifulSoup(page.text, "html.parser")
                name_price = int((soup.find("div", {"id": "product"}).find("p", {"class": "price"}).text)[6:-5])
                if name_price < PRICE[name]:
                    fail.append({"site": "megaceramic", "name": name, "link": NAME_URL[name], "price_fail": name_price, "price_true": PRICE[name]})
    return fail

def get_fail_list():
    return extract_price()
