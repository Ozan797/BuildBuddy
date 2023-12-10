# This file is used for testing the scraper before deploying into the Flask server

from bs4 import BeautifulSoup

# Read the HTML content from the file
with open('website_content.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all CPU Names
cpu_names = soup.find_all(class_='ProductName-sc-d3c4p4-6')[:24]  # Limit to 24 items

# Find all CPU prices
cpu_prices = soup.find_all('span', class_='PriceLabel-sc-lboeq9-0')[:24]  # Limit to 24 items

# Ensure both CPU names and prices have the same length
if len(cpu_names) == len(cpu_prices):
    # Zip CPU names and prices together
    cpu_info = zip(cpu_names, cpu_prices)

    # Print CPU name and price pairs
    for name, price in cpu_info:
        print("CPU Name:", name.get_text(strip=True))
        print("CPU Price:", price.get_text(strip=True))
        print("------------------------")
else:
    print("The number of CPU names and prices doesn't match. Check your data.")
