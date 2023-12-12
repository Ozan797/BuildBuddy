from bs4 import BeautifulSoup
import re
import requests

# Filter CPU data by removing entries with empty fields
def filter_empty_cpu_fields(data):
    required_fields = ['name', 'brand', 'price']

    filtered_data = [entry for entry in data if all(entry.get(field) for field in required_fields)]
    return filtered_data

# Scrape CPU info from the provided URL
def scrape_cpu_info_from_url(url):
    cpu_info_list = []

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        cpu_names = soup.find_all(class_='ProductName-sc-d3c4p4-6')[:24]
        cpu_prices = soup.find_all('span', class_='PriceLabel-sc-lboeq9-0')[:24]

        for name, price in zip(cpu_names, cpu_prices):
            name_text = name.get_text(strip=True)
            brand = name_text.split()[0] if name_text else ''

            if brand.lower() in ('amd', 'intel'):
                cpu_exists = any(cpu['name'] == name_text for cpu in cpu_info_list)
                if not cpu_exists:
                    cpu_info_list.append({
                        'name': name_text,
                        'brand': brand,
                        'price': price.get_text(strip=True)
                    })
    else:
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

    return filter_empty_cpu_fields(cpu_info_list)

# Filter GPU data by removing entries with empty fields
def filter_empty_gpu_fields(data):
    required_fields = ['name', 'brand', 'memory', 'price']

    filtered_data = [entry for entry in data if all(entry.get(field) for field in required_fields)]
    return filtered_data

# Scrape GPU info from the provided URL
def scrape_gpu_info_from_url(url):
    gpu_info_list = []

    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        gpu_items = soup.find_all('tr', class_='Tr-sc-1stvbsu-2 chMRiA')[:60]

        for item in gpu_items:
            full_name = item.find('h3', class_='ProductNameTable-sc-1stvbsu-3 bbvppQ').get_text(strip=True)
            price = item.find("span", class_="PriceLabel-sc-lboeq9-0").get_text(strip=True)
            extracted_price = re.search(r'£[\d,.]+', price)

            memory = ''
            gpu_properties = item.find_all('div', class_='PropertyContainer-sc-1stvbsu-11 TVmeo')
            for prop in gpu_properties:
                if 'gb' in prop.get_text(strip=True).lower():
                    memory = prop.get_text(strip=True)
                    break

            if extracted_price:
                brand = ''
                if any(keyword in full_name.lower() for keyword in ['geforce', 'radeon', 'intel']):
                    if 'geforce' in full_name.lower():
                        brand = 'NVIDIA GeForce'
                    elif 'radeon' in full_name.lower():
                        brand = 'AMD Radeon'
                    elif 'intel' in full_name.lower():
                        brand = 'Intel ARC'

                gpu_exists = any(gpu['name'] == full_name for gpu in gpu_info_list)
                if not gpu_exists:
                    gpu_info_list.append({
                        'name': full_name,
                        'brand': brand,
                        'memory': memory,
                        'price': extracted_price.group()
                    })

    return filter_empty_gpu_fields(gpu_info_list)
