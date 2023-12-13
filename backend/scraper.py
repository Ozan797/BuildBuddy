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
            price_value = None

            memory = ''
            gpu_properties = item.find_all('div', class_='PropertyContainer-sc-1stvbsu-11 TVmeo')
            for prop in gpu_properties:
                if 'gb' in prop.get_text(strip=True).lower():
                    memory_text = prop.get_text(strip=True).lower()
                    memory = int(re.search(r'\d+', memory_text).group()) if re.search(r'\d+', memory_text) else ''
                    break

            if extracted_price:
                price_value = float(extracted_price.group()[1:].replace(',', ''))  # Convert price to float

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
                        'price': price_value
                    })

    return filter_empty_gpu_fields(gpu_info_list)

# Remove RAM entries with empty fields
def filter_empty_ram_fields(data):
    required_fields = ['name', 'price', 'frequency', 'brand', 'ram_type']
    filtered_data = [entry for entry in data if all(entry.get(field) for field in required_fields)]
    return filtered_data

# Scrape RAM information from a URL
def scrape_ram_info_from_url(url):
    ram_info_list = []

    # Fetch HTML content
    response = requests.get(url)
    if response.status_code == 200:
        # Parse HTML content using BeautifulSoup
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        # Find product names and prices
        product_names = soup.find_all(class_='ProductNameTable-sc-1stvbsu-3 bbvppQ')
        product_prices = soup.find_all('span', {'class': 'PriceLabel-sc-lboeq9-0'})[:len(product_names)]

        # Extract information for each RAM product
        for name, price in zip(product_names, product_prices):
            # Extracting price value
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

            # Cleaning product names
            clean_name = name.text.strip().split('(')[0].strip()

            # Extracting brand from the product name
            brand = clean_name.split()[0]  # Extracting the first word as brand

            # Extracting MHz information from the product name
            frequency = ''
            if 'MHz' in clean_name:
                frequency = clean_name.split('MHz')[0].split()[-1]
                if frequency.isdigit():  # Ensuring it's a digit
                    frequency = int(frequency)

            # Extracting RAM type information from the product name
            ram_type = 'DDR4' if 'DDR4' in clean_name else ''  # Checking if 'DDR4' is present in the name

            # Check if the RAM entry exists and add to the RAM info list
            ram_exists = any(ram['name'] == clean_name for ram in ram_info_list)
            if not ram_exists and price_value is not None:
                ram_info_list.append({
                    'name': clean_name,
                    'price': price_value,
                    'frequency': frequency,
                    'brand': brand,
                    "ram_type": ram_type,
                })

    return filter_empty_ram_fields(ram_info_list)