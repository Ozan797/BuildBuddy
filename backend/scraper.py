from bs4 import BeautifulSoup
import re
import requests
import json
import os.path

# Filter CPU data
def filer_empty_cpu_fields(data):
    # Define fields to check for emptiness
    fields_to_check = ['name', 'brand', 'price']  # Adjust fields based on your CPU data structure

    # Filter out objects with empty fields
    filtered_data = [entry for entry in data if all(entry.get(field) for field in fields_to_check)]

    return filtered_data


# CPU Web Scraper
def scrape_cpu_info_from_url(url):
    cpu_info_list = []  # Initialize list to store CPU information

    # Get HTML content from the URL
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')  # Create BeautifulSoup object

        # Find CPU names and prices from the HTML content
        cpu_names = soup.find_all(class_='ProductName-sc-d3c4p4-6')[:24]  # Limit to 24 CPU names
        cpu_prices = soup.find_all('span', class_='PriceLabel-sc-lboeq9-0')[:24]  # Limit to 24 CPU prices

        # Extract relevant data for each CPU
        for name, price in zip(cpu_names, cpu_prices):
            name = name.get_text(strip=True)  # Extract CPU name
            brand = name.split()[0] if name else ''  # Extracting the first word as brand

            # Check if the brand is AMD or Intel and add to the CPU info list
            if brand.lower() in ('amd', 'intel'):
                # Check for duplicates before adding to the list
                cpu_exists = any(cpu['name'] == name for cpu in cpu_info_list)
                if not cpu_exists:
                    cpu_info_list.append({
                        'name': name,
                        'brand': brand,
                        'price': price.get_text(strip=True)
                    })
    else:
        # Print error message if fetching content fails
        print(f"Failed to fetch content from {url}. Status code: {response.status_code}")

    return filer_empty_cpu_fields(cpu_info_list)

def filter_empty_gpu_field(data):
    fields_to_check = ['name', 'brand', 'memory', 'price']
    filtered_data = [entry for entry in data if all(entry.get(field) for field in fields_to_check)]
    return filtered_data

# GPU scraper
def scrape_gpu_info_from_url(url):
    gpu_info_list = []  # Initialize list to store GPU information

    # Get HTML content from the URL
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")  # Create BeautifulSoup object

        # Find GPU items from the HTML content
        gpu_items = soup.find_all('tr', class_='Tr-sc-1stvbsu-2 chMRiA')[:60]  # Limit to 60 GPU items

        # Extract relevant data for each GPU item
        for item in gpu_items:
            # Extract information
            full_name = item.find('h3', class_='ProductNameTable-sc-1stvbsu-3 bbvppQ').get_text(strip=True)
            price = item.find("span", class_="PriceLabel-sc-lboeq9-0").get_text(strip=True)
            extracted_price = re.search(r'£[\d,.]+', price)  # Remove any string except prices

            memory = ''
            gpu_properties = item.find_all('div', class_='PropertyContainer-sc-1stvbsu-11 TVmeo')
            for prop in gpu_properties:
                if 'gb' in prop.get_text(strip=True).lower():
                    memory = prop.get_text(strip=True)
                    break

            if extracted_price:
                brand = ''
                if 'geforce' in full_name.lower() or 'radeon' in full_name.lower() or "intel" in full_name.lower():
                    if 'geforce' in full_name.lower():
                        brand = 'NVIDIA GeForce'
                    elif 'radeon' in full_name.lower():
                        brand = 'AMD Radeon'
                    elif 'intel' in full_name.lower():
                        brand = 'Intel ARC'

                # Check for duplicates before adding to the list
                gpu_exists = any(gpu['name'] == full_name for gpu in gpu_info_list)
                if not gpu_exists:
                    gpu_info_list.append({
                        'name': full_name,
                        'brand': brand,
                        'memory': memory,
                        'price': extracted_price.group()
                    })

    return filter_empty_gpu_field(gpu_info_list)  # Return the list of GPU info
