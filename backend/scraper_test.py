import requests
from bs4 import BeautifulSoup
import json

url = "https://pricespy.co.uk/c/power-supplies"

# Send a GET request to the URL
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

product_names = soup.find_all('h3')

# Extract power supply names
power_supply_names = [name.text.strip() for name in product_names if "W" in name.text]

# Create a list of dictionaries for each power supply name
products_data = [{"name": name} for name in power_supply_names]

# Write data to a JSON file
with open('info.json', 'w') as file:
    json.dump(products_data, file, indent=4)

print("Data has been written to info.json file.")