from bs4 import BeautifulSoup
import requests


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_block = soup.find('ul', class_='products')
    product_block = main_block.find_all('li', class_="product")

    content = []
    for product in product_block:
        brand_name = product.find('h2', class_="woocommerce-loop-product__title").get_text(strip=True)
        product_image = product.find('span', class_="product-image").find('img')['src']
        product_price = product.find("span", class_="woocommerce-Price-amount").get_text(strip=True).replace("000", "000 ")
        configurations = product.find("h5").get_text(strip=True)
        product_url = product.find("a")["href"]

        content.append({
            "brand_name": brand_name,
            "product_url": product_url,
            "product_image": product_image,
            "product_price": product_price,
            "configurations": configurations
        })
    return content


class Parser:
    def __init__(self, url):
        self.URL = url
        self.HOST = 'https://pcmarket.uz'
        self.HEADERS = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.114 Safari/537.36 '
        }

    def get_html(self):
        response = requests.get(self.URL, headers=self.HEADERS)
        try:
            response.raise_for_status()
            return response.text
        except requests.HTTPError:
            print(f'error {response.status_code}')

    def run(self):
        html = self.get_html()
        return get_content(html)


laptop_parser = Parser('https://pcmarket.uz/cat/noutbuki/')
print(laptop_parser.run())
#
# smartphone_parser = Parser('https://pcmarket.uz/cat/kompyutery/')
# print(smartphone_parser.run())
#
# TV_parser = Parser('https://pcmarket.uz/cat/televizory/')
# print(smartphone_parser.run())