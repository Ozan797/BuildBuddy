import requests
from bs4 import BeautifulSoup
import json

url = "https://pricespy.co.uk/c/ddr4-memory"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

product_names = soup.find_all(class_='ProductNameTable-sc-1stvbsu-3 bbvppQ')
product_prices = soup.find_all('span', {'class': 'PriceLabel-sc-lboeq9-0'})[:len(product_names)]

products_data = []
for name, price in zip(product_names, product_prices):
    price_text = price.text.strip()
    price_value = None
    if '£' in price_text:
        price_parts = price_text.split('£')
        for part in price_parts:
            if part:
                try:
                    part_value = float(''.join(filter(str.isdigit, part))) / 100
                    if part_value:
                        price_value = part_value
                        break
                except ValueError:
                    pass

    product = {
        "name": name.text.strip(),
        "price": price_value
    }
    products_data.append(product)

# Filter out entries with NULL price values
products_data = [product for product in products_data if product['price'] is not None]

# Write data to a JSON file
with open('ram_info.json', 'w') as file:
    json.dump(products_data, file, indent=4)

print("Data without NULL prices has been written to ram_info.json file.")
