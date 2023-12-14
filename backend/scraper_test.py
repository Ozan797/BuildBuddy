import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://pricespy.co.uk/c/power-supplies"

# Send a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Extract power supply names and prices
product_names = soup.find_all('h3')
power_supply_names = [name.text.strip() for name in product_names if "W" in name.text]

product_prices = soup.find_all('span')
prices_without_incl_delivery = [
    span.text.strip() 
    for span in product_prices 
    if re.search(r'£', span.text) and "Incl. delivery" not in span.text
]

# Extract wattage (power) information using regular expression
wattages = [int(re.search(r'(\d+)\s*W', name).group(1)) if re.search(r'(\d+)\s*W', name) else 0 for name in power_supply_names]

# Combine names, prices, and wattages
products_data = [{"name": name, "price": price, "power": wattage} for name, price, wattage in zip(power_supply_names, prices_without_incl_delivery, wattages)]

# Write data to a JSON file
with open('info.json', 'w') as file:
    json.dump(products_data, file, indent=4)

print("Data with names, prices, and power information has been written to info.json file.")
