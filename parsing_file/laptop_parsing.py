import requests
from bs4 import BeautifulSoup
from db_bot.laptop_db import Laptop_db

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_block = soup.find('ul', class_='products')
    product_block = main_block.find_all('li', class_="product")

    content_laptop = []
    for product in product_block:
        brand_name = product.find('h2', class_="woocommerce-loop-product__title").get_text(strip=True)
        product_image = product.find('span', class_="product-image").find('img')['src']
        product_price = product.find("span", class_="woocommerce-Price-amount").get_text(strip=True).replace("000", "000 ")
        configurations = product.find("a", class_="description").find('h5').get_text(strip=True)
        product_url = product.find("a")["href"]
        content_laptop.append({
            "brand_name": brand_name,
            "product_url": product_url,
            "product_image": product_image,
            "product_price": product_price,
            "configurations": configurations
        })
    return content_laptop


class Parser_laptop:
    def __init__(self):
        self.URL = 'https://pcmarket.uz/cat/noutbuki/'
        self.HOST = 'https://pcmarket.uz'
        self.HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.114 Safari/537.36 '
        }

    def get_html(self, url):
        response = requests.get(url, headers=self.HEADERS)
        try:
            response.raise_for_status()
            return response.text
        except requests.HTTPError:
            print(f'error {response.status_code}')

    def run(self):
        html = self.get_html(self.URL)
        content1 = get_content(html)
        for data in content1:
            Laptop_db().insert_data(*data.values())

Parser_laptop().run()