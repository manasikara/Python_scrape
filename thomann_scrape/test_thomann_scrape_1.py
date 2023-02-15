import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass, asdict
import csv

@dataclass
class Product:
    manufacturer: str
    title: str
    price: str

def get_html(page):
    url = f"https://www.thomann.de/gb/search_GF_electric_guitars.html?ls=10&pg={page}&hl=BLOWOUT"
    resp = httpx.get(url)
    #html= HTLMParser(resp.text)
    # return html
    return HTMLParser(resp.text)

def parse_products(html):
    products = html.css("div.product")

    results = []
    for item in products:
        new_item = Product(
            manufacturer=item.css_first("span.title__manufacturer").text(),
            title=item.css_first("span.title__name").text(),
            price=item.css_first("div.product__price").text().strip()
        )
       # print(asdict (new_item))
        results.append(asdict (new_item))
    return results

def to_csv(res):
    with open("results.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["manufacturer", "title", "price"])
        writer.writerows(res)


def main():
    for x in range(1,4):
        html = get_html(x)
        print(html.css_first("title").text())
        res = parse_products(html)
        #print(res)
        to_csv(res)


if __name__ == '__main__':
    main()