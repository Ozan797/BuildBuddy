# Scraper for data
from bs4 import BeautifulSoup

def scrape_cpu_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file: # Reads from file
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    cpu_names = soup.find_all(class_='ProductName-sc-d3c4p4-6')[:24]
    cpu_prices = soup.find_all('span', class_='PriceLabel-sc-lboeq9-0')[:24]

    cpu_info_list = []
    for name, price in zip(cpu_names, cpu_prices):
        cpu_info_list.append({
            'name': name.get_text(strip=True),
            'price': price.get_text(strip=True)
        })

    return cpu_info_list

def scrape_cpu_info_pg2 (file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
        
    soup = BeautifulSoup(html_content, "html.parser")
    
    cpu_names = soup.find_all(class_="ProductName-sc-d3c4p4-6")[:24]
    cpu_prices = soup.find_all("span", class_="PriceLabel-sc-lboeq9-0")[:24]
    
    cpu_info_list = []
    for name,price in zip(cpu_names, cpu_prices):
        cpu_info_list.append({
            "name": name.get_text(strip=True),
            "price": price.get_text(strip=True),
        })
        
    return cpu_info_list